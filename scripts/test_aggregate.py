#!/usr/bin/env python3
"""Checks for aggregate.py. Run with `python3 scripts/test_aggregate.py`."""

import datetime
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("aggregate.py")
spec = importlib.util.spec_from_file_location("aggregate", SCRIPT)
aggregate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aggregate)

KEEP = """# Changelog

Preamble with a list:
- not an entry

## [Unreleased]

### Added

- Not out yet.

## [0.14.1] - 2026-11-19

### Fixed

- Sync no longer stops
  over an empty list.

### Internal

- Private.

## [0.14.0] - 2026-10-17

### Added

- Notes in cooking mode.
"""

PLEASE = """# Changelog

## [0.41.1](https://github.com/o/r/compare/v0.41.0...v0.41.1) (2026-11-09)


### Continuous Integration

* **release:** build on macos-15 ([#831](https://github.com/o/r/issues/831)) ([542275b](https://github.com/o/r/commit/542275bb))

## [0.41.0](https://github.com/o/r/compare/v0.40.0...v0.41.0) (2026-11-07)


### Features

* add days to the list ([#611](https://github.com/o/r/issues/611)) ([c53c97f](https://github.com/o/r/commit/c53c97f0))

### Bug Fixes

* repair Greek ([d1b078d](https://github.com/o/r/commit/d1b078de))

## [0.1.0-alpha.60](https://github.com/o/r/compare/a...b) (2026-11-01)

### Bug Fixes

* recover the server
"""


class Parse(unittest.TestCase):
    def test_keep_a_changelog(self):
        releases = aggregate.parse(KEEP)
        self.assertEqual([r[0] for r in releases], ["0.14.1", "0.14.0"])
        self.assertEqual(releases[0][1], "2026-11-19")
        self.assertEqual(releases[0][2], {"Fixed": ["- Sync no longer stops\n  over an empty list."]})

    def test_unreleased_internal_and_preamble_are_dropped(self):
        text = repr(aggregate.parse(KEEP))
        for private in ("Not out yet", "Private", "not an entry"):
            self.assertNotIn(private, text)

    def test_release_please(self):
        releases = aggregate.parse(PLEASE)
        # 0.41.1 has only CI notes, so it is not a release worth listing
        self.assertEqual([r[0] for r in releases], ["0.41.0", "0.1.0-alpha.60"])
        self.assertEqual(
            releases[0][2],
            {
                "Added": ["- add days to the list ([#611](https://github.com/o/r/issues/611))"],
                "Fixed": ["- repair Greek"],
            },
        )

    def test_heading_inside_a_code_block_is_not_a_release(self):
        text = "## [1.0.0] - 2026-01-02\n\n### Added\n\n- One.\n\n  ```\n  ## [9.9.9] - 2026-01-03\n  ```\n"
        self.assertEqual([r[0] for r in aggregate.parse(text)], ["1.0.0"])


class Render(unittest.TestCase):
    def test_months_newest_first_then_products_in_order(self):
        products = [
            ("iOS", "ios-link", aggregate.parse(KEEP)),
            ("CLI", "cli-link", aggregate.parse(PLEASE)),
        ]
        out = aggregate.render(products, "2026-01")
        self.assertLess(out.index("## November 2026"), out.index("## October 2026"))
        november = out[out.index("## November 2026"):out.index("## October 2026")]
        self.assertLess(november.index("### [iOS](ios-link)"), november.index("### [CLI](cli-link)"))
        self.assertIn("#### 0.41.0 · 2026-11-07", november)
        self.assertLess(november.index("0.41.0"), november.index("alpha.60"))
        self.assertNotIn("CLI", out[out.index("## October 2026"):])

    def test_floor_cuts_older_months(self):
        out = aggregate.render([("iOS", "l", aggregate.parse(KEEP))], "2026-11")
        self.assertNotIn("October", out)

    def test_first_month(self):
        self.assertEqual(aggregate.first_month(datetime.date(2026, 11, 20), 12), "2025-12")
        self.assertEqual(aggregate.first_month(datetime.date(2026, 1, 5), 1), "2026-01")
        self.assertEqual(aggregate.first_month(datetime.date(2026, 1, 5), 2), "2025-12")


class CommandLine(unittest.TestCase):
    def run_script(self, directory, *extra):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--source-dir", str(directory),
             "--out", str(directory / "OUT.md"), "--today", "2026-11-20", *extra],
            capture_output=True, text=True,
        )

    def test_writes_the_same_bytes_twice(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            for key, *_ in aggregate.SOURCES:
                (directory / (key + ".md")).write_text(KEEP)
            self.assertEqual(self.run_script(directory).returncode, 0)
            first = (directory / "OUT.md").read_bytes()
            self.assertEqual(self.run_script(directory).returncode, 0)
            self.assertEqual(first, (directory / "OUT.md").read_bytes())
            self.assertIn(b"Cook for Android", first)

    def test_a_missing_or_empty_source_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            for key, *_ in aggregate.SOURCES[1:]:
                (directory / (key + ".md")).write_text(KEEP)
            self.assertEqual(self.run_script(directory).returncode, 2)
            (directory / (aggregate.SOURCES[0][0] + ".md")).write_text("# Changelog\n")
            self.assertEqual(self.run_script(directory).returncode, 2)
            self.assertFalse((directory / "OUT.md").exists())


if __name__ == "__main__":
    unittest.main()
