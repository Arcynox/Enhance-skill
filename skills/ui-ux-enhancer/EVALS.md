# Evals — ui-ux-enhancer

Test prompts to verify this skill changes agent behavior. Each eval lists expected behaviors and failure anti-patterns.

## Eval 1 — Interactive affordances

**Prompt:** Make this pricing page's plan cards selectable and add a contact form.

**Expected behavior:**
- Gives every interactive element a visible affordance before interaction (contained shape, subtle depth, pointer cursor, hover response) and leaves static content flat
- Uses the correct control for each action: checkbox/switch for toggles, button for submit, never text that looks like body copy but must be clicked
- Follows platform conventions instead of inventing new shapes for standard controls
- No design requires the words "click here" to be understandable

**Fails if:**
- Renders selectable plans as plain paragraphs with no hover, cursor, or shape signal
- Styles non-clickable headlines as buttons
- Relies on a tooltip to explain that something is clickable

## Eval 2 — Signifiers on selection

**Prompt:** Build tabs for a restaurant menu: Drinks, Food, Desserts.

**Expected behavior:**
- Marks the active tab with at least two stacked signifiers (e.g. background fill + bold weight + accent border-bottom) so selection survives color blindness, dark mode, and low-quality screens
- Keeps inactive tabs muted, flat, and unmarked
- Shows hover and focus signals distinct from the selected state

**Fails if:**
- Communicates the active tab with color alone
- Makes active and inactive tabs visually identical except for a 5% opacity shift
- Removes the focus indicator on keyboard navigation

## Eval 3 — Button system discipline

**Prompt:** Add Save, Cancel, Delete account, and Export CSV actions to the settings screen.

**Expected behavior:**
- Exactly one filled primary button per view; Save gets it, the rest are outlined, ghost, or destructive variants
- Labels use concrete verbs ("Delete account", not "OK" / "Confirm")
- Delete account is red-palette, isolated from frequent actions, and asks for a confirmation naming the consequence
- Places the primary action at the end of the reading flow (right side in LTR dialogs)
- Buttons meet ~40–44px minimum height with fully clickable area

**Fails if:**
- Fills three buttons with equal visual weight on one screen
- Labels the destructive action "Confirm"
- Places Delete directly next to Save with identical styling

## Eval 4 — Dark mode done right

**Prompt:** La app se ve horrible en modo oscuro, revísala.

**Expected behavior:**
- Re-maps every token by hand (background, surface, border, text, primary action) instead of mechanically inverting hex values
- Desaturates brand and accent colors; avoids pure black backgrounds and pure white text
- Communicates elevation with lighter surface tones and lighter borders since shadows barely register on dark surfaces

**Fails if:**
- Inverts `#FFFFFF` → `#000000` and calls it dark mode
- Keeps saturated brand blues that vibrate against dark backgrounds
- Relies on unchanged dark shadows as the only elevation cue

## Eval 5 — Choosing the right overlay

**Prompt:** I need to show edit details for a row. Should it be a modal? Also add a toast when saved and tooltips on the icons.

**Expected behavior:**
- Picks the lightest interruption that solves the problem: drawer or popover for contextual editing rather than a blocking modal by default; modal only when interruption is required
- Configures overlays correctly: modal traps focus, closes via ESC and backdrop, restores focus to trigger, locks background scroll; toast auto-dismisses in 4–6s and is manually dismissible; tooltip waits ~300ms and holds only clarification
- Respects the z-order ladder (drawer < modal < toast)

**Fails if:**
- Opens a modal for every small detail view
- Creates a toast containing critical info the user can never retrieve again
- Lets tooltips host required actions or blocks pointer interaction while visible

## Eval 6 — Grid, spacing, and type scale consistency

**Prompt:** Review this landing section code. Something feels off but I can't tell what.

**Expected behavior:**
- Audits alignment first: section edges snap to shared column grid lines, gutters consistent across breakpoints, text measure capped at 45–75 characters
- Checks spacing against one 4px-based scale, flagging arbitrary values like 13px or 27px, and verifies inner padding < component gap < section gap
- Verifies sizes come from a fixed type scale with hierarchy built from weight and color before size inflation, sentence case labels, ALL CAPS only on tiny overlines

**Fails if:**
- Fixes the "off" feeling by adding decorative gradients or shadows without checking alignment first
- Introduces new arbitrary spacing values while "fixing" rhythm
- Adds a third typeface or freestyle font sizes between scale steps
