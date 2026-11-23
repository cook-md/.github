# What's new in Cook

What changed in every Cook app, newest first. This file is generated each day
from the products' own changelogs by `scripts/aggregate.py`; do not edit it by
hand. Each product's full history is linked from its heading.

## November 2026

### [Cook for iOS](https://github.com/cook-md/ios-app/blob/HEAD/CHANGELOG.md)

#### 0.14.1 · 2026-11-19

**Fixed**

- Signing in with a large recipe library no longer stops at "Unexpected sync
  error" over an empty list. Recipes and photos now arrive in batches and
  show up as they download, and a sync interrupted by leaving the app picks
  up where it stopped instead of starting again.

#### 0.14.0 · 2026-11-17

**Added**

- Cooking mode now shows a recipe's notes. Each note gets a page of its own,
  in the place the recipe has it: before a step, between steps, or at the
  end. Notes that sit together share one page, and step numbers stay as they
  were. A web address in a note is a link you can tap.
- A Browser tab on Clip Recipe: browse to a recipe — including on sites you
  are signed in to — and clip it straight from the page. Select part of the
  page first to clip only that. "Browse the web" in the plus menu opens it.
- The app asks for a rating once you have added to the shopping list a few
  times: on the third addition, and once more on the fiftieth.

**Changed**

- "Start free trial" at the end of setup now opens the App Store sheet for
  the plan the card names, in one tap. If you close the sheet, you see all
  the plans. Once you have subscribed, setup ends and your recipes open.
  The card also has a sign-in link, Terms of Use, Privacy Policy and
  Restore.
- The plans screen now says that sync covers your shopping list as well as
  your recipes.
- Siri no longer reads the step aloud when you ask for the next or previous
  one in cooking mode. Say "Read the step in Cook" when you want to hear it.
- The free-trial card at the end of setup now says what the trial gives you:
  "Try all app features free for 7 days".

**Fixed**

- A section that has only notes and no steps is no longer missing from the
  recipe's steps.
- Sync no longer stops with "Sync error" after you leave the app and come
  back to it. Two sync sessions could end up running at once and block each
  other.

### [Cook for Android](https://github.com/cook-md/android-app/blob/HEAD/CHANGELOG.md)

#### 0.15.0 · 2026-11-17

**Added**

- Cook mode now shows a recipe's notes, on pages of their own in the place they have in the
  recipe. A web address in a note opens in the browser.
- A Browser tab on Clip Recipe: browse to a recipe, including on sites you are signed in to or
  that sit behind a paywall you subscribe to, and clip it from the page. Select part of the
  page first to clip only that. "Browse the web" in the + menu on My recipes opens the
  tab.

**Changed**

- Cook mode no longer opens a section with an empty ingredients page when the section uses
  no ingredients.
- "Skip" on any of the questions after "Get started" now closes them and opens an empty recipe
  list, so you can start with only your own recipes. "Get sample recipes" there asks the
  questions again, and "Skip" brings you back to the list without adding anything.

**Fixed**

- Stopping a paused timer no longer closes the app.
- A timer that finishes on a phone with no alarm sound set no longer closes the app; it
  vibrates and shows its notification.
- Tapping play on a timer whose time has gone back to zero no longer closes the app.
- On a phone without a system file picker, choosing a recipe folder or importing a file now
  shows a message instead of closing the app.
- A recipe whose title has a `:`, `?` or a similar character no longer shows up twice in a
  folder you chose yourself, and can be moved or renamed straight after it is saved.

### [cook.md](changelogs/cook-cloud.md)

#### 0.23.100 · 2026-11-23

**Added**

- You can give someone a year of Cook Basic or Cook Pro at cook.md/gift. It is
  one payment that does not renew, sent by email on the day you choose or
  printed, and redeemed at cook.md/redeem without a card.

#### 0.23.99 · 2026-11-22

**Fixed**

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

#### 0.23.93 · 2026-11-20

**Added**

- A guide to checking a meal plan against daily nutrient targets, at
  `/help/guides/nutrient-targets`.

#### 0.23.92 · 2026-11-18

**Fixed**

- A sign-in form sent twice no longer shows "Code has expired". Sign-in codes
  last 10 minutes.

#### 0.23.91 · 2026-11-17

**Changed**

- Converting a recipe on the web without signing in is limited to 10 a day.
- The pricing page and the sync help now say that sync covers your shopping
  list as well as your recipes.

#### 0.23.90 · 2026-11-14

**Added**

- The apps page shows a QR code to the store when you open it on a computer.
- The convert page links to the Recipe Clipper browser extension.

**Fixed**

- A message sent through the contact form while signed in may contain links.

#### 0.23.89 · 2026-11-14

**Fixed**

- An import that fails now says why.
- The error page says so when a page or a text holds no recipe.

#### 0.23.88 · 2026-11-13

**Added**

- Bulk import from a pasted list of recipe links, up to 100 at a time. You get
  an email with a zip of `.cook` files, and a `failed-links.txt` naming the
  links that did not convert.

**Fixed**

- An amount written as `6-1/2` is read as a number.
- Converting units keeps a container's count ("2 cans" stays 2 cans).
- A source that is only a list of lines, with no method, keeps its lines
  instead of being refused.

#### 0.23.86 · 2026-11-12

**Fixed**

- Importing a text that is only a link imports the page behind the link.
- Saving an edited recipe keeps its line breaks.

#### 0.23.84 · 2026-11-10

**Added**

- cook.md accepts recipes sent by the Recipe Clipper browser extension.

#### 0.23.82 · 2026-11-10

**Added**

- The home page shows your tools as tiles once you are signed in.
- Bulk import is linked from the home page, the sidebar, the convert help and
  the import form.

#### 0.23.81 · 2026-11-09

**Added**

- Bulk import takes a zip of your own text and Markdown files.

**Changed**

- Bulk import converts up to 2,000 recipes a month.

#### 0.23.80 · 2026-11-08

**Fixed**

- A site that blocks the importer is reported as that, instead of "No recipe
  found".

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.41.0 · 2026-11-07

**Added**

- add some days of a meal plan to the shopping list ([#611](https://github.com/cooklang/cookcli/issues/611))
- **server:** search results page with recipe cards and pictures ([#829](https://github.com/cooklang/cookcli/issues/829)), closes [#828](https://github.com/cooklang/cookcli/issues/828)

**Fixed**

- **deps:** update self_update to 1.3, so zip moves past its advisories ([#827](https://github.com/cooklang/cookcli/issues/827))
- **i18n:** repair Greek locale on main ([#821](https://github.com/cooklang/cookcli/issues/821))
- **server:** render cookware notes in web frontend ([#815](https://github.com/cooklang/cookcli/issues/815))

#### 0.40.0 · 2026-11-03

**Added**

- **i18n:** add Greek translation

**Fixed**

- **aisles:** take no typing or Save in the text tab until the file is in ([#797](https://github.com/cooklang/cookcli/issues/797))
- **build:** write the search index in path order ([#807](https://github.com/cooklang/cookcli/issues/807))
- **editor:** never write back a recipe renamed or deleted in another tab ([#809](https://github.com/cooklang/cookcli/issues/809))
- **editor:** send the pending text before asking for completions ([#805](https://github.com/cooklang/cookcli/issues/805))
- **editor:** show the save status in the page's language
- empty the checked log on Clear instead of removing it ([#814](https://github.com/cooklang/cookcli/issues/814))
- keep the shopping list's owner when rewriting it ([#814](https://github.com/cooklang/cookcli/issues/814))
- list recipes when the collection is on a Windows network drive ([#787](https://github.com/cooklang/cookcli/issues/787))
- recipe and ingredient names in any script ([#803](https://github.com/cooklang/cookcli/issues/803))
- **server:** keep a file's owner when the server rewrites it ([#814](https://github.com/cooklang/cookcli/issues/814))
- **server:** name the language cookie cook_lang so other apps can't shadow it ([#800](https://github.com/cooklang/cookcli/issues/800)), closes [#799](https://github.com/cooklang/cookcli/issues/799)
- **web:** name every form field and hide decorative icons from screen readers ([#801](https://github.com/cooklang/cookcli/issues/801))

### [Cook Editor](https://github.com/cook-md/editor/blob/HEAD/CHANGELOG.md)

#### 0.1.0-alpha.60 · 2026-11-14

**Fixed**

- **cooklang:** recover the language server instead of failing every keystroke ([#263](https://github.com/cook-md/editor/issues/263))

#### 0.1.0-alpha.59 · 2026-11-11

**Fixed**

- **preview:** stop header badges and actions overflowing in narrow panes ([#261](https://github.com/cook-md/editor/issues/261))

#### 0.1.0-alpha.58 · 2026-11-08

**Fixed**

- editor errors reported in Sentry on alpha.57 ([#252](https://github.com/cook-md/editor/issues/252))

## October 2026

### [Cook for iOS](https://github.com/cook-md/ios-app/blob/HEAD/CHANGELOG.md)

#### 0.13.0 · 2026-10-14

**Added**

- Favourites: tap the heart on a recipe to keep it, and find it on the new
  Favourites tab, as one list or grouped by tag, with its own search. They
  are saved in a `.bookmarks` file at the root of your collection, so they
  travel with your recipes.
- Manage your recipes in the app: create, edit, rename, move and delete
  recipes, move and delete folders, and import a `.cook` file from Files.
  Photos and favourites follow along, and most actions can be undone.
- Search your whole library by title, ingredient or tag, by typing or by
  voice, with recent searches and recently opened recipes ready before you
  type.
- Swipe a recipe or meal plan to add it to the shopping list, favourite it or
  delete it, or hold it for more.

**Changed**

- A new look for the recipe list, the recipe screen, meal plans and the empty
  shopping list. Steps sit on cards, and a recipe a step links to opens with
  a tap.
- "+" on the recipes tab opens a menu: create a recipe, import from a link,
  paste text, scan a photo or pick a file.
- Adding a recipe with linked recipes to the shopping list asks which of them
  to include, and the list keeps exactly what you chose.
- The ingredients and cookware tabs are each one list for the whole recipe,
  with linked recipes first.
- The recipe list shows each recipe by the title written in it.
- A shared recipe zip includes the step photos.

**Fixed**

- Step photos show on recipes without section headings, named
  `Recipe.2.jpg` or `Recipe.1.2.jpg`.
- Menus and `.webp` / `.heic` photos download from iCloud to your other
  devices like `.cook` files and `.jpg` photos.
- A photo set with `image:` at the top of a recipe shows on its screen again.
- On iPad, recipes and Settings open in a larger window, and opening a folder
  no longer makes the list jump.

#### 0.12.0 · 2026-10-07

**Added**

- Clip Recipe has a Text tab: paste a recipe from a note, a message or an
  email and it is turned into a Cooklang recipe.
- Share selected text from another app to Cook and it is converted straight
  away. If you're not signed in and hit the import limit, the text is carried
  into the app so you can sign in and finish there.
- Getting started asks three more questions — allergies, how much time you
  have on a weeknight, and what you'd like Cook to help with — so your first
  recipes fit you better. Recipes with an allergen you pick are left out.
- When your starter recipes are ready, a summary shows how many were added,
  what they were matched to and what to try next. If you don't have a plan
  yet, you can look at the plans from there — or start a free trial, when one
  is available to you.

**Changed**

- Meal plans are free for everyone: every day opens in full and Add all
  ingredients works, signed in or not.
- Hidden files and folders (names starting with a dot) no longer appear in
  your recipe list or in folder counts.

**Fixed**

- Sharing a recipe link to Cook while signed out and hitting the import limit
  now offers to sign in: it opens Cook, which signs you in and imports the
  recipe.
- Opening a folder in a large recipe library no longer freezes the app. Cook
  now reads only the folder you're looking at, and loads each recipe's picture
  as its row appears.
- A folder is no longer hidden when a recipe next to it has the same name.
- Recipes and meal plans whose file extension isn't lowercase, like
  `Pancakes.COOK`, now show up.
- Two recipes in the same folder with the same title no longer collapse into
  one row.
- Cook opens again on iPhones and iPads running iOS 16. It crashed at launch
  while the crash reporter catalogued the app's screens.
- Turning sync on while your recipes live in a custom or iCloud folder no
  longer freezes the app while they are copied over.
- Starting to cook no longer freezes the app while step photos and the aisle
  list are read from a slow folder. Each step's photo appears as you reach it.
- Signing in from the plans screen at the end of getting started brings you
  back to your summary instead of jumping straight to your recipes.
- Tapping "Start cooking" while the plans screen was still opening could stop
  every later plans screen from opening until you relaunched the app. The
  summary now waits for the plans screen to close first.
- The one-time plans offer is no longer used up when the plans could not be
  loaded.
- A recipe with ".cook" in the middle of its name, like `Dr.Cook's Chili.cook`,
  now shows its full name.
- A recipe whose name ends in `.menu` or `.cook` before the extension, like
  `Sunday.Menu.cook`, is found again from the shopping list.
- Opening a recipe that iCloud hasn't downloaded yet no longer freezes the app
  while the file is fetched.

#### 0.11.1 · 2026-10-02

**Added**

- Siri: move between cooking steps and finish cooking by voice.
- "What's new" in Settings → About opens this changelog.
- Hit the import limit without an account? You can now sign in for free
  to keep importing, and the import picks up where it stopped.

**Changed**

- The import gates (photo and social-link imports) use the same wording as the
  web converter.
- Signed-out users are asked to sign in at feature gates instead of being shown
  the purchase paywall.
- Sign-in and import prompts no longer suggest that an account alone
  brings sync, photo imports or meal plans: sync comes with Cook Basic, photo
  and social-link imports with a Cook Cloud plan.

**Fixed**

- Changes in a recipe folder are picked up reliably again.
- Turning on sync no longer freezes the app while it checks a large recipe
  folder.
- Importing a recipe after your cook.md session expired no longer fails with a
  message about image clipping: you're asked to sign in again, and the import
  carries on.
- Importing too quickly now tells you how many seconds to wait.
- Importing a social media link while signed out asks you to sign in,
  instead of stopping after the spinner with nothing on screen.

### [Cook for Android](https://github.com/cook-md/android-app/blob/HEAD/CHANGELOG.md)

#### 0.14.0 · 2026-10-15

**Added**

- Favourites: tap the heart on a recipe page, or use the ⋮ menu on a recipe row, and find
  your saved recipes in the new Favourites tab, optionally grouped by tag. They are kept in
  a `.bookmarks` file in your recipe folder, so the iOS app and the editor see the same list.
- Search: tap the search bar on Recipes or Favourites to find recipes by title, ingredient,
  tag or any word in them, or tap the microphone to search by voice. Before you type, it
  shows your recent searches and the recipes you opened last.
- Write a recipe on your phone with + → Create manually, and edit any recipe's text from the
  ⋮ menu on its page, with a preview before you save.
- The + menu on My recipes also offers Paste and convert, Scan from a photo and Import a file.
- Rename, move or delete a recipe from its ⋮ menu; its photos come along, and Undo brings it
  back.
- Press and hold a folder to move it, copy its link, or delete it.
- Adding a recipe that uses other recipes, like a dressing, to the shopping list asks which
  of them to buy for, so you can skip the ones you already have.
- Swipe a menu right to put the whole menu on the shopping list.
- Tap a linked recipe in the ingredients or steps to open it.
- A More details tab on the recipe page shows extra notes from your recipe file.

**Changed**

- The recipe page, My recipes and the menu page have a new look. Recipe pages show one
  ingredient list, larger photos and easier-to-read steps; recipe rows show time, servings
  and tags.
- Swiping a recipe now reveals a button: swipe right for Add to list, left for Delete (or
  Remove on Favourites).
- Pressing and holding a recipe opens the same menu as its ⋮ button.
- Add to list shows a short message with Undo instead of a pop-up.

**Fixed**

- Photos saved as HEIC, the iPhone's default, now show on recipes (Android 9 and newer).
- The shopping list counts the same ingredients as the iOS app for recipes that use other
  recipes, and finds them when their files end in capitals, like `Pancakes.COOK`.
- The tabs at the bottom of the screen stay in place inside a folder.
- If Add to list can't save the ingredients, the recipe page now says so.
- The welcome, paywall and getting-started screens reach the bottom of the screen with
  gesture navigation, without a pale strip above the home bar.

#### 0.13.0 · 2026-10-08

**Added**

- Getting started now asks about allergies, how much time you have on weeknights
  and what you want help with, so your first recipes fit better — and ends on a
  "Your cookbook is ready" page showing what was added for you.
- Clip a recipe from plain text: the clip screen has a new Text tab where you paste a
  recipe copied from a note, a message or an email, and the app turns it into a recipe
  you can cook from.

**Changed**

- Recipes in a folder are listed in file-name order. A recipe whose `title:` differs
  from its file name shows the title but sits where the file name sorts.
- In meal plans, notes are `-- note` lines, as in the Cook Editor and CookCLI; a `> note`
  line now shows as plain text.
- Meal plans are now free for everyone, signed in or not: every day of a plan is
  open, and you can add a whole plan to your shopping list without a plan or an
  account.

**Fixed**

- Adding a meal plan to the shopping list now buys what the plan says: a dish ordered
  by servings (`{4%servings}` of a recipe that serves two) is added twice, not four
  times, matching the portion shown on the plan.
- Opening your recipes, or a folder of them, is fast however many recipes you
  have: the app now reads only the folder on screen, and only the recipes you
  can see, instead of every recipe in the library. Rows show their file name
  first and fill in the title and photo as they come into view.
- Meal plans are read the same way as in the Cook Editor, CookCLI and the iPhone
  app: a dish ordered by servings (`{4%servings}`) shows how many times the
  recipe is cooked, meal times (`Dinner (19:00):`) are shown, and `-- notes`
  appear as notes.
- The "preparing your recipes" screen at the end of onboarding no longer closes
  after a second or two with the bar half full: it stays up long enough to read
  the cooking facts and fills the bar before your recipes open.
- Turning sync on when your sign-in has lapsed now asks you to sign in again
  instead of showing an error screen that came back every time you closed it.
- Your starter recipes are no longer lost to a slow connection: the download at
  the end of getting started now waits as long as a recipe import does, instead
  of giving up after ten quiet seconds and handing you the demo recipes.
- If the folder you picked for your recipes stops answering — its storage app
  was removed, or the folder itself was deleted — the app now notices on the
  first save and shows the "pick your folder again" banner, instead of failing
  the save with a generic error.

#### 0.12.2 · 2026-10-02

**Added**

- "What's new" in Settings → About opens this changelog.
- Hit the import limit without an account? You can now sign in for free
  to keep importing, and the import picks up where it stopped.
- Meal plans for today and tomorrow now appear at the top of My recipes, so
  tonight's dinner is one tap away.

**Changed**

- Onboarding and sign-in prompts no longer suggest that an account alone
  brings sync, photo imports or meal plans: sync comes with Cook Basic, photo
  and social-link imports with a Cook Cloud plan.

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.39.0 · 2026-10-24

**Added**

- a menu can use another menu as one of its meals ([#609](https://github.com/cooklang/cookcli/issues/609))
- **format:** show exact fractions the same way in every output ([#677](https://github.com/cooklang/cookcli/issues/677))
- **pantry:** list items as rows, like the aisle page ([#653](https://github.com/cooklang/cookcli/issues/653))
- **pantry:** new sections from Add item, rename sections, edit pantry.conf as text ([#629](https://github.com/cooklang/cookcli/issues/629))
- publish a JSON Feed at feed.json next to the Atom and RSS feeds ([#679](https://github.com/cooklang/cookcli/issues/679))
- **release:** version the binary archives and name them by platform ([#650](https://github.com/cooklang/cookcli/issues/650))
- **server:** --proxy-strips-prefix for proxies that remove --url-prefix ([#773](https://github.com/cooklang/cookcli/issues/773)), closes [#772](https://github.com/cooklang/cookcli/issues/772)
- **shopping-list:** --from / --to for some days of a menu ([#612](https://github.com/cooklang/cookcli/issues/612))
- **ui:** open sub-recipes and shopping list recipes at their scale ([#686](https://github.com/cooklang/cookcli/issues/686))
- **web:** ask before leaving a page with unsaved changes ([#674](https://github.com/cooklang/cookcli/issues/674)), closes [#519](https://github.com/cooklang/cookcli/issues/519)
- **web:** choose optional ingredients for the shopping list
- **web:** choose optional ingredients for the shopping list

**Fixed**

- **build:** advertise the web feeds on static pages built with --feed ([#676](https://github.com/cooklang/cookcli/issues/676)), closes [#595](https://github.com/cooklang/cookcli/issues/595)
- **ci:** build the Linux glibc binary in manylinux_2_28 ([#662](https://github.com/cooklang/cookcli/issues/662))
- **ci:** give each release target its own Rust cache ([#657](https://github.com/cooklang/cookcli/issues/657))
- **cli:** resolve config from -b for every command ([#734](https://github.com/cooklang/cookcli/issues/734))
- collapse runs of spaces in names typed for new files ([#768](https://github.com/cooklang/cookcli/issues/768))
- **completions:** exit cleanly when the output pipe closes
- **completions:** exit cleanly when the output pipe closes ([#708](https://github.com/cooklang/cookcli/issues/708))
- **core:** drop the spurious servings warning on &gt;&gt; metadata ([#713](https://github.com/cooklang/cookcli/issues/713)) ([#743](https://github.com/cooklang/cookcli/issues/743))
- **doctor:** warn once on a unit-less textual timer ([#745](https://github.com/cooklang/cookcli/issues/745))
- **editor:** close [- -] comments mid-line, highlight quantities ([#663](https://github.com/cooklang/cookcli/issues/663))
- **editor:** highlight nameless timers, mid-line comments and escapes like the parser ([#667](https://github.com/cooklang/cookcli/issues/667))
- **format:** don't split hyphenated words when wrapping cooklang ([#700](https://github.com/cooklang/cookcli/issues/700)) ([#735](https://github.com/cooklang/cookcli/issues/735))
- **format:** escape a literal backslash as \textbackslash{} in LaTeX ([#744](https://github.com/cooklang/cookcli/issues/744))
- **format:** escape for typst string literals, not markup ([#739](https://github.com/cooklang/cookcli/issues/739))
- **format:** escape user text in markdown output ([#746](https://github.com/cooklang/cookcli/issues/746))
- **format:** keep multiline metadata inside document comments ([#740](https://github.com/cooklang/cookcli/issues/740))
- **format:** re-emit the = scaling lock in cooklang source ([#737](https://github.com/cooklang/cookcli/issues/737))
- **format:** read schema.org durations through cooklang's parser ([#705](https://github.com/cooklang/cookcli/issues/705)) ([#741](https://github.com/cooklang/cookcli/issues/741))
- **format:** write exact quantities in cooklang source ([#701](https://github.com/cooklang/cookcli/issues/701)) ([#736](https://github.com/cooklang/cookcli/issues/736))
- **import:** escape the scraped title in YAML frontmatter ([#730](https://github.com/cooklang/cookcli/issues/730))
- **logout:** remove a corrupt session file instead of keeping it ([#716](https://github.com/cooklang/cookcli/issues/716)) ([#727](https://github.com/cooklang/cookcli/issues/727))
- **pantry:** quote the item name in load warnings, log them once on the server ([#776](https://github.com/cooklang/cookcli/issues/776))
- **pantry:** refuse add collisions with a different kind of entry ([#748](https://github.com/cooklang/cookcli/issues/748))
- **pantry:** refuse quantities and dates the file cannot read back ([#753](https://github.com/cooklang/cookcli/issues/753))
- **parser:** strip a UTF-8 BOM before parsing recipes ([#742](https://github.com/cooklang/cookcli/issues/742))
- point out aisle.conf lines written like a # or -- comment ([#688](https://github.com/cooklang/cookcli/issues/688)), closes [#687](https://github.com/cooklang/cookcli/issues/687)
- refuse scales and quantities that cannot round-trip ([#722](https://github.com/cooklang/cookcli/issues/722)) ([#755](https://github.com/cooklang/cookcli/issues/755))
- **seed:** fail on per-file write errors instead of exiting 0 ([#707](https://github.com/cooklang/cookcli/issues/707)) ([#725](https://github.com/cooklang/cookcli/issues/725))
- **seed:** report create_dir_all failure instead of panicking ([#706](https://github.com/cooklang/cookcli/issues/706)) ([#724](https://github.com/cooklang/cookcli/issues/724))
- **server:** hold recipe_image to the recipe-extension rule ([#750](https://github.com/cooklang/cookcli/issues/750))
- **server:** keep pantry edits inside /api/pantry ([#666](https://github.com/cooklang/cookcli/issues/666))
- **server:** keep recipe references inside the collection ([#749](https://github.com/cooklang/cookcli/issues/749))
- **server:** keep requests inside the collection once links resolve ([#751](https://github.com/cooklang/cookcli/issues/751))
- **server:** keep the server's paths out of what it sends ([#670](https://github.com/cooklang/cookcli/issues/670))
- **server:** say on the shopping list when the pantry file could not be used ([#691](https://github.com/cooklang/cookcli/issues/691))
- **server:** say why a change was refused after signing out ([#683](https://github.com/cooklang/cookcli/issues/683)), closes [#675](https://github.com/cooklang/cookcli/issues/675)
- **server:** serve only recipes and pictures from the recipe folder ([#668](https://github.com/cooklang/cookcli/issues/668)), closes [#658](https://github.com/cooklang/cookcli/issues/658)
- **shopping-list:** error clearly on a directory without recipes ([#723](https://github.com/cooklang/cookcli/issues/723)) ([#732](https://github.com/cooklang/cookcli/issues/732))
- **shopping-list:** list a reference that cannot be scaled instead of failing ([#684](https://github.com/cooklang/cookcli/issues/684))
- **shopping-list:** merge case variants into one item ([#694](https://github.com/cooklang/cookcli/issues/694)) ([#747](https://github.com/cooklang/cookcli/issues/747))
- **shopping-list:** refuse -o that would overwrite an input recipe ([#731](https://github.com/cooklang/cookcli/issues/731))
- **shopping-list:** refuse scaling a recipe that makes nothing ([#752](https://github.com/cooklang/cookcli/issues/752))
- **shopping-list:** scale a reference to half servings without rounding ([#681](https://github.com/cooklang/cookcli/issues/681)), closes [#680](https://github.com/cooklang/cookcli/issues/680)
- **update:** compare versions semantically, not as strings ([#729](https://github.com/cooklang/cookcli/issues/729))
- **update:** error cleanly on an unlisted arch or OS ([#720](https://github.com/cooklang/cookcli/issues/720)) ([#728](https://github.com/cooklang/cookcli/issues/728))

#### 0.38.1 · 2026-10-09

**Fixed**

- **server:** keep the ticks on aisle names when a recipe is removed ([#655](https://github.com/cooklang/cookcli/issues/655))
- **server:** name recipes relative to the collection in GET /api/recipes ([#639](https://github.com/cooklang/cookcli/issues/639)), closes [#638](https://github.com/cooklang/cookcli/issues/638)
- **server:** remove the shopping list entry that was clicked ([#646](https://github.com/cooklang/cookcli/issues/646)), closes [#645](https://github.com/cooklang/cookcli/issues/645)
- **server:** show the server's paths on Preferences to admins only ([#642](https://github.com/cooklang/cookcli/issues/642)), closes [#637](https://github.com/cooklang/cookcli/issues/637)
- **web:** keep the shopping list ticks when the aisle picker appears ([#648](https://github.com/cooklang/cookcli/issues/648)), closes [#647](https://github.com/cooklang/cookcli/issues/647)

#### 0.38.0 · 2026-10-07

**Added**

- **i18n:** add Italian translation
- **i18n:** add Italian translation
- **i18n:** add Japanese translation
- **i18n:** translate the step picture strings into Japanese
- **packaging:** build .deb packages for Debian and Ubuntu ([#577](https://github.com/cooklang/cookcli/issues/577))
- **pantry:** don't count missing optional ingredients
- **pantry:** don't count missing optional ingredients
- recognise optional ingredients and cookware (cooklang 0.19)
- recognise optional ingredients and cookware (cooklang 0.19)
- **server:** --recipes-only shows guests only the recipes ([#621](https://github.com/cooklang/cookcli/issues/621))
- **server:** opt-in sign-in before anything can be changed ([#534](https://github.com/cooklang/cookcli/issues/534))
- **server:** pages to manage aisles ([#631](https://github.com/cooklang/cookcli/issues/631))
- **server:** read --cors-origin from COOK_CORS_ORIGIN
- **server:** reader / shopper / editor / admin roles for signed-in users ([#563](https://github.com/cooklang/cookcli/issues/563))
- **server:** rename a recipe or menu from the editor ([#623](https://github.com/cooklang/cookcli/issues/623))
- **server:** upload step pictures from the web editor ([#584](https://github.com/cooklang/cookcli/issues/584)), closes [#562](https://github.com/cooklang/cookcli/issues/562)
- **shopping-list:** leave optional ingredients out unless --include-optional
- **shopping-list:** leave optional ingredients out unless --include-optional
- **ui:** change a meal plan from its calendar ([#610](https://github.com/cooklang/cookcli/issues/610))
- **ui:** Cooklang toolbar above the recipe editor ([#540](https://github.com/cooklang/cookcli/issues/540))
- **ui:** create and edit menus with a recipe picker ([#558](https://github.com/cooklang/cookcli/issues/558))
- **ui:** meal plans laid out as a calendar ([#596](https://github.com/cooklang/cookcli/issues/596))
- **ui:** open a menu's recipes at the scale the menu asks for ([#561](https://github.com/cooklang/cookcli/issues/561))
- **ui:** random recipe button scoped to the current folder ([#554](https://github.com/cooklang/cookcli/issues/554)), closes [#544](https://github.com/cooklang/cookcli/issues/544)
- **ui:** scale a recipe by servings when it declares them ([#565](https://github.com/cooklang/cookcli/issues/565))
- **web:** shrink title pictures in the browser, always re-encode on the server

**Fixed**

- **build:** leave the output dir out of the listing pages ([#634](https://github.com/cooklang/cookcli/issues/634)), closes [#632](https://github.com/cooklang/cookcli/issues/632)
- **ci:** stop CI and releases from failing silently ([#569](https://github.com/cooklang/cookcli/issues/569))
- **deps:** bump rustls to 0.23.45 (GHSA-2mjx-qc3c-rqvc) ([#641](https://github.com/cooklang/cookcli/issues/641)), closes [#640](https://github.com/cooklang/cookcli/issues/640)
- **i18n:** drop the error page strings defined twice ([#579](https://github.com/cooklang/cookcli/issues/579))
- **i18n:** translate the messages that only existed in English ([#567](https://github.com/cooklang/cookcli/issues/567))
- **pantry:** don't wrap "optional" in a second pair of parentheses ([#627](https://github.com/cooklang/cookcli/issues/627)), closes [#626](https://github.com/cooklang/cookcli/issues/626)
- report non-numeric timer values in doctor ([#614](https://github.com/cooklang/cookcli/issues/614))
- **server:** keep search and menu on one line on mobile
- **server:** limit the recipe file endpoints to .cook and .menu files ([#550](https://github.com/cooklang/cookcli/issues/550)), closes [#545](https://github.com/cooklang/cookcli/issues/545)
- **server:** name shopping list entries by their recipe title ([#625](https://github.com/cooklang/cookcli/issues/625))
- **server:** never delete a folder when refusing a new recipe path ([#582](https://github.com/cooklang/cookcli/issues/582)), closes [#549](https://github.com/cooklang/cookcli/issues/549)
- **server:** refuse cross-site WebSocket connections to the language server ([#524](https://github.com/cooklang/cookcli/issues/524))
- **server:** same-origin by default, and refuse unknown Host names ([#583](https://github.com/cooklang/cookcli/issues/583)), closes [#546](https://github.com/cooklang/cookcli/issues/546)
- **server:** trust only localhost and IP addresses as the server's own origin
- stop listing macOS ._ files as recipes ([#557](https://github.com/cooklang/cookcli/issues/557)), closes [#555](https://github.com/cooklang/cookcli/issues/555)
- trim spaces around names typed for new files, pantry items and checks ([#616](https://github.com/cooklang/cookcli/issues/616))
- **ui:** make Done the main action once a title picture is set ([#588](https://github.com/cooklang/cookcli/issues/588)), closes [#587](https://github.com/cooklang/cookcli/issues/587)
- **web:** stop step picture paths escaping cooking mode's img src
- **web:** stop step picture paths escaping cooking mode's img src, closes [#548](https://github.com/cooklang/cookcli/issues/548)

### [Cook Editor](https://github.com/cook-md/editor/blob/HEAD/CHANGELOG.md)

#### 0.1.0-alpha.57 · 2026-10-17

**Changed**

- **native:** prefetch nutrition categories in one batch before report renders ([#238](https://github.com/cook-md/editor/issues/238))

**Fixed**

- **preview:** reserve badge space with loading pills; keep header actions steady ([#237](https://github.com/cook-md/editor/issues/237))

#### 0.1.0-alpha.56 · 2026-10-15

**Fixed**

- **chat:** caret in chat input, tab/file drops attach context, CookBot sees active tab and attachments ([#232](https://github.com/cook-md/editor/issues/232))

#### 0.1.0-alpha.55 · 2026-10-15

**Added**

- **ai:** write AI file edits directly with undo from the chat ([#231](https://github.com/cook-md/editor/issues/231))

**Fixed**

- **account:** Manage subscription carries from=editor_account
- editor crashes reported in Sentry ([#225](https://github.com/cook-md/editor/issues/225))

#### 0.1.0-alpha.54 · 2026-10-11

**Fixed**

- **reports:** menu renders expand staged recipes; renderTemplate documents plan context ([#215](https://github.com/cook-md/editor/issues/215))

#### 0.1.0-alpha.53 · 2026-10-11

**Added**

- **plugin-api:** exportPdf and recipeImages for the Cookbook plugin ([#213](https://github.com/cook-md/editor/issues/213))

#### 0.1.0-alpha.52 · 2026-10-09

**Added**

- **cooklang:** Favourites plugin, cooklangPreviewPath context key and bundled cooklang.favourites ([#208](https://github.com/cook-md/editor/issues/208))
- **cooklang:** menu preview badges and cooklang.api.openReport for the Core Vitals plugin ([#204](https://github.com/cook-md/editor/issues/204))

**Fixed**

- **cooklang:** menus always use the cooklang language; report tabs stop persisting the nutrition token ([#206](https://github.com/cook-md/editor/issues/206))
- remove claude
- Sentry issues seen on alpha.42–alpha.50 ([#211](https://github.com/cook-md/editor/issues/211))

#### 0.1.0-alpha.51 · 2026-10-06

**Added**

- **welcome:** replace CookBot checklist step with a dismissible trial banner ([#180](https://github.com/cook-md/editor/issues/180))

**Fixed**

- **build:** set Linux executableName so electron-builder 26.15 can build the AppImage ([#185](https://github.com/cook-md/editor/issues/185))
- **native:** link the MSVC CRT statically on Windows ([#186](https://github.com/cook-md/editor/issues/186))
- **plugin-ext:** asRelativePath returned '.' for every file on Windows ([#192](https://github.com/cook-md/editor/issues/192))

## September 2026

### [Cook for iOS](https://github.com/cook-md/ios-app/blob/HEAD/CHANGELOG.md)

#### 0.11.0 · 2026-09-23

**Added**

- Quick Look preview for `.cook` files.
- One `cook://` URL scheme: `https://cook.md` recipe links open in the app, and
  `.cook` files open from anywhere (Files, Mail, Messages).
- The onboarding paywall is shown once, on a later day, instead of right after
  the recipe pack.

**Fixed**

- Freezes while recipes were being read, and a crash when swiping between
  recipes.
- The shopping list follows recipe references all the way down.

#### 0.10.4 · 2026-09-17

**Fixed**

- The directory watcher no longer overflows the stack on large libraries.
- A launch crash on iOS 16 caused by Sentry's network swizzling.
- The sync banner's editor links stay on one line.
- The recipe title sits in the same place with and without an image, and the
  recipe page scrolls from anywhere in the header.

#### 0.10.3 · 2026-09-14

**Fixed**

- A folder's recipe count includes the recipes in its subfolders.

#### 0.10.2 · 2026-09-07

**Added**

- Cook Cloud paywalls: Cook Pro purchasable in the app, "On this device" and
  "On desktop" cards, two import meters; descriptive bullets with the rationale
  on top.
- Meal plans: display menus and list upcoming meals.
- Shopping list update.
- Persistent log collection with an export in Settings.

**Fixed**

- A sync 402 goes to the paywall, not to sign-out.
- Kickstart install failures are shown instead of an empty recipe list.
- Subscription state refreshes when Settings opens, and the cached snapshot
  stays on screen while the refresh is in flight.
- A plan upgrade is re-linked instead of being skipped as a renewal, and the
  receipt-minted session is linked rather than trusted.

### [Cook for Android](https://github.com/cook-md/android-app/blob/HEAD/CHANGELOG.md)

#### 0.12.1 · 2026-09-30

**Added**

- Signed-out users now see a "Sign in / See plans" prompt at feature gates
  (photo and social-link imports, meal plans, the paywall) instead of a paywall
  they cannot buy from, matching iOS.

**Fixed**

- Shopping list: removing a recipe no longer fails when another recipe on the
  list has been deleted, and deleted recipes no longer appear on the aisle tab.
- Sharing: protocol-relative image URLs now resolve, and images missing from
  disk are skipped instead of breaking the share.
- Timers: the background timer service now stops reliably.
- Clipping: cancelling the sign-in alert closes the import instead of leaving an
  empty screen, and a signed-out link import asks about social imports rather
  than photo imports.
- A device without a cook.md account counts as signed out even when an anonymous
  purchase session exists.
- Sign-in alert buttons use the accent label colour.

#### 0.12.0 · 2026-09-29

**Added**

- Menus (meal plans): a menu screen opened from the recipe browser or a
  `cook://` link, with day cards, scaling, and "add the whole menu to the
  shopping list".
- Menu files opened from other apps are previewed and saved to Plans.
- The Basic plan card in the paywall now lists meal plans.
- Shopping list redesign: the recipe tab shows linked recipes and menu dishes as
  badged sub-sections; restyled aisle tab, tabs, empty state, clear dialog and
  options sheet.

**Fixed**

- Shopping list: linked recipes that cannot be found are skipped with a warning
  instead of dropping the entry; repeated linked recipes are grouped as on iOS;
  amounts are right-aligned; long scale factors fit at large font sizes.
- Importing: only the file's actual extension is dropped, file names are trimmed
  before detecting menus, and draft and menu titles are sanitised before
  numbering.
- Local folders: saving a copy never overwrites an existing file, and the mirror
  writes over a name the folder picker already claimed.
- Menus: deep links open in the menu screen, recipe references stay inside the
  recipe root, double taps are ignored while a preview save runs, and the scale
  button and controls are labelled for TalkBack.

#### 0.11.0 · 2026-09-23

**Added**

- Open `.cook` files from anywhere (file managers, mail, messaging apps) into
  the shared-recipe preview.
- Deep links: `cook://my/<path>` and `https://cook.md/my/<path>` open the recipe
  or folder; long-press a recipe or folder to copy its link.
- The onboarding paywall is offered on a later day's launch instead of right
  away.

**Fixed**

- Shopping list warns about recipe reference cycles, and unportioned
  sub-recipes scale correctly.
- Import review: fixed misleading details and blank refusal screens.
- Cook is offered for `.cook` files whose URI carries no file name.

#### 0.10.2 · 2026-09-16

**Added**

- Cook Cloud paywalls: new copy, Cook Pro purchasable in the app, import
  meters and account states; a plan badge that says where the plan is managed;
  "Manage subscription" for buyers who never signed in; a warning when an
  account merge left two subscriptions billed.

**Fixed**

- The real sync error is shown, and sync starts right after buying a plan.
- Transient Play Billing failures are retried instead of reported.
- Lost access to a custom recipe folder is recovered.
- Just-saved recipes are kept, and the first folder sync is faster.
- The expired-session flag is cleared when the user signs back in.

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.37.0 · 2026-09-24

**Added**

- **build:** generate Atom and RSS feeds with --feed, closes [#503](https://github.com/cooklang/cookcli/issues/503)
- **build:** let --feed reuse the --sitemap URL
- **cooking-mode:** add interactive countdown timers
- **server:** render URL metadata values as clickable links
- **server:** render URL metadata values as clickable links
- **server:** serve Atom and RSS feeds at /atom.xml and /rss.xml

**Fixed**

- **core:** honour COOK_CONFIG_DIR so tests cannot reach a real session
- **core:** honour COOK_CONFIG_DIR so tests cannot reach a real session
- **docker:** embed the lsp feature so the web editor works
- **docker:** embed the lsp feature so the web editor works
- **server:** cap concurrent LSP sessions
- **server:** cap concurrent LSP sessions
- **server:** don't announce reads of the shopping list as changes
- **server:** keep /recipe and /directory inside the recipe directory
- **server:** keep request-supplied paths inside the recipe directory
- **server:** keep the shopping list inside the recipe directory
- **server:** tell a lagging SSE subscriber the whole list changed
- **web:** leave re-reading the ticks to the tick's own announcement
- **web:** make the editor diagnostic popup readable in dark mode
- **web:** make the editor diagnostic popup readable in dark mode
- **web:** only re-render the shopping list where it changed

#### 0.36.0 · 2026-09-18

**Added**

- **cli:** add `cook completions <shell>` for shell completion scripts
- **cli:** add `cook completions <shell>` for shell completion scripts, closes [#467](https://github.com/cooklang/cookcli/issues/467)
- **doctor:** show which recipes use each reported ingredient
- **doctor:** show which recipes use each reported ingredient, closes [#485](https://github.com/cooklang/cookcli/issues/485)
- **packaging:** add Fedora RPM packaging
- **server:** add --cors-origin and --cors-allow-credentials, closes [#465](https://github.com/cooklang/cookcli/issues/465)
- **server:** build the CORS layer from the validated config
- **server:** make CORS configuration configurable
- **server:** refuse cross-origin writes under the wildcard default
- **server:** validate CORS origin and credential flags
- **ui:** add token layer and component vocabulary
- **ui:** token foundation and Cooklang palette, existing layout kept

**Fixed**

- **build:** emit search index as a script so file:// search works
- **build:** emit search index as a script so file:// search works, closes [#471](https://github.com/cooklang/cookcli/issues/471)
- **build:** harden search index load and scope the file:// claim
- **build:** ship only compiled stylesheets and scripts in the static site, closes [#493](https://github.com/cooklang/cookcli/issues/493)
- **build:** wire resolved --lang to &lt;html lang&gt; attribute, closes [#470](https://github.com/cooklang/cookcli/issues/470)
- **doctor:** compare reported recipe paths without assuming a separator
- **editor:** do not show Saved before any save, closes [#491](https://github.com/cooklang/cookcli/issues/491)
- **editor:** syntax colours from tokens instead of hex, closes [#490](https://github.com/cooklang/cookcli/issues/490)
- **format:** stop hard wrapping markdown output
- **format:** stop hard wrapping markdown output, closes [#497](https://github.com/cooklang/cookcli/issues/497)
- **i18n:** translate icon-button labels, closes [#488](https://github.com/cooklang/cookcli/issues/488)
- **packaging:** attach the built RPMs to the release
- **packaging:** give the build root the toolchain the spec asks for
- **packaging:** keep the packaged binary stripped
- **packaging:** make the RPM workflow build again
- **search:** decode recipe files lossily instead of failing on invalid UTF-8
- **search:** decode recipe files lossily instead of failing on invalid UTF-8
- **search:** pick up cooklang-find 0.7.1 for invalid UTF-8 in front matter, closes [#498](https://github.com/cooklang/cookcli/issues/498)
- **server:** accept bracketed IPv6 CORS origins
- **server:** read the write guard's host from the Host header only
- **server:** reject CORS origins that could never match
- **server:** reject CORS origins with an empty host
- **server:** report `tags` as an array whatever the frontmatter spelled
- **server:** report `tags` as an array whatever the frontmatter spelled
- **server:** stop deriving the new-recipe host from a forgeable header
- **server:** take the API docs host from Host, not X-Forwarded-Host
- **server:** take the API docs host from Host, not X-Forwarded-Host
- **shopping-list:** cap reference depth, and cover the yield branch
- **shopping-list:** follow recipe references all the way down
- **shopping-list:** follow recipe references all the way down, closes [#509](https://github.com/cooklang/cookcli/issues/509)
- **ui:** build the scale URL safely and guard bad scale values
- **ui:** keep icon-only actions below lg, tidy print rules and docs
- **ui:** keep overflow menu highlight and brand mark legible
- **ui:** pantry stock colour, compact inline buttons, smaller row icons
- **ui:** recipes index review fixes
- **ui:** safe scale navigation on menus, aria-pressed on preference toggles
- **ui:** show the new-recipe error border, ring its input, compact API chips
- **ui:** tighten token foundation after review
- **ui:** white text on filled buttons via a darker accent fill
- **web:** align the pantry page with the header width
- **web:** close the UI follow-ups from [#456](https://github.com/cooklang/cookcli/issues/456)
- **web:** escape recipe names in server-mode search results, closes [#487](https://github.com/cooklang/cookcli/issues/487)
- **web:** keep the served order on the default sort, closes [#486](https://github.com/cooklang/cookcli/issues/486)
- **web:** no skipped heading levels on API docs and sectioned recipes, closes [#492](https://github.com/cooklang/cookcli/issues/492)
- **web:** show the shopping list empty state after clearing, closes [#489](https://github.com/cooklang/cookcli/issues/489)
- **web:** sort the recipes index naturally on the server, closes [#486](https://github.com/cooklang/cookcli/issues/486)

### [Cook Editor](https://github.com/cook-md/editor/blob/HEAD/CHANGELOG.md)

#### 0.1.0-alpha.50 · 2026-09-30

**Added**

- first run — welcome checklist, CookBot trial gate, usage events ([#159](https://github.com/cook-md/editor/issues/159))

**Fixed**

- **cookbot:** friendly session-expired message; dev builds use the local CookBot ([#161](https://github.com/cook-md/editor/issues/161))
- Sentry issues seen on alpha.43–alpha.47 ([#162](https://github.com/cook-md/editor/issues/162))

#### 0.1.0-alpha.49 · 2026-09-27

**Added**

- **app:** recommend first-party plugins in the Extensions view ([#156](https://github.com/cook-md/editor/issues/156))

**Fixed**

- **cooklang-native:** cooklang-reports-nutrition 0.1.3 (½ cup and fraction ranges read correctly) ([#158](https://github.com/cook-md/editor/issues/158))

#### 0.1.0-alpha.48 · 2026-09-27

**Added**

- **cooklang:** cooklang.api.refreshBadges ([#155](https://github.com/cook-md/editor/issues/155))
- **cooklang:** pantry editing API for plugins ([#152](https://github.com/cook-md/editor/issues/152))
- **cooklang:** plugin badges and report rendering API (Nutri-Score) ([#154](https://github.com/cook-md/editor/issues/154))

#### 0.1.0-alpha.47 · 2026-09-25

**Added**

- **cooklang:** editor API for the Recipe Hub plugin ([#149](https://github.com/cook-md/editor/issues/149))
- **cooklang:** plugin outlets, Cooklang plugin API, shopping list as a default plugin ([#148](https://github.com/cook-md/editor/issues/148))
- ship the recipe-hub plugin by default; shopping-list 0.1.2 ([#150](https://github.com/cook-md/editor/issues/150))

**Fixed**

- **shopping-list:** expand recipe references at every depth ([#145](https://github.com/cook-md/editor/issues/145))

#### 0.1.0-alpha.46 · 2026-09-24

**Added**

- **cookbot:** renderTemplate renders staged files; searchRecipes digest gains steps, cookware, menu recipes/dates, kind ([#144](https://github.com/cook-md/editor/issues/144))
- **deeplink:** handle cook:// links, unify the .cook UTI, offer Save to Drafts ([#139](https://github.com/cook-md/editor/issues/139))

**Changed**

- **cookbot:** shrink searchRecipes results — drop name, omit empty fields ([#125](https://github.com/cook-md/editor/issues/125)) ([#142](https://github.com/cook-md/editor/issues/142))

**Fixed**

- **cookbot:** live COOK.md, honest truncation, turns that always end, keep the question across folder open ([#141](https://github.com/cook-md/editor/issues/141))
- **preview:** show the recipe's title: metadata instead of the filename ([#131](https://github.com/cook-md/editor/issues/131)) ([#143](https://github.com/cook-md/editor/issues/143))

#### 0.1.0-alpha.45 · 2026-09-20

**Added**

- **cooklang-ai,cooklang:** bulk recipe metadata tools so CookBot stops reading files to tag them ([#134](https://github.com/cook-md/editor/issues/134))

#### 0.1.0-alpha.44 · 2026-09-16

**Added**

- **cooklang:** open recipes the way a recipe editor should ([#126](https://github.com/cook-md/editor/issues/126))
- **cooklang:** recognize Obsidian-style .md recipes with recipe: true ([#129](https://github.com/cook-md/editor/issues/129))

**Fixed**

- six Sentry issues still firing on alpha.43 ([#130](https://github.com/cook-md/editor/issues/130))

#### 0.1.0-alpha.43 · 2026-09-03

**Added**

- clickable URLs and working timers in the recipe preview ([#115](https://github.com/cook-md/editor/issues/115))
- **cooklang,cooklang-ai:** batch arguments for the read tools ([#124](https://github.com/cook-md/editor/issues/124))

**Fixed**

- six Sentry issues from alpha.38-.42 ([#118](https://github.com/cook-md/editor/issues/118))

## August 2026

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.35.0 · 2026-08-30

**Added**

- add the --no-cors argument to bypass cors verification
- add the --no-cors argument to bypass cors verification

**Fixed**

- formating

#### 0.34.0 · 2026-08-23

**Added**

- **core:** extract command logic into a cookcli-core library crate
- **core:** let a shopping list be built from in-memory recipe text
- **format:** publish the recipe converters as cooklang-format
- **release:** publish a source tarball with the compiled assets ([#454](https://github.com/cooklang/cookcli/issues/454))
- **search:** require every term to match, closes [#425](https://github.com/cooklang/cookcli/issues/425)
- **shopping-list:** add --extra for items no recipe calls for ([#457](https://github.com/cooklang/cookcli/issues/457)), closes [#175](https://github.com/cooklang/cookcli/issues/175)

**Fixed**

- build recipe reference paths with '/' on every platform, closes [#442](https://github.com/cooklang/cookcli/issues/442)
- **ci:** skip the Claude review when its token is unavailable ([#455](https://github.com/cooklang/cookcli/issues/455))
- **ci:** tolerate CRLF checkouts in the api docs freshness test ([#439](https://github.com/cooklang/cookcli/issues/439))
- clear the help-wanted backlog
- disable bundled_units so quantities keep their authored units ([#433](https://github.com/cooklang/cookcli/issues/433))
- **doctor:** attribute a broken reference to the recipe that wrote it, closes [#437](https://github.com/cooklang/cookcli/issues/437)
- **pantry:** edit pantry.conf in place instead of rewriting it, closes [#429](https://github.com/cooklang/cookcli/issues/429)
- **recipe:** keep the cooklang formatter idempotent, closes [#414](https://github.com/cooklang/cookcli/issues/414)
- **recipe:** order cookware amounts deterministically too
- **report:** resolve the recipe argument like every other command, closes [#430](https://github.com/cooklang/cookcli/issues/430)
- **server:** order shopping list quantity components deterministically, closes [#441](https://github.com/cooklang/cookcli/issues/441)
- **server:** saturate the pantry expiring threshold instead of panicking, closes [#428](https://github.com/cooklang/cookcli/issues/428)
- **shopping-list:** honour --plain in the YAML writer, closes [#419](https://github.com/cooklang/cookcli/issues/419)
- **shopping-list:** order quantity components deterministically
- **shopping-list:** stop expanding a reference that leads back on itself, closes [#424](https://github.com/cooklang/cookcli/issues/424)

#### 0.33.1 · 2026-08-12

**Fixed**

- **ci:** build Linux glibc binary against an older glibc ([#426](https://github.com/cooklang/cookcli/issues/426)), closes [#420](https://github.com/cooklang/cookcli/issues/420)
- **docker:** add server feature for docker image ([#422](https://github.com/cooklang/cookcli/issues/422))

#### 0.33.0 · 2026-08-10

**Added**

- **build:** add --compress flag to write gzip copies of generated assets ([#389](https://github.com/cooklang/cookcli/issues/389)), closes [#345](https://github.com/cooklang/cookcli/issues/345)
- **build:** add --repo-url flag to link the source repo from the site footer ([#383](https://github.com/cooklang/cookcli/issues/383)), closes [#376](https://github.com/cooklang/cookcli/issues/376)
- **build:** default site language to the system locale and document --lang ([#387](https://github.com/cooklang/cookcli/issues/387))
- **i18n:** allow pluralization ([#377](https://github.com/cooklang/cookcli/issues/377))
- put server, import and lsp behind cargo features ([#369](https://github.com/cooklang/cookcli/issues/369)), closes [#366](https://github.com/cooklang/cookcli/issues/366)
- **recipe:** add --paper-size and --margin flags for LaTeX/Typst output ([#382](https://github.com/cooklang/cookcli/issues/382)), closes [#379](https://github.com/cooklang/cookcli/issues/379)
- **server:** add a button to copy the shopping list as plain text ([#411](https://github.com/cooklang/cookcli/issues/411)), closes [#380](https://github.com/cooklang/cookcli/issues/380)
- **server:** add API documentation page at /api-docs ([#412](https://github.com/cooklang/cookcli/issues/412))
- **server:** add copy options to the shopping list copy button ([#413](https://github.com/cooklang/cookcli/issues/413))
- **server:** respect prefers-color-scheme for selecting theme ([#364](https://github.com/cooklang/cookcli/issues/364))

**Fixed**

- **deps:** declare cooklang's bundled_units feature explicitly ([#371](https://github.com/cooklang/cookcli/issues/371)), closes [#366](https://github.com/cooklang/cookcli/issues/366)
- fail the build with instructions when compiled front-end assets are missing ([#404](https://github.com/cooklang/cookcli/issues/404)), closes [#233](https://github.com/cooklang/cookcli/issues/233)
- **i18n:** remove hardcoded english meta titles ([#378](https://github.com/cooklang/cookcli/issues/378))
- satisfy clippy::useless_borrows_in_formatting ([#370](https://github.com/cooklang/cookcli/issues/370))
- **server:** resolve section-style step image names (Recipe.S.N.ext) ([#388](https://github.com/cooklang/cookcli/issues/388)), closes [#374](https://github.com/cooklang/cookcli/issues/374)
- **server:** wrap long ingredient notes instead of clipping them ([#386](https://github.com/cooklang/cookcli/issues/386))

### [Cook Editor](https://github.com/cook-md/editor/blob/HEAD/CHANGELOG.md)

#### 0.1.0-alpha.42 · 2026-08-30

**Added**

- **sync:** restart sync task on session-token renewal
- **sync:** restart sync task on session-token renewal

#### 0.1.0-alpha.41 · 2026-08-29

**Added**

- recipe images in the recipe preview ([#110](https://github.com/cook-md/editor/issues/110))

#### 0.1.0-alpha.40 · 2026-08-28

**Added**

- **sync:** gate CookCloud sync on the plan entitlement — locked and needs-plan states with in-app upgrade

#### 0.1.0-alpha.39 · 2026-08-20

**Fixed**

- harden startup and keybinding paths against errors seen in alpha.38 ([#104](https://github.com/cook-md/editor/issues/104))

#### 0.1.0-alpha.38 · 2026-08-18

**Added**

- **chat:** warn before the AI quota runs out instead of stopping dead at 100% ([#101](https://github.com/cook-md/editor/issues/101))
- **cooklang:** renderTemplate templateUri + listReportTemplates tool ([#102](https://github.com/cook-md/editor/issues/102))
- Sentry error reporting across all three processes ([#90](https://github.com/cook-md/editor/issues/90))
- **telemetry:** add commands to send a test error to Sentry ([#92](https://github.com/cook-md/editor/issues/92))

**Fixed**

- do not tell developers to run nvm when the repo has no nvm ([#100](https://github.com/cook-md/editor/issues/100))

#### 0.1.0-alpha.37 · 2026-08-11

**Fixed**

- make `npm run test` runnable and enforce it in CI ([#85](https://github.com/cook-md/editor/issues/85)), closes [#84](https://github.com/cook-md/editor/issues/84)
- report Cookbot quota errors accurately instead of "busy, try again" ([#86](https://github.com/cook-md/editor/issues/86))

#### 0.1.0-alpha.36 · 2026-08-10

**Fixed**

- re-initialize and retry Cookbot request on expired session ([#78](https://github.com/cook-md/editor/issues/78))
- surface Cookbot chat errors and auto-retry dropped connections ([#83](https://github.com/cook-md/editor/issues/83)), closes [#80](https://github.com/cook-md/editor/issues/80) [#81](https://github.com/cook-md/editor/issues/81)

## July 2026

### [Cook Editor](https://github.com/cook-md/editor/blob/HEAD/CHANGELOG.md)

#### 0.1.0-alpha.35 · 2026-07-27

**Added**

- recipe import (URL, text, images, clipping browser) ([#74](https://github.com/cook-md/editor/issues/74))

#### 0.1.0-alpha.34 · 2026-07-19

**Added**

- nutrition deps from crates.io (public cooklang-reports-nutrition) ([#72](https://github.com/cook-md/editor/issues/72))

#### 0.1.0-alpha.33 · 2026-07-15

**Added**

- **nutrition:** allergen support — bump nutrition crates to db 8af0735 ([#70](https://github.com/cook-md/editor/issues/70))

#### 0.1.0-alpha.32 · 2026-07-13

**Added**

- **reports:** expose expanded plan context when rendering .menu reports ([#68](https://github.com/cook-md/editor/issues/68))

#### 0.1.0-alpha.31 · 2026-07-04

**Fixed**

- **electron:** actually ship + resolve bundled plugins in the release ([#66](https://github.com/cook-md/editor/issues/66))

#### 0.1.0-alpha.30 · 2026-07-04

**Fixed**

- **electron:** load bundled VS Code plugins in packaged app ([#64](https://github.com/cook-md/editor/issues/64))

#### 0.1.0-alpha.29 · 2026-07-02

**Fixed**

- **electron:** point bundled rgPath at app.asar.unpacked ([#62](https://github.com/cook-md/editor/issues/62))

#### 0.1.0-alpha.28 · 2026-07-02

**Fixed**

- **electron:** unpack native executables from asar ([#60](https://github.com/cook-md/editor/issues/60))

#### 0.1.0-alpha.27 · 2026-07-01

**Fixed**

- **macos:** vendor cooklang-rs xcframework via curl to dodge flaky CI download ([#58](https://github.com/cook-md/editor/issues/58))

#### 0.1.0-alpha.26 · 2026-07-01

**Fixed**

- **macos:** stop Quick Look build hanging on SwiftPM artifact download ([#56](https://github.com/cook-md/editor/issues/56))

## June 2026

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.32.0 · 2026-06-12

**Added**

- add recipe sorting by name, modified date, and created date ([#356](https://github.com/cooklang/cookcli/issues/356))
- make shopping list and pantry nav links configurable via settings ([#357](https://github.com/cooklang/cookcli/issues/357))

#### 0.31.0 · 2026-06-09

**Added**

- **build:** generate sitemap.xml with `cook build web --sitemap` ([#351](https://github.com/cooklang/cookcli/issues/351))

**Fixed**

- **server:** avoid renameat2 SIGSYS on aarch64 Android (Termux) ([#353](https://github.com/cooklang/cookcli/issues/353)), closes [#349](https://github.com/cooklang/cookcli/issues/349)

### [Cook Editor](https://github.com/cook-md/editor/blob/HEAD/CHANGELOG.md)

#### 0.1.0-alpha.25 · 2026-06-30

**Added**

- **cooklang-native:** register nutrition extension when feature + url present
- **cooklang:** add cooklang.nutrition.serviceUrl preference
- **cooklang:** add electron-main report export service
- **cooklang:** add report export RPC protocol
- **cooklang:** add report print/export commands and toolbar
- **cooklang:** add standalone report export document builder
- **cooklang:** bind report export service proxy
- **cooklang:** expose export document from report widget
- **cooklang:** inject nutrition service URL + cook.md token into report config
- **cooklang:** register report export contribution
- **cooklang:** register report export RPC handler
- **cooklang:** render mermaid diagrams in jinja reports ([#55](https://github.com/cook-md/editor/issues/55))
- nutrition reports for Cook Pro users
- **reports:** bundle jinjahtml for jinja report-template syntax highlighting
- **reports:** print, export PDF, and export PNG for rendered reports
- **report:** typographic treatment + page margins for rendered reports

**Fixed**

- **cooklang:** harden report export per review
- **cooklang:** match recipe/menu file extensions case-insensitively ([#50](https://github.com/cook-md/editor/issues/50)) ([#51](https://github.com/cook-md/editor/issues/51))
- **cooklang:** render printer toolbar icon via themed SVG mask
- **cooklang:** treat print dialog cancel as quiet success
- **cooklang:** use distinct nls keys for export toolbar tooltips
- **cooklang:** use valid codicon-print for print toolbar icon

#### 0.1.0-alpha.24 · 2026-06-14

**Added**

- AI-authored template rendering (renderTemplate tool) ([#46](https://github.com/cook-md/editor/issues/46))

**Fixed**

- **ai-chat-ui:** add trailing space after inserted #file mention ([#48](https://github.com/cook-md/editor/issues/48))

#### 0.1.0-alpha.23 · 2026-06-11

**Added**

- **cooklang-native:** add renderReport via cooklang-reports crate
- **cooklang:** add built-in report templates and template-file helpers
- **cooklang:** add Render Report command with template QuickPick
- **cooklang:** add renderReport RPC to CooklangLanguageService
- **cooklang:** add ReportWidget rendering report output as markdown
- **cooklang:** discover report templates in reports/ and templates/ dirs
- **cooklang:** make preview/report widgets focusable, fix stale-parse races, live template re-render
- **cooklang:** Render Report command — Jinja2 reports for recipes
- **cooklang:** render report output as markdown, HTML, or text by template extension
- **cooklang:** render reports for .menu files
- **cooklang:** search whole workspace for report templates via ripgrep
- **cooklang:** wire up report widget factory and contribution

**Fixed**

- **cooklang-native:** surface detailed template errors
- **cooklang:** enable Render Report from preview widgets, not only text editors
- **cooklang:** guard ReportWidget against stale and post-dispose renders
- **cooklang:** resolve report target from current main-area tab
- **cooklang:** reuse report widget by widget id, not factory cache

#### 0.1.0-alpha.22 · 2026-06-10

**Added**

- **branding:** default VSX registry to plugins.cook.md
- **branding:** default VSX registry to plugins.cook.md

#### 0.1.0-alpha.21 · 2026-06-09

**Added**

- **macos:** editor-style Quick Look preview (two-column, pills, badges, menu cards)

**Fixed**

- **macos:** sandbox the Quick Look appex so PluginKit registers it

#### 0.1.0-alpha.20 · 2026-06-09

**Fixed**

- **macos:** add required bundle keys to appex Info.plist so PluginKit registers it

#### 0.1.0-alpha.19 · 2026-06-09

**Fixed**

- **macos:** suppress get-task-allow on the Quick Look appex (notarization)

#### 0.1.0-alpha.18 · 2026-06-09

**Fixed**

- **macos:** pre-sign the Quick Look appex in CI so electron-builder can seal the app

#### 0.1.0-alpha.17 · 2026-06-09

**Fixed**

- **macos:** embed Quick Look appex before the resources/app cleanup guard

#### 0.1.0-alpha.16 · 2026-06-09

**Added**

- **cooklang-ai:** add includeHidden parameter to directory structure tool
- **cooklang-ai:** indented-tree directory structure output, hide dotfiles
- **linux:** enable GNOME spacebar text preview for .cook/.menu via MIME subclass
- **macos:** SwiftUI recipe preview view for Quick Look
- **macos:** declare .cook/.menu UTIs for Quick Look + file association
- **macos:** map CooklangRecipe to a testable preview view-model
- **macos:** open .cook/.menu files on Finder double-click (open-file event)
- **macos:** preview controller with parse + text fallback
- **macos:** recipe formatting helpers for Quick Look preview
- **macos:** scaffold Quick Look appex (XcodeGen + CooklangParser)
- **win,linux:** register .cook/.menu file associations

**Fixed**

- **linux:** make deb maintainer scripts superset electron-builder defaults

#### 0.1.0-alpha.15 · 2026-06-06

**Fixed**

- **cookbot:** externalize gRPC packages and add bundle structural check
- **lint:** make lint pass across all packages

## May 2026

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.30.0 · 2026-05-18

**Added**

- add cook build static-site generator ([#344](https://github.com/cooklang/cookcli/issues/344))
- **shopping-list:** add --pantry and --ignore-pantry flags ([#340](https://github.com/cooklang/cookcli/issues/340))
- **sync:** OAuth 2.0 device-code login for CLI and Docker users ([#347](https://github.com/cooklang/cookcli/issues/347))

**Fixed**

- default new recipe path to current folder ([#332](https://github.com/cooklang/cookcli/issues/332)) ([#341](https://github.com/cooklang/cookcli/issues/341))
- don't treat Windows drive-letter colons as scaling delimiter ([#338](https://github.com/cooklang/cookcli/issues/338)), closes [#335](https://github.com/cooklang/cookcli/issues/335)
- **server:** recognize `duration` and `time required` as `time` aliases ([#342](https://github.com/cooklang/cookcli/issues/342)), closes [#320](https://github.com/cooklang/cookcli/issues/320)

## April 2026

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.29.1 · 2026-04-24

**Fixed**

- resolve menu recipe references from collection root in CLI ([#330](https://github.com/cooklang/cookcli/issues/330))
- scale menu recipe references by servings/yield ([#329](https://github.com/cooklang/cookcli/issues/329))
- shop list other ordering

#### 0.29.0 · 2026-04-14

**Added**

- live updates for shopping list page ([#325](https://github.com/cooklang/cookcli/issues/325))
- migrate shopping list to new format with checked state ([#318](https://github.com/cooklang/cookcli/issues/318))

**Fixed**

- escape single quotes in JS string literals to prevent XSS ([#326](https://github.com/cooklang/cookcli/issues/326))
- include menu freehand ingredients in web shopping list ([#324](https://github.com/cooklang/cookcli/issues/324))
- ingredient and cookware names invisible when printing in dark mode ([#322](https://github.com/cooklang/cookcli/issues/322)), closes [#319](https://github.com/cooklang/cookcli/issues/319)
- unreadable plan card on shopping list in dark mode ([#323](https://github.com/cooklang/cookcli/issues/323))

#### 0.28.1 · 2026-04-09

**Fixed**

- remove openssl dependency to fix Linux release builds ([#317](https://github.com/cooklang/cookcli/issues/317))
- resolve npm dependency security vulnerabilities

#### 0.28.0 · 2026-04-08

**Added**

- add --url-prefix flag for reverse proxy subpath support ([#309](https://github.com/cooklang/cookcli/issues/309))
- add Swedish to language switcher
- Added swedish translation ([#310](https://github.com/cooklang/cookcli/issues/310))
- update cooklang-import to 0.9.3

**Fixed**

- handle non-ASCII characters in pantry TOML keys ([#311](https://github.com/cooklang/cookcli/issues/311)) ([#313](https://github.com/cooklang/cookcli/issues/313))
- improve cooking mode responsiveness on smartphones ([#306](https://github.com/cooklang/cookcli/issues/306))
- prevent print layout from truncating recipe content ([#307](https://github.com/cooklang/cookcli/issues/307)), closes [#304](https://github.com/cooklang/cookcli/issues/304)

#### 0.27.2 · 2026-04-02

**Fixed**

- add "m" unit abbreviation, text-only timer test
- address review feedback on Docker permission fix
- address review feedback on JSON-LD schema output
- address second round of review feedback
- improve JSON-LD schema.org output for HowToStep
- quote pantry section names containing spaces in TOML output
- quote pantry section names containing spaces in TOML output, closes [#292](https://github.com/cooklang/cookcli/issues/292)
- quote section name with space in seed pantry.conf
- remove unused import, add zero-duration timer guard test
- resolve Docker volume permission issues when creating recipes
- resolve Docker volume permission issues when creating recipes, closes [#287](https://github.com/cooklang/cookcli/issues/287)
- use existing sections in pantry Add Item form
- use existing sections in pantry Add Item form, closes [#293](https://github.com/cooklang/cookcli/issues/293)

### [Cook Editor](https://github.com/cook-md/editor/blob/HEAD/CHANGELOG.md)

#### 0.1.0-alpha.9 · 2026-04-23

**Added**

- Added EPL attribution, written-source offer, and an About dialog disclosing
  the Eclipse Theia upstream and the project's EPL-2.0 license.

#### 0.1.0-alpha.8 · 2026-04-22

**Fixed**

- Including a recipe in another recipe now pulls in any sub-recipe references
  with their resolved scales applied.
- Resolved servings and yield units correctly when adding a menu to the
  shopping list.

#### 0.1.0-alpha.7 · 2026-04-21

**Fixed**

- Restored frontend features (autocomplete, ingredient/cookware lookups) in
  the Electron build that had regressed after the upstream merge.

#### 0.1.0-alpha.6 · 2026-04-20

**Added**

- Manual `Check for Updates` command in the menu, plus auto-updater fixes so
  users on shipped builds receive new alpha releases.

#### 0.1.0-alpha.5 · 2026-04-20

**Fixed**

- `cookbot.proto` is now packaged into `app.asar`, fixing AI features in the
  shipped binary.

#### 0.1.0-alpha.4 · 2026-04-20

**Added**

- Restored the full release build matrix (macOS x64 + arm64, Windows, Linux)
  after stabilizing CI.

**Fixed**

- Cooklang LSP autocomplete now stays responsive after workspace changes
  (folder open/close, recipe rename, etc.).
- Aligned `@theia/monaco-editor-core` versions across packages to prevent the
  silent dual-Monaco registration bug.

#### 0.1.0-alpha.2 · 2026-04-17

**Added**

- macOS code signing and notarization in the release workflow.

**Fixed**

- macOS zip artifact filenames now include the architecture suffix to avoid
  collisions between x64 and arm64 builds.

#### 0.1.0-alpha.1 · 2026-04-17

**Added**

- Subscription account widget shows the AI token balance and reset date.
- Pro plan fallback when `planName` is absent on active subscriptions.
- Refresh subscription state when the account widget activates.
- Desktop-return callback for the upgrade flow so users land back in the
  editor after subscribing.

**Changed**

- Renamed CookEd → **Cook Editor** and refreshed the splash screen.
- Dropped the sync-feature paywall: workspace sync is available to every
  logged-in user.
- AI credits and plan label now read directly from the cook.md API
  (`ai_credits_remaining`, `plan_slug`, `plan_name`).

**Fixed**

- Stopped shipping the Rust `target/` cache inside macOS bundles, cutting
  installer size significantly.
- Honor `WEB_BASE_URL` for `Get AI Addon` and other external links from the
  account widget (lets staging builds point at staging cook.md).
- Re-seed the frontend subscription cache on token refresh so stale state
  doesn't survive a re-login.
- Use Theia's shared-dependencies import for `@lumino/messaging` to avoid
  duplicate copies in the Electron build.

## March 2026

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.27.1 · 2026-03-24

**Fixed**

- filter artifact download in release pipeline
- filter artifact download to skip docker build cache in release pipeline

#### 0.27.0 · 2026-03-23

**Added**

- add fuzzy file reference autocomplete in editor

**Fixed**

- simplify regex patterns in editor completion

#### 0.26.0 · 2026-03-10

**Added**

- add CRUD subcommands to pantry CLI
- make Docker setup reusable and add automated image publishing

**Fixed**

- improve cook mode scroll, dark mode logo contrast, and print styles ([#264](https://github.com/cooklang/cookcli/issues/264), [#267](https://github.com/cooklang/cookcli/issues/267), [#268](https://github.com/cooklang/cookcli/issues/268))
- resolve two failing UI tests in CI

#### 0.25.1 · 2026-03-09

**Added**

- consolidate aisle.conf ingredients with synonyms
- group related ingredients in seed aisle.conf
- redesign seed folder to showcase Cooklang spec features

#### 0.25.0 · 2026-03-08

**Added**

- add GET /api/menus endpoint for listing menu files
- add GET /api/menus/*path endpoint for parsed menu data
- add GET /api/stats endpoint for recipe and menu counts
- add pantry expiring and depleted API endpoints
- show today's menu banner on recipes page
- show today's menu banner on recipes page

**Fixed**

- compile regexes once with LazyLock in menus handler
- make menu print view compact while keeping comfortable screen layout
- show ingredient quantities in shopping list print view
- simplify today's menu banner, remove meal pills and fix button padding

#### 0.24.0 · 2026-03-03

**Added**

- add cookcloud sync dependencies
- add CookCloud Sync section to Preferences page
- add CookCloud sync to CLI server
- add cooking_mode_ingredients field to RecipeSection
- add Docker build/push workflow with versioned images on ghcr.io
- add root docker-compose.yml, remove outdated docker/ directory
- add sync API endpoints (status, login, logout)
- add sync session and endpoint modules
- allow --host to take an optional IP argument
- make sync a default feature, exclude from Docker demo image
- make sync an optional feature flag
- populate cooking mode with uncombined aisle-sorted ingredients
- replace Dockerfile with multi-stage build for demo deployment
- start sync on server boot with graceful shutdown

**Fixed**

- add warning log on aisle file read failure in recipe handler
- address PR review feedback for sync implementation
- address review feedback for sync security, correctness, and UX
- align dev-dependency reqwest version with main dependency
- correct ENTRYPOINT arg order and add Docker build caching
- detect finished sync task and reflect accurate status in UI
- pin Docker builder stage to rust:bookworm for GLIBC compatibility
- sync bugs and code quality improvements
- updated sync
- use plain styling for CookCloud Sync section on preferences page
- use published cooklang 0.18.2 and async aisle file read
- use try_lock for sync handle to avoid blocking_lock panic

## February 2026

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.23.0 · 2026-02-16

**Added**

- add print support for shopping list page
- **cooking-mode:** add 'c' keyboard shortcut for cooking mode
- **cooking-mode:** add Close button to done card
- **cooking-mode:** add cooking mode JS with carousel, swipe, and wake lock
- **cooking-mode:** add cooking mode stylesheet
- **cooking-mode:** add scroll wheel navigation between cards
- **cooking-mode:** add Start Cooking button to recipe page
- **cooking-mode:** add tap-to-crossout for mise en place ingredients
- **cooking-mode:** click prev/next cards to navigate
- **cooking-mode:** embed recipe JSON data in template
- **cooking-mode:** include cooking mode CSS and JS in recipe template
- **cooking-mode:** smart swipe — scroll within card, navigate at boundaries
- propagate server error messages to UI
- remove print buttons from recipe and shopping list views

**Fixed**

- **cooking-mode:** address PR feedback for code quality and accessibility
- **cooking-mode:** escape &lt;/script&gt; sequences in embedded JSON
- **cooking-mode:** remove recipe name from done card
- improve pantry page layout on small screens
- preserve all pantry item attributes when quantity is present, closes [#249](https://github.com/cooklang/cookcli/issues/249)
- render fractional quantities with units in shopping list, closes [#258](https://github.com/cooklang/cookcli/issues/258)
- reset step numbers per section in recipe and cooking mode

#### 0.22.0 · 2026-02-10

**Added**

- add keyboard shortcuts for web UI, closes [#248](https://github.com/cooklang/cookcli/issues/248)
- support backslash line breaks for formatting in steps and notes

**Fixed**

- allow dirty working directory for cargo publish and format code
- issues with line break
- optimize web UI layout for tablet-sized screens
- resolve clippy warnings for unnecessary_unwrap
- update dependencies to resolve security vulnerabilities
- use if-let instead of is_some + unwrap for ingredient references

## January 2026

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.21.0 · 2026-01-21

**Added**

- **api:** add GET /api/recipes/raw/{path} endpoint
- **api:** add PUT /api/recipes/{path} endpoint
- **editor:** add autosave, remove preview, rename Cancel to Back
- **editor:** add CodeMirror editor entry point
- **editor:** add Cooklang syntax mode for CodeMirror 6
- **editor:** add delete recipe, improve editor UX
- **editor:** add LSP connection status indicator
- **editor:** add LSP document synchronization
- **editor:** add LSP-powered autocomplete
- **editor:** add new recipe creation page
- **editor:** add preview toggle
- **editor:** display LSP diagnostics in editor
- **editor:** integrate CodeMirror with syntax highlighting
- **editor:** Phase 4 - LSP client & full features
- **i18n:** add editor translation keys
- **i18n:** add LSP status translation keys
- improve PWA [#239](https://github.com/cooklang/cookcli/issues/239)
- **lsp:** add WebSocket to LSP subprocess bridge
- **lsp:** register WebSocket LSP endpoint at /api/ws/lsp
- **ui:** add /edit/{path} route for recipe editor
- **ui:** add Edit button to menu page
- **ui:** add Edit button to recipe detail page
- **ui:** add editor template with textarea
- **ui:** add New Recipe button to recipes list

**Fixed**

- add 1MB request body size limit
- address TOCTOU race condition in create_recipe
- clippy
- display errors to user via toast notifications
- **editor:** address code review feedback for recipe creation
- **editor:** pass base_path to LSP for aisle.conf loading
- **editor:** prevent HTML escaping of JSON in template
- **editor:** reset line-scoped states and fix Makefile clean target
- **editor:** use HighlightStyle for proper syntax highlighting
- fmt
- fmt
- improve LSP bridge task cleanup and document buffer size
- lsp version
- use published language srver
- use spawn_blocking for synchronous canonicalize calls
- use tokio::fs for async file deletion in recipe_delete
- use tokio::fs for async file operations in recipe_save
- use tokio::fs for async file reading in edit_page
- use tokio::fs for async file reading in pantry_page
- use tokio::fs for async file reading in recipe_raw
- validate filename before sanitization in create_recipe

#### 0.20.0 · 2026-01-16

**Added**

- add cook lsp subcommand for language server support
- also publish in crate
- combine duplicate ingredients in recipe display
- combine duplicate ingredients in web UI recipe display
- log context paths in LSP for debugging

**Fixed**

- display more context for errors
- extra space removed [#226](https://github.com/cooklang/cookcli/issues/226)

#### 0.19.3 · 2026-01-04

**Fixed**

- respect explicit low thresholds in pantry depleted command, closes [#228](https://github.com/cooklang/cookcli/issues/228)
- update macOS runners from deprecated macOS-13

## December 2025

### [CookCLI](https://github.com/cooklang/cookcli/blob/HEAD/CHANGELOG.md)

#### 0.19.2 · 2025-12-28

**Fixed**

- add Windows-specific snapshot for doctor validate test
- use consistent path separator in doctor validate output

#### 0.19.1 · 2025-12-27

**Added**

- improve breadcrumb
- remove ".cook" in the breadcrumb

**Fixed**

- add export of shopping list in markdown format
- add export of shopping list in markdown format
- better alignment in the breadcrumb
- notes are rendered in correct order between steps (web interface)
- show pantry inventory even if pantry.conf is empty, but show link to preferences page only if pantry.conf is not found
- use ingredient list with common names from aisle configuration
