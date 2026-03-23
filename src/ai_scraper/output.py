"""Output formatting — builds the final combined markdown."""

import re
import time

from .models import CrawlState


def build_markdown(state: CrawlState) -> str:
    """Combine all collected pages into a single markdown document."""
    parts: list[str] = []

    parts.append(f"# {state.config.topic}\n")
    parts.append(
        f"*Scraped {len(state.pages)} pages on {time.strftime('%Y-%m-%d')}*\n"
    )
    parts.append("---\n")

    # Table of contents
    parts.append("## Table of Contents\n")
    for i, page in enumerate(state.pages, 1):
        anchor = re.sub(r"[^a-z0-9]+", "-", page.title.lower()).strip("-")
        parts.append(f"{i}. [{page.title}](#{anchor})")
    parts.append("\n---\n")

    # Page content
    for page in state.pages:
        parts.append(f"## {page.title}\n")
        parts.append(f"*Source: {page.url}*\n")
        parts.append(page.markdown)
        parts.append("\n\n---\n")

    return "\n".join(parts)


def build_url_list(state: CrawlState) -> str:
    """Return a plain-text list of all scraped URLs."""
    lines = [f"# URLs scraped for: {state.config.topic}", ""]
    for i, page in enumerate(state.pages, 1):
        lines.append(f"{i}. {page.url}")
    lines.append(f"\nTotal: {len(state.pages)} pages")
    return "\n".join(lines)
