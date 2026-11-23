# Changelog

What changed in each release of cook.md (the website, recipe import and
sync), newest first. A release with nothing to say to the people who use it is
left out. Internal engineering notes stay in the private repository; this file
is generated from it.

## [0.23.101] - 2026-11-23

### Fixed

- The gift page's "Continue to payment" button opens the payment page. In
  0.23.100 it answered "The payment page could not be opened" for everyone.

## [0.23.100] - 2026-11-23

### Added

- You can give someone a year of Cook Basic or Cook Pro at cook.md/gift. It is
  one payment that does not renew, sent by email on the day you choose or
  printed, and redeemed at cook.md/redeem without a card.

## [0.23.99] - 2026-11-22

### Fixed

- The blog was fact-checked, all 20 posts. Posts no longer say recipe
  imports are part of Cook Pro or that Kickstart gives fifteen recipes,
  the CookBot post says what it can read in your folder, and the Paprika
  and meal-kit comparisons use the vendors' current plans and prices.
- The help pages were checked against the released apps and corrected.
  The iOS and Android pages and the in-app FAQ describe the apps as they
  are now: no storage chooser, recipes can be written and edited on the
  phone, the shopping list syncs, and which imports need a plan.
- The CookBot help says what CookBot can read (any file in the folder you
  have open) and that conversations are kept for 90 days. It used to say
  only shared files were sent and nothing was stored.
- The Sync Agent, Cook Editor, Cookify, Cook MCP, Nutrition API, plugin
  and report-template pages no longer give commands, file paths, limits
  or code samples that do not work. Cook MCP is no longer said to work
  with ChatGPT.

## [0.23.93] - 2026-11-20

### Added

- A guide to checking a meal plan against daily nutrient targets, at
  `/help/guides/nutrient-targets`.

## [0.23.92] - 2026-11-18

### Fixed

- A sign-in form sent twice no longer shows "Code has expired". Sign-in codes
  last 10 minutes.

## [0.23.91] - 2026-11-17

### Changed

- Converting a recipe on the web without signing in is limited to 10 a day.
- The pricing page and the sync help now say that sync covers your shopping
  list as well as your recipes.

## [0.23.90] - 2026-11-14

### Added

- The apps page shows a QR code to the store when you open it on a computer.
- The convert page links to the Recipe Clipper browser extension.

### Fixed

- A message sent through the contact form while signed in may contain links.

## [0.23.89] - 2026-11-14

### Fixed

- An import that fails now says why.
- The error page says so when a page or a text holds no recipe.

## [0.23.88] - 2026-11-13

### Added

- Bulk import from a pasted list of recipe links, up to 100 at a time. You get
  an email with a zip of `.cook` files, and a `failed-links.txt` naming the
  links that did not convert.

### Fixed

- An amount written as `6-1/2` is read as a number.
- Converting units keeps a container's count ("2 cans" stays 2 cans).
- A source that is only a list of lines, with no method, keeps its lines
  instead of being refused.

## [0.23.86] - 2026-11-12

### Fixed

- Importing a text that is only a link imports the page behind the link.
- Saving an edited recipe keeps its line breaks.

## [0.23.84] - 2026-11-10

### Added

- cook.md accepts recipes sent by the Recipe Clipper browser extension.

## [0.23.82] - 2026-11-10

### Added

- The home page shows your tools as tiles once you are signed in.
- Bulk import is linked from the home page, the sidebar, the convert help and
  the import form.

## [0.23.81] - 2026-11-09

### Added

- Bulk import takes a zip of your own text and Markdown files.

### Changed

- Bulk import converts up to 2,000 recipes a month.

## [0.23.80] - 2026-11-08

### Fixed

- A site that blocks the importer is reported as that, instead of "No recipe
  found".
