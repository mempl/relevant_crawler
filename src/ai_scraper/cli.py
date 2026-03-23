"""CLI entrypoint for the AI scraper."""

import argparse
import logging
import sys
from urllib.parse import urlparse

import anthropic

from .crawler import crawl
from .models import CrawlConfig, CrawlState
from .output import build_markdown, build_url_list

log = logging.getLogger(__name__)


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="ai-scraper",
        description=(
            "AI-powered focused web crawler. Uses Claude to judge which links "
            "to follow and which content is relevant, then outputs a single "
            "clean markdown file."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  # Single seed URL
  ai-scraper \\
      --urls "https://docs.databricks.com/en/genie/index.html" \\
      --topic "Databricks Genie documentation and features" \\
      --depth 3 -o genie_docs.md

  # Multiple seed URLs
  ai-scraper \\
      --urls "https://docs.example.com/a" "https://docs.example.com/b" \\
      --topic "Example SDK" --depth 2

  # Load URLs from a file (one per line)
  ai-scraper \\
      --urls-file seeds.txt \\
      --topic "Databricks Genie" -o genie.md

  # Just list the URLs that would be scraped (dry-run-ish)
  ai-scraper \\
      --urls "https://docs.example.com" \\
      --topic "Example SDK" --list-urls
        """,
    )

    # --- URL sources (at least one required) ---
    url_group = p.add_argument_group("seed URLs (provide at least one)")
    url_group.add_argument(
        "--urls", nargs="+", default=[],
        help="One or more seed URLs to start crawling from.",
    )
    url_group.add_argument(
        "--urls-file",
        help=(
            "Path to a text file containing seed URLs, one per line. "
            "Blank lines and lines starting with # are ignored."
        ),
    )

    # --- Core options ---
    p.add_argument(
        "--topic", required=True,
        help="Topic description — the AI uses this to judge relevance.",
    )
    p.add_argument(
        "--depth", type=int, default=3,
        help="Maximum crawl depth (default: 3).",
    )
    p.add_argument(
        "--output", "-o", default="output.md",
        help="Output markdown file path (default: output.md).",
    )
    p.add_argument(
        "--domains", nargs="*", default=None,
        help="Allowed domains. Default: inferred from seed URLs.",
    )
    p.add_argument(
        "--max-pages", type=int, default=100,
        help="Maximum number of pages to scrape (default: 100).",
    )
    p.add_argument(
        "--delay", type=float, default=1.0,
        help="Delay between HTTP requests in seconds (default: 1.0).",
    )
    p.add_argument(
        "--model", default="claude-sonnet-4-20250514",
        help="Anthropic model to use (default: claude-sonnet-4-20250514).",
    )
    p.add_argument(
        "--list-urls", action="store_true",
        help=(
            "After crawling, print the list of scraped URLs to stdout "
            "(also saved as <output>.urls.txt)."
        ),
    )
    p.add_argument(
        "--verbose", "-v", action="store_true",
        help="Enable debug logging.",
    )

    return p.parse_args(argv)


def _load_urls_from_file(path: str) -> list[str]:
    """Read URLs from a text file (one per line, # comments, blank lines ok)."""
    urls = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                urls.append(line)
    return urls


def main(argv: list[str] | None = None) -> None:
    args = _parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    # Collect seed URLs from both sources
    seed_urls: list[str] = list(args.urls)
    if args.urls_file:
        seed_urls.extend(_load_urls_from_file(args.urls_file))

    if not seed_urls:
        log.error("No seed URLs provided. Use --urls and/or --urls-file.")
        sys.exit(1)

    # Infer domain whitelist
    if args.domains:
        domains = args.domains
    else:
        domains = list({urlparse(u).netloc for u in seed_urls})
    log.info("Allowed domains: %s", domains)

    # Build config
    config = CrawlConfig(
        topic=args.topic,
        seed_urls=seed_urls,
        max_depth=args.depth,
        max_pages=args.max_pages,
        request_delay=args.delay,
        domain_whitelist=domains,
        model=args.model,
    )

    # Init Anthropic client (reads ANTHROPIC_API_KEY from env)
    client = anthropic.Anthropic()

    state = CrawlState(config=config)

    log.info(
        "Starting crawl — topic: %s, depth: %d, seeds: %d URLs",
        config.topic, config.max_depth, len(config.seed_urls),
    )

    crawl(state, client)

    if not state.pages:
        log.warning("No pages collected!")
        sys.exit(0)

    # Write main markdown output
    md_output = build_markdown(state)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(md_output)
    log.info("✅ Written %d pages to %s", len(state.pages), args.output)

    # Write / print URL list
    url_list = build_url_list(state)
    urls_path = args.output.rsplit(".", 1)[0] + ".urls.txt"
    with open(urls_path, "w", encoding="utf-8") as f:
        f.write(url_list)
    log.info("📋 URL list saved to %s", urls_path)

    if args.list_urls:
        print("\n" + url_list)


if __name__ == "__main__":
    main()
