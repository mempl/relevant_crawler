"""HTML fetching, cleaning, and markdown conversion."""

import logging
import re
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Comment
from markdownify import markdownify as md

log = logging.getLogger(__name__)

# Tags to strip entirely
STRIP_TAGS = [
    "nav", "footer", "header", "aside", "script", "style", "noscript",
    "iframe", "form", "button", "svg",
]

# Class / ID substrings that indicate boilerplate
STRIP_CLASSES = [
    "nav", "navbar", "sidebar", "footer", "header", "menu", "breadcrumb",
    "advertisement", "ad", "ads", "cookie", "banner", "popup", "modal",
    "social", "share", "comment", "related", "recommended", "toc",
    "table-of-contents", "signup", "signin", "login",
]

USER_AGENT = (
    "Mozilla/5.0 (compatible; AIScraper/0.1; "
    "+https://github.com/example/ai-scraper)"
)


def fetch_html(url: str, timeout: int = 15) -> Optional[str]:
    """Fetch raw HTML from a URL."""
    try:
        resp = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": USER_AGENT},
        )
        resp.raise_for_status()
        content_type = resp.headers.get("Content-Type", "")
        if "text/html" not in content_type and "application/xhtml" not in content_type:
            log.warning("Skipping non-HTML content at %s (%s)", url, content_type)
            return None
        return resp.text
    except requests.RequestException as e:
        log.warning("Failed to fetch %s: %s", url, e)
        return None


def clean_html(html: str) -> BeautifulSoup:
    """Remove boilerplate elements from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove comments
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()

    # Remove unwanted tags
    for tag_name in STRIP_TAGS:
        for tag in soup.find_all(tag_name):
            tag.decompose()

    # Remove elements whose class/id smells like boilerplate
    for el in soup.find_all(True):
        raw_classes = el.get("class", [])
        if isinstance(raw_classes, list):
            classes = " ".join(raw_classes)
        else:
            classes = str(raw_classes) if raw_classes else ""
        el_id = el.get("id", "") or ""
        combined = f"{classes} {el_id}".lower()
        if any(kw in combined for kw in STRIP_CLASSES):
            el.decompose()

    return soup


def extract_links(html: str, base_url: str) -> list[dict]:
    """Extract all links with their anchor text from raw HTML."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    seen = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(base_url, href).split("#")[0]

        if not full_url.startswith(("http://", "https://")):
            continue
        if full_url in seen:
            continue
        seen.add(full_url)

        text = a.get_text(strip=True) or href
        links.append({"url": full_url, "text": text})

    return links


def html_to_markdown(soup: BeautifulSoup) -> str:
    """Convert cleaned HTML to markdown, targeting main content area."""
    main = (
        soup.find("main")
        or soup.find("article")
        or soup.find("div", {"role": "main"})
        or soup.find("div", class_=re.compile(r"content|main|article|doc", re.I))
        or soup.body
        or soup
    )
    raw_md = md(str(main), heading_style="ATX", strip=["img"])
    raw_md = re.sub(r"\n{3,}", "\n\n", raw_md)
    raw_md = re.sub(r"[ \t]+\n", "\n", raw_md)
    return raw_md.strip()


def get_title(html: str) -> str:
    """Extract the page title from raw HTML."""
    soup = BeautifulSoup(html, "html.parser")
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)
    return "Untitled"
