"""Core crawl loop."""

import logging
import time

import anthropic

from .ai import judge_content, judge_links
from .fetcher import clean_html, extract_links, fetch_html, get_title, html_to_markdown
from .models import CrawlState, Page

log = logging.getLogger(__name__)


def crawl(state: CrawlState, client: anthropic.Anthropic) -> None:
    """Run the crawl loop, mutating *state* in place."""
    cfg = state.config

    # Seed the queue
    for url in cfg.seed_urls:
        state.queue.append((url, 0))

    while state.queue:
        if len(state.pages) >= cfg.max_pages:
            log.warning("Reached max page limit (%d), stopping.", cfg.max_pages)
            break

        url, depth = state.queue.pop(0)
        url = url.split("#")[0]

        if url in state.visited:
            continue
        state.visited.add(url)

        log.info(
            "📄 [depth=%d  pages=%d  queue=%d] %s",
            depth, len(state.pages), len(state.queue), url,
        )

        html = fetch_html(url, timeout=cfg.request_timeout)
        if html is None:
            continue

        time.sleep(cfg.request_delay)

        # Parse & clean
        soup = clean_html(html)
        title = get_title(html)
        raw_md = html_to_markdown(soup)

        if len(raw_md.strip()) < 50:
            log.info("   ⏭  Too little content, skipping.")
            continue

        # AI content check
        log.info("   🤖 Judging content relevance…")
        cleaned_md = judge_content(client, cfg.model, cfg.topic, title, raw_md)

        if cleaned_md is None:
            log.info("   ❌ Page deemed irrelevant, skipping.")
            continue

        log.info("   ✅ Accepted: %s", title)
        state.pages.append(Page(url=url, title=title, markdown=cleaned_md, depth=depth))

        # Follow links?
        if depth < cfg.max_depth:
            links = extract_links(html, url)
            if links:
                log.info("   🔗 Found %d links, asking AI which to follow…", len(links))
                relevant_urls = judge_links(
                    client, cfg.model, cfg.topic, url, links, cfg.domain_whitelist,
                )
                new_urls = [u for u in relevant_urls if u not in state.visited]
                log.info("   🔗 AI selected %d new links to follow.", len(new_urls))
                for u in new_urls:
                    state.queue.append((u, depth + 1))

    log.info("Crawl complete. Collected %d pages.", len(state.pages))
