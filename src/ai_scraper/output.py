"""Output formatting — builds the final combined markdown."""

import re
import time

from .models import CrawlState


def build_markdown(state: CrawlState) -> str:
    """Combine all collected pages into a single markdown document."""
    parts: list[str] = []

    parts.append(f"# {state.config.topic}")
    parts.append("")
    parts.append(
        f"*Scraped {len(state.pages)} pages on {time.strftime('%Y-%m-%d %H:%M')}*"
    )
    parts.append("")

    # ---- Table of Contents ----
    parts.append("---")
    parts.append("")
    parts.append("## Table of Contents")
    parts.append("")
    for i, page in enumerate(state.pages, 1):
        parts.append(f"{i}. [{page.title}]({page.url})")
    parts.append("")

    # ---- Page content ----
    for i, page in enumerate(state.pages, 1):
        parts.append("=" * 80)
        parts.append("")
        parts.append(f"## {i}. {page.title}")
        parts.append("")
        parts.append(f"**URL:** {page.url}")
        parts.append(f"**Crawl depth:** {page.depth}")
        parts.append("")
        parts.append("---")
        parts.append("")
        parts.append(page.markdown)
        parts.append("")
        parts.append("")

    return "\n".join(parts)


def build_url_list(state: CrawlState) -> str:
    """Return a plain-text list of all scraped URLs."""
    lines = [f"# URLs scraped for: {state.config.topic}", ""]
    for i, page in enumerate(state.pages, 1):
        lines.append(f"{i}. [{page.title}] {page.url}")
    lines.append(f"\nTotal: {len(state.pages)} pages")
    return "\n".join(lines)
