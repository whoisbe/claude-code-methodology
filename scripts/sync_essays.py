#!/usr/bin/env python3
"""Sync the Newsletter essay list in README.md from the Substack RSS feed.

Reads https://whoisb.substack.com/feed, filters out the "Coming soon"
placeholder, and rewrites the block between <!-- ESSAYS:START --> and
<!-- ESSAYS:END --> in README.md.

Exits 0 whether or not anything changed. Exits non-zero on parse/network failure.
"""
from __future__ import annotations

import re
import sys
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET
from zoneinfo import ZoneInfo

FEED_URL = "https://whoisb.substack.com/feed"
REPO_ROOT = Path(__file__).resolve().parent.parent
README = REPO_ROOT / "README.md"
START_MARKER = "<!-- ESSAYS:START -->"
END_MARKER = "<!-- ESSAYS:END -->"
ET_TZ = ZoneInfo("America/New_York")

IGNORED_PUBDATE = "2025-11-17"
IGNORED_TITLES = {"coming soon"}


def fetch_feed(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "claude-code-methodology-sync/1.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def parse_items(xml_bytes: bytes) -> list[tuple[str, str, str]]:
    root = ET.fromstring(xml_bytes)
    items: list[tuple[str, str, str]] = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pubdate_raw = (item.findtext("pubDate") or "").strip()
        if not (title and link and pubdate_raw):
            continue
        dt = parsedate_to_datetime(pubdate_raw).astimezone(ET_TZ)
        date_iso = dt.strftime("%Y-%m-%d")
        if title.lower() in IGNORED_TITLES or date_iso == IGNORED_PUBDATE:
            continue
        items.append((date_iso, title, link))
    items.sort(key=lambda row: row[0], reverse=True)
    return items


def render_block(items: list[tuple[str, str, str]]) -> str:
    return "\n".join(f"- **{date}** — [{title}]({link})" for date, title, link in items)


def splice(readme_text: str, block: str) -> str:
    pattern = re.compile(
        re.escape(START_MARKER) + r"\n.*?\n" + re.escape(END_MARKER),
        re.DOTALL,
    )
    replacement = f"{START_MARKER}\n{block}\n{END_MARKER}"
    new_text, count = pattern.subn(replacement, readme_text, count=1)
    if count != 1:
        raise RuntimeError(
            f"Expected exactly one {START_MARKER}/{END_MARKER} block in README.md"
        )
    return new_text


def main() -> int:
    try:
        xml_bytes = fetch_feed(FEED_URL)
        items = parse_items(xml_bytes)
    except Exception as exc:
        print(f"sync_essays: failed to fetch/parse feed: {exc}", file=sys.stderr)
        return 1
    if not items:
        print("sync_essays: no essays parsed after filtering", file=sys.stderr)
        return 1
    block = render_block(items)
    current = README.read_text()
    updated = splice(current, block)
    if updated == current:
        print("sync_essays: README already up to date")
        return 0
    README.write_text(updated)
    print(f"sync_essays: README updated with {len(items)} essays")
    return 0


if __name__ == "__main__":
    sys.exit(main())
