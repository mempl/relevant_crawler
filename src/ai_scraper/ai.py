"""AI-powered relevance judgment for links and page content."""

import json
import logging
import re
from typing import Optional
from urllib.parse import urlparse

import anthropic

log = logging.getLogger(__name__)


def judge_links(
    client: anthropic.Anthropic,
    model: str,
    topic: str,
    current_url: str,
    links: list[dict],
    domain_whitelist: list[str],
) -> list[str]:
    """Ask Claude which links are relevant to the topic.

    Returns a list of URLs deemed relevant.
    """
    filtered = []
    for link in links:
        parsed = urlparse(link["url"])
        if any(parsed.netloc.endswith(d) for d in domain_whitelist):
            filtered.append(link)

    if not filtered:
        return []

    link_list = "\n".join(
        f"{i + 1}. [{l['text']}]({l['url']})" for i, l in enumerate(filtered)
    )

    prompt = f"""You are a focused web crawler assistant. You are crawling documentation about:

TOPIC: {topic}

You are currently on: {current_url}

Below is a list of links found on this page. Return ONLY the numbers of links that
are likely to lead to pages with relevant documentation content about the topic.

Be GENEROUS — include links if there's a reasonable chance they lead to relevant
content. It's better to follow a few extra links than miss important pages.

Exclude only links that are clearly:
- Login / signup / pricing pages
- Community forums / support tickets
- Completely unrelated products or topics
- External sites to different companies

Return a JSON array of numbers, e.g. [1, 3, 5]. If none are relevant, return [].

LINKS:
{link_list}"""

    try:
        resp = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        text = resp.content[0].text.strip()
        match = re.search(r"\[[\d\s,]*\]", text)
        if match:
            indices = json.loads(match.group())
            return [
                filtered[i - 1]["url"]
                for i in indices
                if 1 <= i <= len(filtered)
            ]
    except Exception as e:
        log.warning("AI link judgment failed: %s", e)

    return []


def clean_content(
    client: anthropic.Anthropic,
    model: str,
    topic: str,
    title: str,
    markdown: str,
) -> str:
    """Ask Claude to clean the scraped markdown — remove boilerplate remnants
    but KEEP all documentation text.

    Always returns content (never discards a page entirely).
    """
    # Truncate very long pages to avoid blowing context
    truncated = markdown[:15000]

    prompt = f"""You are a documentation extraction assistant. Clean up this scraped
web page content for inclusion in a documentation collection.

TOPIC: {topic}
PAGE TITLE: {title}

Instructions:
1. KEEP all documentation text, explanations, code examples, tables, lists,
   warnings, notes, and technical content. When in doubt, KEEP it.
2. REMOVE only obvious non-content: navigation menus, cookie banners, footer
   boilerplate ("© 2024 Company..."), sidebar widget text, "Related articles"
   link lists, breadcrumb trails, "Was this helpful?" prompts, share buttons text.
3. Preserve all markdown formatting (headings, code blocks, lists, bold, links).
4. Do NOT summarize or shorten the content. Return it in full.
5. Do NOT add any commentary, preamble, or wrapping. Return ONLY the cleaned markdown.
6. Do NOT wrap the output in code fences.

PAGE CONTENT:

{truncated}"""

    try:
        resp = client.messages.create(
            model=model,
            max_tokens=8192,
            messages=[{"role": "user", "content": prompt}],
        )
        cleaned = resp.content[0].text.strip()
        # If the AI returned something very short compared to input, something
        # went wrong — fall back to raw content
        if len(cleaned) < len(truncated) * 0.1 and len(truncated) > 500:
            log.warning(
                "   ⚠️  AI returned suspiciously short content (%d vs %d chars), "
                "keeping raw markdown.",
                len(cleaned), len(truncated),
            )
            return truncated
        return cleaned
    except Exception as e:
        log.warning("AI content cleaning failed: %s — keeping raw content", e)
        return truncated
