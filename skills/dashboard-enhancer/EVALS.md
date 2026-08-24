# Evals — dashboard-enhancer

Test prompts to verify this skill changes agent behavior. Each eval lists expected behaviors and failure anti-patterns.

## Eval 1 — CRM sales dashboard from scratch

**Prompt:** Hazme un dashboard de ventas para un CRM.

**Expected behavior:**
- Asks for or states the data model before choosing components, mapping each metric to its preferred UI (metric → KPI, time evolution → line chart, status → badge)
- Follows the dashboard hierarchy: global status → key metrics → alerts → trends → recent activity → actions
- KPIs include context: label, value, delta vs. previous period (e.g. `↑ 12.5% vs. previous month`), not a bare number
- Avoids the generic "6 cards + 3 charts + table" layout without functional justification
- States that charts must answer a question and drops any chart that answers none

**Fails if:**
- Produces card soup: every section wrapped in a card with equal visual weight
- Adds decorative charts with no stated decision they enable
- Shows bare numbers like `1,248` with no comparison or trend direction

## Eval 2 — Data table design

**Prompt:** Design a clients table for an admin panel with name, email, total spend, and status.

**Expected behavior:**
- Right-aligns numeric columns (`Total spend`) and left-aligns text columns, showing consistent currency formatting
- Classifies columns as primary / secondary / contextual instead of showing everything always visible
- Uses a single `⋯` overflow menu for secondary row actions rather than a toolbar per row
- Plans truncation for long emails via ellipsis plus tooltip or drawer detail view

**Fails if:**
- Centers or left-aligns money values so magnitudes cannot be compared by digit
- Puts edit, delete, export, copy ID, and history all inline on every row
- Lets long text wrap or break the layout with no truncation strategy

## Eval 3 — States before styling

**Prompt:** Build an inventory screen for this ERP spec I'll paste below.

**Expected behavior:**
- Defines loading, empty, error, success, disabled, and offline states before any visual polish
- Chooses skeletons over a full-screen spinner when the content structure is known, loading only the affected section
- Empty state explains what is empty, why, and offers the next action with a button like `[ + New product ]`
- Error messages answer what happened, what the impact is, and how to recover (e.g. `[ Retry ]`) instead of `Error 500`

**Fails if:**
- Designs only the populated happy path
- Blocks the entire screen with one spinner because a single widget is loading
- Ships `No data.` as the empty state with no explanation or action
- Reports failures as raw codes with no recovery path

## Eval 4 — Status colors and accessibility

**Prompt:** Muestra el estado de cada pedido con colores en la tabla de pedidos.

**Expected behavior:**
- Reserves semantic hues strictly (green = success, amber = warning, red = danger) and refuses arbitrary decorative colors
- Never communicates status through color alone; combines color + icon + label on every badge
- Keeps contrast at WCAG-compliant levels and keeps focus states visible for keyboard users
- Gives icon-only buttons accessible names

**Fails if:**
- Marks failed orders with only a red dot and no icon or text
- Uses brand accent colors interchangeably with success/error semantics
- Removes focus outlines to make the design look cleaner

## Eval 5 — Destructive vs reversible actions

**Prompt:** Add archive and delete options to the client detail page.

**Expected behavior:**
- Treats archive as reversible: executes it and offers `[ Undo ]` feedback instead of interrupting with a confirmation modal
- Treats delete as irreversible: explicit confirmation naming the consequence, distinct red styling, isolated from frequent actions
- Never places the destructive action adjacent to frequent actions without sufficient differentiation
- Provides clear feedback after both actions so the user never wonders "did it work?"

**Fails if:**
- Asks "Are you sure?" for every minor reversible change
- Executes permanent deletion silently with no confirmation and no undo
- Places Delete directly next to Save with identical styling

## Eval 6 — Responsive strategy per breakpoint

**Prompt:** Este panel administrativo se ve roto en el celular, arréglalo.

**Expected behavior:**
- Redesigns each breakpoint intentionally instead of shrinking desktop: tables become lists/cards, filters move to a drawer, sidebar becomes a navigation menu, secondary info moves to detail views
- Asks what information can disappear on mobile without affecting the task
- Keeps gutters, margins, and grouping logic consistent while reducing column count

**Fails if:**
- Scales the desktop layout down until columns are unreadably narrow
- Hides critical primary actions behind horizontal scroll on mobile
- Changes navigation structure between breakpoints so users lose orientation

## Eval 7 — Progressive disclosure in forms

**Prompt:** Create a "New product" form. It has around 30 fields in the spec.

**Expected behavior:**
- Splits fields into essential, optional, and advanced; shows only what is needed to begin (e.g. Name, Price, Category) behind a `[ More options ]` disclosure
- Validates close to the problem: inline errors next to the failing field as the user types, preserving entered data
- Groups remaining sections with spacing and headings rather than dumping 30 inputs in one scroll

**Fails if:**
- Renders all 30 fields immediately at equal weight
- Waits until submit to reveal every validation error at once
- Clears the user's input when validation fails

## Eval 8 — Context preservation across navigation

**Prompt:** When users click a reservation row and go back, their filters reset. Fix the UX.

**Expected behavior:**
- Preserves search, filters, sorting, pagination, selection, scroll position, and current tab when returning to a list
- Opens entity details in context (drawer, tabs, breadcrumbs like Client ├── Activity ├── Purchases) instead of sending the user to separate pages that break list context
- Reflects the user's mental model in navigation labels, grouped into Operations / Analysis / System rather than internal architecture

**Fails if:**
- Sends the user to a detached detail page and back to a freshly reset list
- Rebuilds filters as page-local state lost on every navigation
- Names nav items after database tables instead of user tasks

## Eval 9 — Sidebar from scratch

**Prompt:** "Diseñá la sidebar para un panel de gestión de links cortos."

**Expected behavior:**
- Pairs every nav item with an icon AND short label, explicitly noting this enables icon-only collapse.
- Sinks rare items (settings, help) to the bottom, separated from primary groups.
- Includes an active-state indicator and shows where badge chips/notification counts would sit.

**Fails if:**
- Flat ungrouped link dump with no active state.
- Labels only, making collapse impossible.

## Eval 10 — Chart fundamentals audit

**Prompt:** "Review the analytics section of this dashboard screenshot/code: two charts, no axis labels, one has a date picker."

**Expected behavior:**
- Flags missing grid lines/axis numbers before any aesthetic comment.
- Demands a consistent date-range selector shared by both charts.
- Questions any exotic chart type and suggests line/bar defaults with per-item identification (icons/labels).

**Fails if:**
- Only critiques colors or styling.
- Proposes a different range selector per chart.
