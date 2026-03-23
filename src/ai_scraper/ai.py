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
    # Pre-filter: only links within whitelisted domains
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

Exclude links that look like:
- Login / signup pages
- Pricing / sales pages
- Community forums / support tickets
- Blog posts unrelated to the topic
- API references for unrelated products
- External sites
- Links that are clearly navigation/UI (e.g. "Back to top")
- Pagination links are OK if they continue relevant content

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


def judge_content(
    client: anthropic.Anthropic,
    model: str,
    topic: str,
    title: str,
    markdown: str,
) -> Optional[str]:
    """Ask Claude to clean the content — remove irrelevant sections.

    Returns cleaned markdown, or None if the page is entirely irrelevant.
    """
    # Truncate very long pages to stay within context limits
    truncated = markdown[:12000]

    prompt = f"""You are a documentation extraction assistant. Your job is to clean up
scraped web content and return ONLY the parts relevant to the topic.

TOPIC: {topic}
PAGE TITLE: {title}

Below is markdown extracted from a web page. Please:
1. Remove any remaining ads, navigation remnants, cookie notices, footer text,
   sidebar content, "related articles" sections, and other boilerplate.
2. Remove content that is NOT relevant to the topic.
3. Keep all technical documentation, code examples, explanations, tables, and
   headings that ARE relevant.
4. Preserve the original markdown formatting (headings, code blocks, lists, etc).
5. If the page is entirely irrelevant to the topic, respond with exactly: IRRELEVANT

Return ONLY the cleaned markdown, nothing else. Do not wrap it in code fences."""

    try:
        resp = client.messages.create(
            model=model,
            max_tokens=4096,
            messages=[{"role": "user", "content": f"{prompt}\n\n---\n\n{truncated}"}],
        )
        text = resp.content[0].text.strip()
        if text == "IRRELEVANT":
            return None
        return text
    except Exception as e:
        log.warning("AI content judgment failed: %s — keeping raw content", e)
        return markdown
