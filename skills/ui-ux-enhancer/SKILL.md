---
name: ui-ux-enhancer
description: Design interfaces that visually communicate their own behavior through affordances, signifiers, visual hierarchy, grids, spacing, typography, color, dark mode, shadows, icons, buttons, states, feedback, microinteractions, overlays, art direction, atmospheric depth, composition variety, and motion choreography. Reduces reliance on explicit instructions by making every element self-explanatory. Use when designing, building, reviewing, or polishing any user interface, component library, web app screen, landing page, or interactive product UI.
---

# UI/UX Enhancer

## Objective

Design interfaces that communicate how they work visually, reducing the need for explicit instructions.

A good interface lets users understand at a glance:

- What is interactive.
- What each element does.
- What is selected.
- What is active.
- What is disabled.
- What just happened.
- Which information matters most.
- Which elements are related.
- What can be done next.

> **The interface must explain its behavior through its design.**

The quality of an interface depends not only on colors, components, shadows, or aesthetics. It depends on whether users can perceive, understand, act, and receive a response without unnecessary effort.

---

## Ask first

Never invent missing context silently. Before designing any interface, check the brief for:

- Product type and platform (web app, mobile, marketing site).
- Who the primary users are and what they must accomplish.
- Existing design system, tokens, or brand constraints.
- Scope: single component, full screen, or whole flow.

If answers are missing, ask up to 5 batched questions — never one at a time.

For every question, propose a smart default:

> If no answer: assume this default and proceed.

Silence or a bare "ok" means the defaults are accepted. Never ask what the provided code, data, screenshots, or repo context already answer.

---

## 1. Affordances

An **affordance** is what an element allows the user to do. Strong affordances make the possible action obvious before any interaction happens.

| Element | Affordance |
|---|---|
| Button | Press |
| Input | Type |
| Checkbox | Toggle |
| Switch | Flip |
| Slider | Drag |
| Link | Navigate |
| Interactive card | Open |
| Handle | Drag |
| Select | Choose |
| Tab | Switch content |

### Principle

> An interactive element must never look like static content.

Treatments that build affordance:

```text
Shape       contained, rounded bodies read as pressable
Depth       subtle shadow or raised surface reads as liftable
Cursor      pointer on clickable, text caret on editable, grab on draggable
Motion      a slight hover response hints interactivity before any click
Convention  follow platform defaults instead of inventing new shapes
```

Users must be able to infer what they can do with an element without reading an explanation. If the design needs the words "click here", the design has already failed.

---

## 2. Signifiers

A **signifier** is a visual signal that tells the user how an element works or which state it is in.

Common signifiers:

- Hover.
- Focus.
- Active.
- Pressed.
- Selected.
- Disabled.
- Highlight.
- Border.
- Background.
- Underline.
- Icon.
- Cursor.
- Tooltip.
- Chevron.
- Loading indicator.
- Color change.
- Font-weight change.

### Example: tabs

```text
[ Drinks ]    Food      Desserts
━━━━━━━━━━
  ▲ active tab, communicated by three stacked signals:
    1. background fill on the pill
    2. bold font-weight on the label
    3. accent border-bottom under the pill

Food and Desserts stay muted, flat, and unmarked — clearly inactive.
```

Stack at least two signifiers on the active item so the selection survives color blindness, dark mode, and low-quality screens.

---

## 3. Visual hierarchy

Hierarchy decides what users see first, second, and last — before they choose what to care about.

- Exactly one primary action per view.
- Size, weight, and contrast must all agree on importance; conflicting signals cancel out.
- Critical information goes at the top of the scan path (top-left in LTR layouts, top-right in RTL).
- Group related items; separate unrelated ones with space, not only with lines.
- Build hierarchy with whitespace first; add decoration only if it is still unclear.

| Level | Tools |
|---|---|
| Primary | Large size, high contrast, filled component |
| Secondary | Medium size, standard contrast, outlined component |
| Tertiary | Standard size, muted color, plain text link |
| Metadata | Small size, lowest contrast, caption |

```text
INVOICE #2041                     ← metadata: small, muted
Payment overdue                   ← headline: large, heavy
Your card was declined on ...     ← supporting: normal, muted
[ Update payment method ]         ← primary: filled, high contrast
        Manage billing            ← tertiary: quiet text link
```

> If everything is emphasized, nothing is emphasized.

---

## 4. Grids & layout

Alignment is invisible when correct and obvious when wrong.

- Compose on a column grid: typically 4 columns on mobile, 8–12 on tablet and desktop.
- Keep gutters and page margins consistent across every breakpoint.
- Cap text measure at 45–75 characters per line regardless of container width.
- Align section edges to shared vertical lines; ragged edges read as broken.
- Prefer fixed max-width containers over full-bleed percentages for content areas.
- Breakpoints change the grid, not the logic: same order, same grouping, fewer columns.

```text
Desktop (12 cols)                    Mobile (4 cols)
| 3 cols nav || 9 cols content |    | 4 cols content |
                                    [ nav collapses below ]
```

> Misalignment is the cheapest bug to fix and the loudest one to ship.

---

## 5. Spacing

Space is the primary grouping tool. Treat it as data, not as leftovers.

- Use one spacing scale, typically base 4px: 4, 8, 12, 16, 24, 32, 48, 64, 96.
- Related items sit closer than unrelated items — proximity implies relationship.
- Inner padding grows slower than outer gaps: component padding < gap between components < gap between sections.
- Never pick arbitrary values; round to the nearest scale step.
- When in doubt, use more space. Crowding is harder to repair later than emptiness.

```text
label ↔ field          4–8px     one unit, tightly coupled
field ↔ field          16–24px   within a form group
group ↔ group          32–48px   between form sections
section ↔ section      64–96px   between page regions
```

> Whitespace is not empty; it is the structure users navigate by.

---

## 6. Typography

Type carries most of the hierarchical work in a clean interface.

- Maximum two typefaces: one for display and headings, one for body. One is often enough.
- Define a fixed type scale and never freestyle sizes between steps.
- Body text starts at 16px on the web; line-height 1.4–1.6 for body, 1.1–1.3 for headings.
- Differentiate levels with weight and color before inflating size.
- Sentence case for buttons, labels, and menus; reserve ALL CAPS for tiny overline labels only.

```text
Display   48/56   Bold       marketing hero only
H1        32/40   Bold       page titles
H2        24/32   Semibold   section titles
H3        18/28   Semibold   card titles
Body      16/24   Regular    default reading text
Caption   13/18   Regular    metadata, helper text
```

> Users read the hierarchy before they read the words.

---

## 7. Color

Color sets mood, directs attention, and encodes meaning — in that order of fragility.

- Distribute roughly 60% neutral, 30% brand, 10% accent across any screen.
- Reserve semantic hues strictly: green = success, amber = warning, red = danger, blue = information.
- Meet contrast minimums: 4.5:1 for body text, 3:1 for large text and UI component boundaries.
- Never let color be the only carrier of meaning (see States).
- Build tints and shades from your core hues instead of introducing new ones per screen.

| Role | Hue | Used for |
|---|---|---|
| Neutral | Gray scale | Surfaces, text, borders, dividers |
| Brand | Primary | Key actions, links, active highlights |
| Success | Green | Confirmations, healthy status |
| Warning | Amber | Caution, recoverable risk |
| Danger | Red | Errors, destructive actions |

> Color is the fastest channel to the user — and the first one lost to accessibility constraints.

---

## 8. Dark mode

Dark mode is a re-mapped theme, not an inverted palette.

- Re-tune every token by hand; mechanical hex swaps produce mud.
- Desaturate brand and accent colors; saturated hues vibrate painfully against dark surfaces.
- Communicate elevation with lighter surface tones, because shadows barely register on dark backgrounds.
- Avoid pure black backgrounds and pure white text; soft darks and off-whites reduce halation.
- Borders get lighter as shadows get weaker; surface steps replace depth cues.

```text
Token map (light → dark)
background      #FFFFFF → #101216
surface         #F5F6F8 → #171B21
border          #E2E4E9 → rgba(255,255,255,0.10)
text primary    #111418 → #E8EAED
text muted      #5A6068 → #9AA0A6
primary action  #2563EB → #60A5FA
```

> In light mode elevation casts shadows; in dark mode elevation emits light.

---

## 9. Shadows & elevation

Shadows tell users which layer is talking to them.

- Maintain one elevation ladder for the whole product and reuse it everywhere.
- Higher elevation means larger blur, larger offset, lower opacity — never simply darker.
- Pair shadows with a hairline border so cards stay crisp on any background.
- Anything that overlaps content must visibly float above it.
- Raising elevation on hover signals "this can be picked up"; lowering it on press signals "this was pushed".

| Level | Element | Recipe |
|---|---|---|
| 0 | Page background | None |
| 1 | Cards, sticky header | `0 1px 3px rgba(0,0,0,.10)` |
| 2 | Dropdown, popover | `0 4px 12px rgba(0,0,0,.14)` |
| 3 | Modal, drawer | `0 12px 32px rgba(0,0,0,.18)` |
| 4 | Toast | `0 8px 24px rgba(0,0,0,.20)` |

```text
page < card < dropdown < drawer/modal < toast
lowest ─────────────────────────────▶ highest
```

> If two layers overlap and the user cannot tell which is on top, the shadow failed.

---

## 10. Icons

Icons compress meaning; sloppy icons compress it into confusion.

- One icon set per product: same grid, stroke width, corner radius, and style.
- Pair icons with text labels unless the symbol is truly universal (search, close, settings).
- Keep consistent optical size; align glyphs to the pixel grid to avoid blur.
- Provide touch targets of at least 44×44px even when the glyph itself is 20–24px.
- Follow platform conventions for meaning; creativity belongs in shape refinement, not semantics.

| Rule | Why |
|---|---|
| Same stroke weight everywhere | Mixed weights read as different products |
| Label unfamiliar icons | Unlabeled icons force guessing |
| No decorative icons inside task flows | Decoration dilutes functional signals |
| Legible at 16px | Detail that dies when small should not exist |

> An unlabeled, unconventional icon is a puzzle the user never agreed to solve.

---

## 11. Buttons

Buttons are the contract between what the interface promises and what the user intends.

- Exactly one filled primary button per view.
- Label with concrete verbs: "Save changes" beats "OK"; "Delete project" beats "Confirm".
- Destructive actions get distinct styling plus a confirmation step that names the consequence.
- Minimum height around 40–44px with generous horizontal padding; the whole area must be clickable.
- Place the primary action at the end of the reading flow (right side in LTR dialogs) and stay consistent product-wide.

| Variant | Style | Use |
|---|---|---|
| Primary | Filled, highest contrast | The one main action |
| Secondary | Outlined or tonal | Supporting alternatives |
| Tertiary | Text or ghost | Low-stakes choices, escape routes |
| Destructive | Red palette | Irreversible or harmful actions |

```text
[ Cancel ]   [ Save changes ]     secondary left, primary right
[ Delete account ]                destructive: red, isolated, confirmed
```

> The primary button should be findable in under one second, even by a scanning eye.

---

## 12. States

Every interactive element is a small machine with eight gears. Ship all of them.

| State | Required signal |
|---|---|
| Default | Resting appearance with visible affordance |
| Hover | Subtle background or lightness shift, pointer cursor |
| Focus | Visible ring for keyboard users — never removed without replacement |
| Active / pressed | Slightly darker shade or scale-down; confirms the click landed |
| Disabled | Reduced opacity, blocked cursor, no hover effects; explain why via helper text when possible |
| Loading | Spinner or progress inside the trigger, width locked, repeat clicks ignored |
| Empty | Friendly placeholder plus the next action — never a silent void |
| Error | Message adjacent to its cause, input preserved, focus moves to the first error |

```text
[ Save ]            default
[ Save ]            hover: background lightens
[ Save ]            focus: 2px accent ring
[ Save ]            pressed: shade darkens briefly
[ Saving... ]       loading: label swaps for spinner, width locked
[ Save ]            disabled: 40% opacity, ignores all input
```

> A missing state is a bug that ships quietly and screams in production.

---

## 13. Feedback

Unacknowledged actions feel broken, even when they worked.

- Acknowledge every interaction within ~100ms: hover states, pressed effects, optimistic updates.
- Match the pattern to the wait: instant state changes for fast results, toasts for seconds, progress bars with percentages for longer waits.
- Keep success feedback brief; make error feedback specific and offer the next step.
- Report failure loudly; silence converts minor errors into lost trust.
- Deliver feedback near the point of interaction, not in a distant log or notification center.

| Wait time | Pattern |
|---|---|
| Instant | Inline state change, pressed effect |
| Under ~4s | Toast or inline confirmation |
| 4s and longer | Progress bar with percent or named steps |
| Unknown duration | Spinner for short waits, skeleton loader plus honest copy otherwise |

```text
[ Upload report ]
  ────────────────────────────  62%   uploading report.pdf
```

> Silence after an action reads as failure — even when it succeeded.

---

## 14. Microinteractions

Motion earns its place by explaining something static pixels cannot.

- Animate to confirm actions, reveal relationships, or direct attention — never to decorate.
- Micro-feedback runs 100–200ms; transitions 200–400ms; anything past 500ms feels laggy.
- Ease-out for entrances, ease-in for exits, springs for drag gestures and playful toggles.
- Honor `prefers-reduced-motion`: swap movement for opacity changes.
- One moving thing per moment; simultaneous animations compete and none win.

| Interaction | Motion | Duration |
|---|---|---|
| Button press | Scale to 0.97 | ~100ms |
| Modal open | Fade plus scale from 0.96 | ~250ms |
| Toggle switch | Knob slide | ~150ms |
| Accordion | Height expand | ~250ms |
| Skeleton load | Shimmer loop | Until replaced |

> Motion is a sentence: it has a subject (the element), a verb (the change), and a reason.

---

## 15. Overlays

Overlays interrupt. Choose the lightest interruption that solves the problem.

- Pick by purpose, not habit: modal to block and focus, drawer for side context, popover for anchored detail, tooltip for hints, toast for results.
- Modals: single task, obvious close affordance, ESC and backdrop-click dismissal, focus trapped inside, background scroll locked, focus returned to the trigger on close.
- Drawers: editing in context; push or cover content without losing orientation.
- Popovers: anchored to their trigger, dismissed by clicking outside, never host critical flows.
- Tooltips: appear after ~300ms delay, vanish on pointer move, hold only clarifications — nothing the user must act on.
- Toasts: auto-dismiss after 4–6s, manually dismissible, stacked in one corner, never the sole home of important news.

| Overlay | Purpose | Lifetime |
|---|---|---|
| Modal | Blocking decisions | Until resolved |
| Drawer | Side-panel context or editing | Until closed |
| Popover | On-demand detail | Click outside |
| Tooltip | Hover clarification | Auto on leave |
| Toast | Result confirmation | Auto-dismiss 4–6s |

```text
z-order ladder:
page (0) → sticky bar (10) → drawer (30) → modal + backdrop (50) → toast (70)
```

> An overlay steals the user's attention; earn it back with an obvious way out.

---

## 16. Art direction & visual identity

Restraint is not anonymity. Clean does not mean generic.

- Choose a typographic voice: pair a characterful display treatment with a neutral body. Display sizes earn personality; body text stays quiet.
- Commit to a point of view — editorial, terminal, soft-utility, brutalist. Every screen should be attributable to its product.
- Include one memorable element per view: an oversized numeral, a thick rule, a mono metadata label, a distinctive radius.
- Default-look tells: default system styling everywhere, one font weight, everything centered, stock blue links, uniform card rows.

> If five different startups could have shipped your screen unchanged, it has no identity.

---

## 17. Depth, light & atmosphere

Flat is a choice, not a default.

- Build depth in layers: page background < surface < raised. Differentiate with surface steps and border lightness, not just bigger shadows.
- Ambient accents: at most two large, very low-opacity radial glows or gradient meshes anchored to the composition (behind the hero, behind the featured item). Never mid-page, never saturated.
- Texture beats plastic: 2–4% grain/noise over large flat areas kills gradient banding and the vector-plastic look.
- Glass (blur + translucent fill) only over rich backgrounds; blur over plain color shows nothing and reads as fog.
- Use rgba borders instead of solid grays — they stay correct across themes.

### Dark mode depth

Dark mode is not inverted light: reduce saturation of accents slightly, separate surfaces by steps plus borders, keep shadows subtle — in dark themes light does the separating, not shadow.

---

## 18. Composition variety

Uniformity reads as template. Rhythm reads as designed.

- Vary section composition down the page: full-width statement → split layout → dense grid → quiet interlude. Never repeat the same container rhythm twice in a row.
- Use bento grids when items differ in importance: one dominant cell, supporting cells with varied spans. Equal thirds means nothing is important.
- Break symmetry deliberately against strong alignment lines elsewhere — asymmetry needs an anchor.
- Exploit scale contrast: very large display next to small mono caption creates energy safe layouts lack.
- Add second-read moments: footnote annotations, hover-revealed context, mono metadata that rewards attention.

> Equal boxes make equal impressions.

---

## 19. Motion choreography

Motion is a choreographed scene, not sprinkles.

- Entrance choreography: staggered children in reading order, 40–80ms steps, ease-out, short travel (8–24px).
- Scroll-linked reveals fire once on viewport entry. Never re-trigger on scroll-up.
- Hover moves something real: lift + shadow grow, arrow nudge, media scale 1.02–1.05. Nothing wiggles without meaning.
- Duration ladder: micro 120–160ms, standard 200ms, dramatic 400ms maximum. Exponential-out easings.
- Under prefers-reduced-motion: swap transforms for opacity, remove parallax entirely.

> Remove every transition and the layout must still communicate everything.

---

## 20. Design workflow checklist

Run this pre-flight before calling any screen done:

- [ ] Every interactive element shows an affordance plus hover and focus states
- [ ] Exactly one primary action per view
- [ ] Contrast passes: 4.5:1 body text, 3:1 large text and UI boundaries
- [ ] Spacing values come from the scale; edges align to the grid
- [ ] All eight states designed: default, hover, focus, active, disabled, loading, empty, error
- [ ] Every action produces feedback; destructive paths ask for confirmation
- [ ] Overlays trap focus, close via ESC and backdrop, restore focus on exit
- [ ] Dark mode is re-mapped, not inverted; `prefers-reduced-motion` respected
- [ ] Verified at the smallest supported viewport and with keyboard only
- [ ] Nothing on screen exists purely for decoration

---

## 21. Audit mode

Use when reviewing an EXISTING interface rather than designing a new one.

### Process

1. Inventory every screen/state you can see.
2. Score each dimension 0–10.
3. Log findings tagged blocker / major / minor.
4. Deliver fixes ordered by impact ÷ effort.

Fourteen dimensions × 10 = 140 raw points; normalize the total to 100 before applying verdicts.

### Scoring rubric

| Dimension | Question | Score |
|---|---|---|
| Affordance clarity | Does every interactive element look interactive before any interaction? | /10 |
| Signifier coverage | Do active and selected items stack at least two signifiers? | /10 |
| Visual hierarchy | Does exactly one primary action dominate each view? | /10 |
| Grid alignment | Do edges align to shared column lines across breakpoints? | /10 |
| Spacing consistency | Do all values come from one spacing scale? | /10 |
| Typography scale discipline | Are sizes drawn from a fixed type scale, never freestyled? | /10 |
| Color semantics & contrast | Are semantic hues reserved and contrast minimums met? | /10 |
| Dark mode integrity | Is dark mode re-mapped token by token, not inverted? | /10 |
| Elevation logic | Does the shadow ladder match the actual z-order? | /10 |
| Icon clarity | One set per product, labeled when unfamiliar, legible at 16px? | /10 |
| Button system coherence | One filled primary per view, concrete verb labels? | /10 |
| State coverage | Do all eight states exist on every interactive element? | /10 |
| Microinteraction purpose | Does motion explain rather than decorate, honoring reduced motion? | /10 |
| Overlay appropriateness | Is the lightest interruption chosen, with an obvious way out? | /10 |

### Verdict thresholds

```text
0–39   Redesign the core flow
40–69  Targeted fixes
70–100 Polish only
```

### Finding format

```text
[MAJOR] Settings form — focus ring removed on all inputs
Score impact: -3 (State coverage)
Fix: Restore a visible 2px accent focus ring
Effort: Low
```

Order the final report by impact ÷ effort, highest first.

---

## 22. Final principles

Hard rules. When a design choice conflicts with one of these, the principle wins.

1. If it looks clickable, it must be clickable — and nothing else should look clickable.
2. Never communicate state with color alone.
3. One primary action per view.
4. Every interactive element defines all eight states.
5. Every action receives feedback within 100ms.
6. Same element, same look, same behavior — everywhere.
7. Clarity outranks aesthetics; aesthetics exist to serve clarity.
8. Remove before you add; every element must justify its existence.
9. The user's attention is borrowed — overlays, motion, and color must repay it.
10. Test with keyboard, dark mode, reduced motion, and the smallest viewport before shipping.

> The interface must explain its behavior through its design. Anything it cannot explain on its own is a defect.
