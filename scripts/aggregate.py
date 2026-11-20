#!/usr/bin/env python3
"""Build CHANGELOG.md, the "What's new" across every Cook app, from each
product's own public changelog.

Each source is a Markdown changelog in one of two shapes:

    ## [0.14.1] - 2026-11-19            Keep a Changelog (iOS, Android, cook.md)
    ## [0.41.0](compare-url) (2026-11-07)   release-please (CookCLI, Cook Editor)

Only the subsections in SECTIONS are carried over, under one name each
(`Features` reads as `Added`, `Bug Fixes` as `Fixed`). Anything else, such as
`Continuous Integration` or `Miscellaneous Chores`, is not news and is dropped,
and so is a release left with no entries. release-please's trailing commit
links are removed; pull request links stay.

The output groups releases by month, newest first, then by product in the
order of SOURCES. It has no timestamp, so a run that finds nothing new
writes the same bytes and the workflow has nothing to commit.

    aggregate.py                      # fetch every source, write CHANGELOG.md
    aggregate.py --months 6           # how far back to go (default 12)
    aggregate.py --source-dir DIR     # read DIR/<key>.md instead of fetching

A source that cannot be fetched or has no release at all is an error (exit
status 2) and nothing is written: a network failure must not publish a
changelog with a product missing.
"""

import argparse
import datetime
import re
import sys
import urllib.request
from pathlib import Path

RAW = "https://raw.githubusercontent.com/%s/HEAD/CHANGELOG.md"
PAGE = "https://github.com/%s/blob/HEAD/CHANGELOG.md"

# key, title, where to read it, where a person reads it
SOURCES = [
    ("ios", "Cook for iOS", RAW % "cook-md/ios-app", PAGE % "cook-md/ios-app"),
    ("android", "Cook for Android", RAW % "cook-md/android-app", PAGE % "cook-md/android-app"),
    ("cook-cloud", "cook.md", "changelogs/cook-cloud.md", "changelogs/cook-cloud.md"),
    ("cookcli", "CookCLI", RAW % "cooklang/cookcli", PAGE % "cooklang/cookcli"),
    ("editor", "Cook Editor", RAW % "cook-md/editor", PAGE % "cook-md/editor"),
]

SECTIONS = {
    "added": "Added",
    "features": "Added",
    "changed": "Changed",
    "performance improvements": "Changed",
    "deprecated": "Deprecated",
    "removed": "Removed",
    "fixed": "Fixed",
    "bug fixes": "Fixed",
    "security": "Security",
}
SECTION_ORDER = ["Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"]

RELEASE = re.compile(
    r"^##\s+\[?v?(?P<version>\d[^\]\s(]*)\]?(?:\([^)]*\))?\s*(?:-\s*|\()(?P<date>\d{4}-\d{2}-\d{2})\)?\s*$"
)
COMMIT_LINK = re.compile(r"\s*\(\[[0-9a-f]{7,40}\]\([^)]*/commit/[^)]*\)\)")
MONTHS = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December",
]

PREAMBLE = """# What's new in Cook

What changed in every Cook app, newest first. This file is generated each day
from the products' own changelogs by `scripts/aggregate.py`; do not edit it by
hand. Each product's full history is linked from its heading.
"""


class SourceError(Exception):
    """A source could not be read, or holds no release."""


def parse(text):
    """Return [(version, date, {section: [entry]})], in the file's order.

    An entry is a list item with its continuation lines, joined by newlines.
    """
    releases, current, section, in_code = [], None, None, False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
        heading = None if in_code else RELEASE.match(line)
        if heading:
            current = (heading.group("version"), heading.group("date"), {})
            releases.append(current)
            section = None
        elif not in_code and line.startswith("## "):
            current, section = None, None  # Unreleased, or prose
        elif current is None:
            continue
        elif not in_code and line.startswith("### "):
            section = SECTIONS.get(line[4:].strip().lower())
        elif section is None:
            continue
        elif re.match(r"^[-*] ", line) and not in_code:
            entry = COMMIT_LINK.sub("", "- " + line[2:].rstrip())
            current[2].setdefault(section, []).append(entry)
        elif line.strip() and section in current[2]:
            current[2][section][-1] += "\n" + line.rstrip()
    return [release for release in releases if release[2]]


def read_source(location, key, source_dir):
    if source_dir is not None:
        path = source_dir / (key + ".md")
    elif not location.startswith("https://"):
        path = Path(location)
    else:
        try:
            with urllib.request.urlopen(location, timeout=30) as response:
                return response.read().decode("utf-8")
        except OSError as error:
            raise SourceError("%s: %s" % (location, error))
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SourceError("%s: %s" % (path, error))


def first_month(today, months):
    """The `YYYY-MM` that starts a window of `months` months ending this month."""
    index = today.year * 12 + today.month - 1 - (months - 1)
    return "%04d-%02d" % (index // 12, index % 12 + 1)


def render(products, since):
    """`products` is [(title, link, releases)]; `since` is a `YYYY-MM` floor."""
    months = sorted(
        {date[:7] for _t, _l, releases in products for _v, date, _s in releases if date[:7] >= since},
        reverse=True,
    )
    out = [PREAMBLE]
    for month in months:
        out.append("## %s %s\n" % (MONTHS[int(month[5:]) - 1], month[:4]))
        for title, link, releases in products:
            mine = sorted(
                (r for r in releases if r[1][:7] == month), key=lambda r: r[1], reverse=True
            )
            if not mine:
                continue
            out.append("### [%s](%s)\n" % (title, link))
            for version, date, sections in mine:
                out.append("#### %s · %s\n" % (version, date))
                for section in SECTION_ORDER:
                    if section in sections:
                        out.append("**%s**\n\n%s\n" % (section, "\n".join(sections[section])))
    return "\n".join(out).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default="CHANGELOG.md", type=Path)
    parser.add_argument("--months", default=12, type=int)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument("--today", default=datetime.date.today().isoformat())
    args = parser.parse_args()

    products = []
    try:
        for key, title, location, link in SOURCES:
            releases = parse(read_source(location, key, args.source_dir))
            if not releases:
                raise SourceError("%s: no release found in %s" % (title, location))
            products.append((title, link, releases))
    except SourceError as error:
        print(error, file=sys.stderr)
        sys.exit(2)

    today = datetime.date.fromisoformat(args.today)
    args.out.write_text(render(products, first_month(today, args.months)), encoding="utf-8")


if __name__ == "__main__":
    main()
