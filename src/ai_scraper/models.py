"""Data models for the crawler."""

from dataclasses import dataclass, field


@dataclass
class Page:
    """A single scraped page."""

    url: str
    title: str
    markdown: str
    depth: int


@dataclass
class CrawlConfig:
    """Configuration for a crawl run."""

    topic: str
    seed_urls: list[str]
    max_depth: int = 3
    max_pages: int = 100
    request_delay: float = 1.0
    request_timeout: int = 15
    domain_whitelist: list[str] = field(default_factory=list)
    model: str = "claude-sonnet-4-20250514"


@dataclass
class CrawlState:
    """Mutable state during a crawl."""

    config: CrawlConfig
    visited: set[str] = field(default_factory=set)
    pages: list[Page] = field(default_factory=list)
    queue: list[tuple[str, int]] = field(default_factory=list)  # (url, depth)
