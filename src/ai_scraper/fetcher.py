"""HTML fetching, cleaning, and markdown conversion."""

import logging
import re
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Comment, Tag
from markdownify import markdownify as md

log = logging.getLogger(__name__)

# Exact class/id tokens that indicate boilerplate.
# Checked as whole-word matches to avoid "nav" matching "navigate".
STRIP_CLASS_EXACT = {
    "navbar", "sidebar", "footer", "breadcrumb", "cookie-banner",
    "advertisement", "ads", "popup", "modal", "share-buttons",
    "signup-banner", "signin", "login-form",
}

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
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


def _should_strip_element(el: Tag) -> bool:
    """Decide whether an element is boilerplate."""
    tag = el.name
    if tag in ("script", "style", "noscript", "iframe", "svg", "link", "meta"):
        return True

    try:
        raw_classes = el.attrs.get("class", [])
    except AttributeError:
        return False

    if isinstance(raw_classes, list):
        class_set = {str(c).lower() for c in raw_classes}
    else:
        class_set = {str(raw_classes).lower()} if raw_classes else set()

    el_id = str(el.attrs.get("id", "") or "").lower()

    if class_set & STRIP_CLASS_EXACT:
        return True
    if el_id in STRIP_CLASS_EXACT:
        return True

    return False


def clean_html(html: str) -> BeautifulSoup:
    """Remove boilerplate elements from HTML — conservatively."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove comments
    for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
        comment.extract()

    # Remove clearly unwanted elements
    for el in list(soup.find_all(True)):
        if not isinstance(el, Tag):
            continue
        if _should_strip_element(el):
            try:
                el.decompose()
            except Exception:
                pass

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
    """Convert cleaned HTML to markdown.

    Tries to find the main content area, falls back to full body.
    """
    candidates = [
        soup.find("main"),
        soup.find("article"),
        soup.find("div", {"role": "main"}),
        soup.find("div", class_=re.compile(r"\bcontent\b", re.I)),
        soup.find("div", class_=re.compile(r"\bdoc\b", re.I)),
        soup.find("div", class_=re.compile(r"\bmarkdown\b", re.I)),
        soup.find("div", class_=re.compile(r"\barticle\b", re.I)),
        soup.find("section", class_=re.compile(r"\bcontent\b", re.I)),
    ]

    target = None
    for c in candidates:
        if c and len(c.get_text(strip=True)) > 100:
            target = c
            break

    if target is None:
        target = soup.body or soup

    raw_md = md(str(target), heading_style="ATX", strip=["img"])

    # Clean up whitespace but preserve structure
    raw_md = re.sub(r"\n{3,}", "\n\n", raw_md)
    raw_md = re.sub(r"[ \t]+\n", "\n", raw_md)
    raw_md = re.sub(r"\n[ \t]+\n", "\n\n", raw_md)

    return raw_md.strip()


def get_title(html: str) -> str:
    """Extract the page title from raw HTML."""
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    if h1 and len(h1.get_text(strip=True)) > 3:
        return h1.get_text(strip=True)
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return "Untitled"
