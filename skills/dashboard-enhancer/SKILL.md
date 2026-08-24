---
name: dashboard-enhancer
description: Design, audit, and improve professional dashboards, admin panels, backoffices, CRMs, ERPs, analytics screens, and SaaS interfaces. Prioritizes data-driven UI, information hierarchy, progressive disclosure, complete component states, interaction design, accessibility, and responsive behavior over generic card-soup layouts. Use when the user asks to design, build, review, critique, or enhance any dashboard, admin interface, data-heavy screen, table view, KPI panel, or internal tool.
---

# Dashboard Enhancer

## Purpose

This skill defines how to design and evaluate dashboards, admin panels, backoffices, CRMs, ERPs, management systems, analytics dashboards, and professional SaaS applications.

The goal is not simply to create a visually attractive interface.

The goal is to create an interface that allows the user to:

**see → understand → decide → act**

with the least possible cognitive friction.

---

## Ask first

Never invent missing context silently. Before designing any screen, check the brief for:

- Who uses it: role, frequency of use, consequence of errors.
- The tasks and decisions the interface must support.
- What entities, states, and permissions exist in the data model.
- Target devices and breakpoints that matter.

If answers are missing, ask up to 5 batched questions — never one at a time.

For every question, propose a smart default:

> If no answer: assume this default and proceed.

Silence or a bare "ok" means the defaults are accepted. Never ask what the provided code, data, screenshots, or repo context already answer.

---

# Core Philosophy

# 1. Data drives the UI

The data must determine the shape of the interface.

Never start with:

> "What cards, charts, or components can I add?"

Start with:

> "What information exists, what does the user need to understand, and what is the best representation for that information?"

### Mandatory mapping

| Data                   | Preferred UI             |
| ---------------------- | ------------------------ |
| Metric                 | KPI / Metric             |
| Comparison             | Table                    |
| Time evolution         | Line / Area chart        |
| Distribution           | Bar chart                |
| Status                 | Badge / Chip             |
| Temporal activity      | Timeline / Activity feed |
| Entity                 | List / Table / Card      |
| Contextual information | Tooltip / Popover        |
| Detail                 | Drawer / Detail view     |
| Configuration          | Form                     |
| Secondary action       | Dropdown / Context menu  |
| Quick action           | Inline action            |
| Location               | Map                      |
| Hierarchical relation  | Tree / Nested list       |

Do not assume a table is correct simply because the data is tabular.

Do not assume a card is correct simply because this is a dashboard.

---

# 2. Design around user tasks

Before designing a screen, identify:

* What the user needs to know.
* What the user needs to do.
* What they do frequently.
* What they do occasionally.
* Which actions are dangerous.
* What information needs context.
* Which decisions they must be able to make.

Prioritize the UI according to:

**frequency × importance × consequence**

### High frequency + high importance

Always visible.

Examples:

* Search
* Create
* Save
* Check status

### High frequency + low importance

Visible or contextual.

### Low frequency + high consequence

Easy to find, but protected.

Examples:

* Delete
* Cancel
* Deactivate

### Low frequency + low consequence

Progressively disclosed.

Examples:

* Copy ID
* Export
* Metadata

---

# 3. Information hierarchy

Every screen must have an evident visual hierarchy.

Priority:

1. Critical information.
2. Primary action.
3. Key metrics.
4. Problems and alerts.
5. Secondary information.
6. Secondary actions.
7. Technical or contextual information.

The hierarchy must use:

* Size.
* Typographic weight.
* Contrast.
* Spacing.
* Position.
* Grouping.
* Color.
* Density.

Do not give every element the same visual weight.

---

# 4. Avoid card soup

Do not automatically turn every section into a card.

Ask:

> "Does this content really need a visual container?"

You can use:

* Spacing.
* Dividers.
* Grouping.
* Typography.
* Sections.
* Subtle backgrounds.

Cards should be used when they help group information or create a conceptual unit.

Do not use them simply because "a dashboard has cards".

---

# 5. Progressive Disclosure

Do not show all functionality at once.

Use the spectrum of explicitness:

```text
ALWAYS VISIBLE
      ↓
VISIBLE IN CONTEXT
      ↓
VISIBLE ON INTERACTION
      ↓
VISIBLE WHEN REQUESTED
```

### Always visible

* Primary action.
* Search.
* Critical filters.
* Important navigation.

### Contextual

* Edit.
* Share.
* Export.
* Secondary actions.

### Interaction

* Copy.
* Delete.
* Row actions.
* Additional metadata.

### Requested

* Advanced configuration.
* Technical details.
* Full history.
* Metadata.

Do not hide an important feature just to achieve a minimalist look.

---

# 6. UI is what you can't see

Design both the visible UI and the contextual UI explicitly.

Every component must consider:

* Default.
* Hover.
* Focus.
* Active.
* Selected.
* Disabled.
* Loading.
* Empty.
* Error.
* Success.

Additionally consider:

* Tooltip.
* Popover.
* Dropdown.
* Drawer.
* Modal.
* Toast.
* Context menu.
* Confirmation.
* Inline editing.
* Keyboard interaction.

An interface is not finished when its normal state is designed.

---

# 7. State-first design

Before considering a component finished, define its states.

## Buttons

```text
Default
Hover
Focus
Active
Disabled
Loading
Success
Error
```

## Inputs

```text
Empty
Focused
Filled
Invalid
Disabled
Read-only
Loading
```

## Tables

```text
Loading
Empty
Populated
Filtered
Selected
Error
Partial
```

## Pages

```text
Loading
Empty
Error
Unauthorized
Forbidden
Offline
Success
```

---

# 8. Empty states

Never settle for:

> "No data."

An empty state must explain:

1. What is empty.
2. Why.
3. What the user can do.

Prefer:

```text
You don't have any clients yet.

Register your first client to get started.

[ + New client ]
```

The empty state must be functional, not merely informative.

---

# 9. Loading states

Choose the loading state according to context.

Use:

* Skeleton.
* Spinner.
* Progress.
* Optimistic UI.
* Placeholder.

Prefer skeletons when the content structure is known.

Avoid blocking the entire screen with a spinner when only one section is loading.

---

# 10. Error handling

Every visible error must answer:

* What happened.
* What its impact is.
* What the user can do.

Avoid:

```text
Error 500.
```

Prefer:

```text
We couldn't load the reservations.

Try again.

[ Retry ]
```

Whenever possible:

* Preserve entered data.
* Maintain context.
* Allow retry.
* Explain recovery.
* Avoid forcing the user to repeat work.

---

# 11. Feedback

Every important action must provide feedback.

Example:

```text
Save
↓
Saving...
↓
Changes saved ✓
```

The user should never be left wondering:

> "Did it work?"

Use:

* Toast.
* Inline feedback.
* State change.
* Progress.
* Confirmation.
* Undo.

### Toasts are the notification system

Use toasts whenever the user must be made aware of something without taking over the screen or being forced to act.

Toasts are not only for success — warnings and errors frequently belong here too, and they are the states most often forgotten:

```text
✓ Link created                    [ View ]
⚠ 2 links failed to update        [ Retry ]
✕ Connection lost — changes saved locally
```

---

# 12. Undo over confirmation when appropriate

For reversible actions, prefer Undo when it is more efficient than a modal.

Example:

```text
Client archived.

[ Undo ]
```

Do not constantly interrupt the flow with unnecessary confirmations.

For irreversible or high-impact actions, use explicit confirmation.

---

# 13. Tables

A table must exist because it facilitates a task.

It should account for, when applicable:

* Search.
* Filtering.
* Sorting.
* Pagination.
* Selection.
* Bulk actions.
* Row actions.
* Column visibility.
* Export.
* Detail view.

## Column hierarchy

Classify columns:

### Primary

Always visible.

### Secondary

Hideable or adaptable.

### Contextual

Show via:

* Drawer.
* Expanded row.
* Detail page.
* Popover.

---

# 14. Table interaction

Avoid placing too many actions directly on each row.

Prefer:

```text
⋯
```

for secondary actions.

Use hover to reveal actions when appropriate.

Example:

```text
Juan Pérez     Admin     Active     ⋯
```

Do not turn every row into a toolbar.

---

# 15. Numbers

Numeric values must be correctly aligned.

By default:

**right-align numbers**

This makes comparison easier:

```text
$       9,500
$      25,000
$     125,000
$   1,250,000
```

Use consistent formats:

* Currency.
* Percentage.
* Decimals.
* Separators.
* Units.

---

# 16. Text truncation

Do not let long text break a table or layout.

Use:

* Ellipsis.
* Tooltip.
* Expand.
* Drawer.
* Detail view.

Never sacrifice the entire interface structure to display secondary text in full.

---

# 17. Semantic color

Color must carry meaning.

Use color mainly for:

* Success.
* Warning.
* Error.
* Info.
* Status.
* Priority.
* Selection.

Do not use arbitrary colors solely to decorate cards.

### Important

Never communicate information through color alone.

Combine:

**color + icon + label**

when relevant.

---

# 18. Charts

A chart must answer a question.

Before adding one:

> "What decision does this chart enable?"

Use charts for:

* Trends.
* Comparisons.
* Distributions.
* Anomalies.
* Evolution.
* Relationships.

Do not add charts simply because "the dashboard needs graphs".

---

# 19. Dashboard hierarchy

A general dashboard should normally follow:

```text
Global status
      ↓
Key metrics
      ↓
Alerts / problems
      ↓
Trends
      ↓
Recent activity
      ↓
Actions
      ↓
Detailed analysis
```

Do not turn the main dashboard into a reports page.

Its primary purpose is:

> **to orient the user and enable action.**

---

# 20. KPI design

A KPI must provide context.

Do not show only:

```text
1,248
```

Prefer:

```text
CLIENTS

1,248

↑ 12.5%
vs. previous month
```

A KPI should answer:

* What.
* How much.
* Compared to what.
* Whether it is improving or getting worse.

---

# 21. Alerts

Alerts must represent actionable problems.

Example:

```text
⚠ 3 products have critical stock

[ View products ]
```

Do not overuse alerts.

> If everything is urgent, nothing is urgent.

---

# 22. Activity feeds

Activity feeds should communicate:

* Who.
* What.
* Which entity.
* When.

Example:

```text
Juan created a reservation
3 minutes ago

María confirmed a payment
8 minutes ago
```

Use avatars/icons when they speed up recognition.

---

# 23. Context preservation

Do not unnecessarily lose:

* Search.
* Filters.
* Sorting.
* Pagination.
* Selected items.
* Scroll position.
* Current tab.

If the user returns to a screen, preserve their context when reasonable.

---

# 24. Navigation

Navigation must reflect the user's mental model, not the internal architecture of the code.

Example:

```text
Dashboard

OPERATIONS
  Clients
  Sales
  Inventory

ANALYSIS
  Reports
  Statistics

SYSTEM
  Settings
```

Separate conceptually:

* Operations.
* Analysis.
* Administration.
* Configuration.

---

# 25. Contextual navigation

Within an entity use:

* Tabs.
* Secondary navigation.
* Breadcrumbs.

Example:

```text
Client
├── Information
├── Activity
├── Purchases
├── Payments
└── History
```

Do not send the user to separate pages when internal context is sufficient.

---

# 26. Modals vs Drawers vs Popovers

## Modal

For:

* Important confirmations.
* Focused tasks.
* Actions that require interruption.

## Drawer

For:

* Details.
* Inspection.
* Contextual editing.
* Extensive information.

## Popover

For:

* Quick actions.
* Filters.
* Contextual information.
* Small content.

## Tooltip

For:

* Brief explanations.
* Icons.
* Ambiguous labels.

## Decision criteria

Classify by context complexity and blocking cost:

```text
Popover    simple context, non-blocking
           user can click away without consequences

Modal      complex context, blocking
           task is directly related to the content on screen
           user must complete or cancel before continuing

New page   permanent or very large context
           destination has its own URL and depth
```

A modal hides the page while changes are being made, so confirm the result with a toast when it closes.

Never navigate to a new page without a back button or breadcrumbs.

---

# 27. Responsive

Not simply shrinking desktop.

Every breakpoint must have a strategy.

### Desktop

Prioritize:

* Density.
* Comparison.
* Multi-column.
* Sidebar.

### Tablet

Reduce:

* Columns.
* Navigation.
* Simultaneous actions.

### Mobile

Transform:

* Tables → lists/cards.
* Filters → drawer.
* Actions → menus.
* Sidebar → navigation menu.
* Secondary information → detail view.

Ask:

> "What information can disappear without affecting the task?"

---

# 28. Accessibility

Every dashboard must consider:

* WCAG principles.
* Contrast.
* Keyboard navigation.
* Focus.
* Screen readers.
* Semantic HTML.
* Labels.
* Accessible names.
* Reduced motion.

Do not use color as the only indicator.

Icon-only buttons need accessible labels.

Focus states must be visible.

---

# 29. Design tokens

Maintain consistency through tokens.

## Spacing

```text
4
8
12
16
24
32
48
64
```

## Typography

```text
Display
Heading
Body
Label
Caption
```

## Color

```text
Background
Surface
Border
Text
Muted
Primary
Success
Warning
Danger
Info
```

## Radius

Use a limited, consistent system.

Do not assign arbitrary values to each component.

---

# 30. Consistency

The same action must look and behave similarly across the entire product.

If:

```text
[ + New client ]
```

is the primary action in Clients, use the same pattern for:

```text
[ + New sale ]
[ + New product ]
[ + New reservation ]
```

Consistency reduces learning.

---

# 31. Microinteractions

Use animation to communicate:

* Change.
* Cause and effect.
* Entrance.
* Exit.
* Feedback.
* Spatial continuity.

Do not use animation solely for decoration.

### Rule

> Animation should explain a transition, not compete with the content.

---

# 32. Performance perception

The user must perceive that the application responds.

Consider:

* Skeletons.
* Optimistic updates — apply the change instantly and assume the request succeeds; roll back visibly if it fails. Users prefer a snappy dashboard over correct-but-slow pauses.
* Lazy loading.
* Pagination.
* Virtualization.
* Progressive loading.
* Immediate feedback.

Do not block the entire interface when only one section is loading.

---

# 33. Forms

Show the necessary information first.

Separate:

### Essential

Fields required to complete the task.

### Optional

Complementary information.

### Advanced

Technical settings.

Example:

```text
New product

Name *
Price *
Category *

[ More options ]

Stock
Supplier
SKU
Taxes
Metadata
```

Do not present 30 fields when only 4 are needed to begin.

---

# 34. Validation

Validate close to the problem.

Prefer:

```text
Email

luigi@

⚠ Enter a valid email address
```

instead of waiting until submit to report all errors.

Always preserve entered data whenever possible.

---

# 35. Destructive actions

High-impact actions need greater explicitness.

Examples:

* Delete.
* Cancel.
* Disable.
* Reset.
* Remove.

Consider:

* Context.
* Confirmation.
* Consequence.
* Undo.
* Reauthentication.

Never place important destructive actions next to frequent actions without sufficient differentiation.

---

# 36. Permissions

The UI must account for roles and permissions.

Do not show actions the user cannot perform when hiding them is clearer.

Consider:

```text
View
Create
Edit
Delete
Export
Manage
Configure
```

Do not assume all users have the same level of access.

---

# 37. Auditability

For enterprise systems, consider:

```text
Who
What
When
Before
After
```

Example:

```text
Juan Pérez

Updated the price.

Previous: $25,000
New:      $27,500

Aug 23, 2026 — 4:42 PM
```

Especially important for:

* ERP.
* CRM.
* Inventory.
* Finance.
* Administration.

---

# 38. Cognitive load

Reduce:

* Simultaneous decisions.
* Redundant information.
* Unnecessary colors.
* Unnecessary buttons.
* Unnecessary text.
* Ambiguous navigation.
* Unclear states.

Use:

* Grouping.
* Hierarchy.
* Progressive disclosure.
* Consistency.
* Context.
* Smart defaults.

---

# 39. Scanability

Users generally scan dashboards before reading them.

Design so they can quickly identify:

* What is happening.
* What changed.
* What is wrong.
* What requires attention.
* What they can do.

Use:

* Headings.
* Numbers.
* Badges.
* Icons.
* Alignment.
* Whitespace.
* Grouping.

---

# 40. Three-level information architecture

Design information in levels.

## Level 1 — Scan

Immediately visible information.

## Level 2 — Inspect

Contextual information when drilling deeper.

## Level 3 — Act

Specific actions.

Example:

```text
CLIENT

Juan Pérez
Active
$125,000

        ↓

Details
Email
Phone
Last purchase

        ↓

Actions
Edit
Archive
More actions
```

---

# 41. Decision framework

Before adding any element, answer:

```text
1. What information does it represent?
2. Why does it need to exist?
3. Who needs it?
4. How often?
5. What decision does it enable?
6. What action does it allow?
7. Should it always be visible?
8. Can it be contextual?
9. What happens when it is empty?
10. What happens if it fails?
```

If it has no clear answer:

**consider removing it.**

---

# 42. Dashboard quality test

A dashboard must be evaluable with these questions:

### Data

* Do the data drive the UI?
* Is the representation appropriate?

### Hierarchy

* What do I see first?
* What can I ignore?

### Action

* What is the primary action?
* Can I find it immediately?

### Context

* Do I know where I am?
* Do I know which entity I am working on?

### State

* What happens while loading?
* What happens when empty?
* What happens if it fails?

### Interaction

* What appears on hover?
* What appears on focus?
* Which actions are hidden?

### Feedback

* Do I know whether my action worked?

### Accessibility

* Can I use it with a keyboard?
* Is color alone sufficient?
* Do icons have accessible meaning?

### Responsive

* What happens on mobile?

---

# 43. Mandatory design workflow

When this skill is used to create a dashboard, follow this order:

## Step 1 — Understand

Identify:

* User.
* Role.
* Goals.
* Tasks.
* Data.
* Frequency.
* Consequences.

## Step 2 — Model

Define:

* Entities.
* Relations.
* States.
* Permissions.
* Data dimensions.

## Step 3 — Prioritize

Classify:

* Primary.
* Secondary.
* Contextual.
* Advanced.

## Step 4 — Choose representation

Determine:

* Table.
* Chart.
* Timeline.
* List.
* Card.
* Metric.
* Form.
* Drawer.
* Popover.

## Step 5 — Structure

Create:

* Navigation.
* Sections.
* Hierarchy.
* Layout.
* Information levels.

## Step 6 — Interaction

Define:

* Hover.
* Focus.
* Click.
* Selection.
* Menus.
* Shortcuts.
* Inline actions.

## Step 7 — States

Design:

* Loading.
* Empty.
* Error.
* Success.
* Disabled.
* Offline.
* Permission denied.

## Step 8 — Responsive

Define behavior:

* Desktop.
* Tablet.
* Mobile.

## Step 9 — Accessibility

Review:

* Keyboard.
* Contrast.
* Labels.
* Focus.
* Semantic structure.

## Step 10 — Polish

Only then optimize:

* Typography.
* Spacing.
* Colors.
* Borders.
* Radius.
* Shadows.
* Animation.

**Visual polish comes last.**

---

# 44. Anti-patterns

Explicitly avoid:

## Generic dashboard

```text
6 cards
+
3 charts
+
recent activity
+
table
```

with no functional reason.

## Card soup

Everything turned into cards.

## Chart decoration

Charts that answer no question.

## Rainbow UI

Colors without meaning.

## Button overload

Too many visible actions.

## Modal overload

Everything resolved with modals.

## Tooltip dependency

Fundamental information hidden in tooltips.

## Desktop shrinking

Desktop simply scaled down for mobile.

## One-state design

Designing only the normal state.

## Empty dashboard

A dashboard that does not orient the user.

## Decorative minimalism

Hiding important features solely to achieve a "clean" look.

---

# 45. Final principles

These rules take priority during any design:

1. **Data drives the UI.**
2. **User tasks drive the hierarchy.**
3. **Important actions remain discoverable.**
4. **Secondary actions are progressively disclosed.**
5. **Every component has states.**
6. **Every important action provides feedback.**
7. **Color communicates meaning.**
8. **Not everything needs a card.**
9. **Not everything needs a table.**
10. **Charts must answer questions.**
11. **Context should be preserved.**
12. **Errors should be recoverable.**
13. **Accessibility is part of the design, not an afterthought.**
14. **Responsive behavior must be intentionally designed.**
15. **Visual polish comes after information architecture and interaction design.**

---

# 46. Audit mode

Use this mode when reviewing an EXISTING dashboard rather than designing a new one.

## Process

1. Inventory every screen/state you can see.
2. Score each dimension 0–10.
3. Log findings tagged blocker / major / minor.
4. Deliver fixes ordered by impact ÷ effort.

## Scoring rubric

Each dimension scores 0–10. Maximum total: 100.

| Dimension                              | Question                                                            | Score |
| -------------------------------------- | ------------------------------------------------------------------- | ----- |
| Data–UI fit                            | Does every representation match its data type?                      | /10   |
| Information hierarchy                  | Is critical information what users see first?                       | /10   |
| Primary action discoverability         | Can the primary action be found immediately?                        | /10   |
| State coverage (loading/empty/error)   | Are loading, empty, and error states designed for key components?   | /10   |
| Feedback on actions                    | Does every important action confirm its result?                     | /10   |
| Context preservation                   | Do filters, sorting, pagination, and selection survive navigation?  | /10   |
| Accessibility                          | Can it be operated by keyboard alone, without relying on color?     | /10   |
| Responsive behavior                    | Does each breakpoint have an intentional strategy, not a shrink?    | /10   |
| Cognitive load                         | Are simultaneous decisions and redundant elements minimized?        | /10   |
| Visual consistency                     | Do the same actions look and behave the same everywhere?            | /10   |

## Verdict thresholds

```text
0–39   Redesign the core flow
40–69  Targeted fixes
70–100 Polish only
```

## Finding format

Log every finding using this structure:

```text
[MAJOR] Reservations table — no empty state
Score impact: -2 (State coverage)
Fix: Add empty state with primary action [+ New reservation]
Effort: Low
```

Order the final report by impact ÷ effort, highest first.

---

# 47. Sidebar anatomy

The sidebar is the spine of the product: it houses persistent, globally relevant elements.

Typical contents:

* Navigation.
* Profile management.
* Search.

Profile management and search may also live in the top bar — choose one and stay consistent.

## Structure, top to bottom

```text
┌──────────────────┐
│ ◔ Acme Inc   ⌄   │  profile / workspace switcher
│                  │  avatar + chevron signals clickability
│ ◇ Home           │
│ Links       3  │  icon + short label + badge chip
│ Analytics      │
│                  │
│ ≡ Settings        │  rare items sink to the bottom
│ ? Help center     │
└──────────────────┘
```

Rules:

* Each link pairs a recognizable icon with a short title — this is what makes the sidebar collapsible to icons-only.
* Icon + label slots also carry notification counts and "new" chips naturally.
* Group links by relevance; navigation exists to reduce cognitive load.
* Rarely used items (settings, help) go to the bottom, separated.
* As links grow, nest them into dropdowns.
* Always provide an active-state indicator on the current location.
* Optional: a promo slot for features/integrations, and notifications can fill leftover space.

---

# 48. Density and type scale

A dashboard is not a landing page. Its typography follows different physics:

* Smaller sizes overall — more content must fit.
* Tighter scale steps — less spacing between levels than marketing pages use.
* Grids are followed strictly — dashboards use most or all of the screen; whitespace is budgeted, not generous.
* Component features shrink accordingly: smaller paddings, denser rows.

What occupies the main section declares what matters most to the user:

```text
Project management tool → project status up top
Financial dashboard     → investments up top
Link tracker            → link management up top
```

Start from a simple grid (for example two columns × two rows), place the primary working surface at the top, and supporting metrics below. The very top row is reserved for page actions and simple controls.

---

# 49. List separation

Lists need visual separation between items. Three tools, in order of quietness:

1. **Space** — padding alone. Quietest option.
2. **Dividers** — lines between rows. Default choice for data rows.
3. **Color** — alternating or hover backgrounds. Strongest signal, noisiest.

Prefer stacking items into a single list over giving every item its own bordered card — cards multiply clutter.

The list layout also makes empty states natural: one region, one message, one action.

---

# 50. Bulk selection and contextual actions

Static lists are not enough in real applications — users must manage data efficiently.

Support multi-selection (checkboxes, click, shift-click). Selection is a state change that should reveal new context rather than navigate:

```text
☐ 3 selected        [ Archive ]  [ Delete ]   [ Cancel ]
```

Rules:

* The bulk-action bar appears only when selection exists.
* Dangerous bulk actions keep their protections (confirmation, undo).
* Show the count — "3 selected", never just buttons.
* Always offer an explicit exit (Cancel, clear selection).

---

# 51. Chart fundamentals

Charts fail at basics before they fail at beauty.

* Do not invent exotic chart types nobody can read. Start from line charts for time series and bar charts for per-item comparison.
* Add grid lines and axis numbers — everyone forgets them, and without them values cannot be judged.
* Pair every chart with a summary value and a date-range selector.
* Use the same range selector across all charts on the screen — one control, many charts.
* Make chart series switchable when relevant (e.g. toggling signups vs conversions on the same plot).
* Identify bar/line series with icons or labels (a favicon next to each link's bar beats a legend).
* Microinteractions that inform: hover reveals exact value + tooltip bubble; hovering one bar may dim the others to focus attention.

Informative and aesthetic are not in conflict — but information comes first.

---

# 52. The four building blocks

Nearly every dashboard page is composed of four elements:

| Block | Used for | Notes |
|---|---|---|
| Lists & tables | The main working surface | Separation via space/dividers/color; tables become tools with search, filter, sort |
| Cards | Charts, toasts, grouped content | Keep margins well spaced; choose border OR background tint — outlines suit dark mode, tints suit light mode |
| User input | Modals, settings pages, forms | See Forms skill for depth |
| Tabs | New views without sidebar clutter | Related views of related data in one context |

Master these four and any dashboard page becomes layout work, not invention.

Example decomposition — a settings modal is mostly lists plus some inputs plus some cards, inside a modal. A Notion-style view switcher is tabs over related tables.

---

# Final Mental Model

When designing a dashboard, always think:

```text
DATA
  ↓
MEANING
  ↓
REPRESENTATION
  ↓
HIERARCHY
  ↓
PROGRESSIVE DISCLOSURE
  ↓
INTERACTION
  ↓
STATE
  ↓
FEEDBACK
  ↓
ACCESSIBILITY
  ↓
RESPONSIVE
  ↓
VISUAL POLISH
```

The expected result is not:

> "A pretty dashboard."

The expected result is:

> **A tool that enables the user to understand information, detect important situations, and act quickly.**

---

# Golden Rule

> ## Don't design the dashboard.
>
> ## Design the user's understanding of the data.

A professional dashboard must enable:

**SEE → UNDERSTAND → DECIDE → ACT**

with the least possible friction.
