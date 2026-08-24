---
name: forms-enhancer
description: Design, build, and review forms, validation flows, multi-step wizards, settings panels, filters, and inline editing experiences. Covers input selection, field anatomy, validation timing, error recovery, autosave and dirty-state handling, progressive disclosure of fields, keyboard interaction, accessibility, and mobile input behavior. Use when the user asks to create, improve, refactor, or audit any form, signup/login flow, checkout, wizard, settings page, search filters panel, or editable table.
---

# Forms Enhancer

## Objective

A form exists to collect correct data with minimum friction.

Every good form makes clear:

- Why each field exists.
- What a correct answer looks like.
- What went wrong and how to fix it.
- What is saved and what is not.
- What happens when the user commits.
- How to go back without losing work.

> **Every field must earn its place; every error must be recoverable.**

The quality of a form depends not on how many fields it has but on how few it needs and how safely it fails. Users forgive an ugly form. They never forgive lost input or a silent error.

---

## Ask first

Never invent missing context silently. Before building any form, check the brief for:

- What happens with the collected data and who consumes it.
- The stakes: throwaway signup vs. irreversible legal/checkout flow.
- Whether it is a single form, wizard, filter panel, or inline editing.
- Any auth, compliance, or integration requirements.

If answers are missing, ask up to 5 batched questions — never one at a time.

For every question, propose a smart default:

> If no answer: assume this default and proceed.

Silence or a bare "ok" means the defaults are accepted. Never ask what the provided code, data, screenshots, or repo context already answer.

---

## 1. Every field earns its place

Each field is a toll the user pays. Collect only what you need now.

Before adding any field, answer one question: **what decision or action uses this data?** If nothing consumes it, the field is decoration and decoration has a cost — abandonment grows with every field added.

The delete-or-defer test:

```text
Can we delete it?        no consumer today → remove
Can we defer it?         needed later → ask later (after signup, at first use)
Can we infer it?         derivable from other data → derive, never ask
Must we ask?             legal, billing, or blocking → keep, and justify in the hint
```

| Excuse for a field | Reality |
|---|---|
| "Might be useful someday" | Someday never funds the friction of today |
| "Marketing wants it" | Ask after activation, not before |
| "Everyone asks for phone" | Only if something calls or texts the user |
| "Confirm email field" | Paste errors are rarer than drop-off; rely on show-typed-value instead |

> The best field is the one the user never had to fill.

---

## 2. Ask in the right order

Order is rhythm: easy questions first, personal ones in the middle, commitment last.

- Open with fields that cost nothing: name, email. Momentum starts with answered questions.
- Place sensitive fields after trust is built — payment details come after value is shown, not before.
- Group by mental step ("who are you", "where do you live", "how do you pay"), not by database schema.
- One topic per section heading; users scan headings as checkpoints, so name them with plain nouns.
- Never interleave topics: address line 2 between password fields reads as a broken page.

```text
Wrong (schema order)            Right (mental-step order)
─────────────────────           ─────────────────────
Card number                     Email
Address line 1                  Password
First name                      Full name          ← who you are
Password                        ── divider ──
Company                         Address            ← where you are
Last name                       ── divider ──
Promo code                      Card + billing     ← how you pay
                                Promo code         ← optional, last, collapsed
```

> Every unanswered question is a small act of trust; spend trust in ascending order.

---

## 3. Input selection matrix

The input type is the first error message: the right control prevents mistakes instead of reporting them.

| Data type | Preferred input | Avoid |
|---|---|---|
| Email | `type="email"` + `autocomplete="email"` | Text input with hand-rolled regex |
| Long text | `<textarea>` that autosizes up to a max | Single-line input that truncates silently |
| Enum, ≤5 options | Radio group, all options visible | Select hiding 4 options behind 2 clicks |
| Enum, >5 options | Select or searchable combobox | Radio wall of 30 options |
| Date, constrained | Plain inputs or preset ranges ("last 30 days") | Custom calendar for a fixed window |
| Date, free-form | Native date picker | Three stacked selects (day/month/year) |
| Number | `inputmode="numeric"` on text input | `type="number"` spinners for ZIPs, card codes |
| Phone | `type="tel"`, `autocomplete="tel"`, format as typed | Free-text box plus strict regex scolding |
| Money | Decimal input with currency shown beside (`USD $`) | Spinner arrows on a salary field |
| Search | `<input type="search">` with clear button | Labeled "Go" text box |
| Boolean | Checkbox or switch — semantics differ | Switch inside a form submitted later |

Switch vs checkbox semantics:

```text
switch   effect applies immediately      → settings toggles, live preferences
checkbox value joins the submission      → "I agree to terms", multi-select lists
```

Using a switch inside a form that submits later makes users believe the change already happened.

> The right control answers most questions before validation ever runs.

---

## 4. Field anatomy

Every visible field carries four slots, each with exactly one job.

| Slot | Job | Rule |
|---|---|---|
| Label | Names the field permanently | Always visible above the input; never placeholder-only |
| Placeholder | Shows format or an example | Disappears on focus; must never carry instructions the user needs later |
| Hint | Explains constraints or why we ask | Persistent, tied via `aria-describedby`; quiet but readable contrast |
| Error | Reports failure and the fix | Appears next to the field only when there is a failure |

Required markers policy:

- Mark optional fields, not required ones, when most fields are required: a muted "(optional)" suffix beats forty red asterisks.
- If asterisks exist, define them once at the top of the form — a legend nobody can see is a legend that does not exist.

```text
Work email                          ← label, always visible
We only use this for receipts.      ← hint, persistent
[ you@company.com____________ ]     ← placeholder = example only
```

Placeholder-as-label fails three ways: it vanishes on focus, fails memory during review, and usually ships below contrast minimums.

> If removing all placeholders breaks the form, the labels were placeholders wearing a costume.

---

## 5. Validation strategy

Validation has a schedule. Running it early punishes typing; running it late punishes patience.

- Validate on **blur** — the user finished the field and expects a verdict.
- After the first error, re-validate **on change** — once flagged, a field should clear its own error the moment it becomes valid.
- Never validate on the first keystroke: "w is not a valid email" while typing is harassment, not help.
- Validate **near the problem** — message beside the field, not in a distant banner.
- Reserve submit-time summary for page-level failures: expired session, server rejection, or a long scrollable page where inline flags alone get lost.
- Async checks (username availability) run debounced after typing pauses, never on every keypress, and never block focus.

| Moment | Validate? | Why |
|---|---|---|
| First keystroke | No | No complete answer exists yet |
| Blur with content | Yes | Field is done; verdict expected |
| Change after an error | Yes | Clear the error the instant it is fixed |
| Debounced async | Yes | Availability checks need pause + patience |
| Submit | Yes, again | Server-side rules and full-form consistency |

```text
keystroke 1..n   silent
blur             "Enter a valid email, like you@company.com"
typing again     error clears as soon as format is valid
submit           re-check everything; server rules last word
```

> Validate when the user finishes a thought, not in the middle of having one.

---

## 6. Error messages

An error message does two jobs: say what happened, then say how to fix it. Scolding is not one of the jobs.

| Bad | Good |
|---|---|
| Invalid input | Enter your email in the format name@example.com |
| This field is required | Enter the address where your invoices go |
| Password too weak | Use at least 12 characters; add a number or symbol |
| Card declined | Your bank declined the charge — try another card or contact them |
| Value out of range | Delivery is available for ZIP codes in Quito; yours looks like Guayaquil |

Rules:

- Name the concrete format with an example inside the message itself.
- **Never** use "Invalid input", "Error", or the raw exception text as user-facing copy.
- Preserve everything the user typed — repopulate every field, mask passwords but keep them entered.
- Move focus to the first errored field after submit; place the summary link list above the form for long pages.
- Announce errors politely to assistive tech: `aria-live="polite"` on per-field regions, `role="alert"` on the summary.

```text
✗  "Invalid input"

✓  "Enter a phone number with area code,
    for example 099 123 4567."
```

> An error message is a repair manual written for a person holding the broken part.

---

## 7. Disabled submit vs always-enabled

Two schools. Pick deliberately, because each shapes behavior differently.

| Approach | Behavior | Cost |
|---|---|---|
| Disabled until valid | Blocks premature submits | User stares at a dead button with no reason given; screen-reader users hear nothing about what is missing |
| Always enabled + validate on click | Pressing reveals what is missing | One extra round-trip; needs solid error handling |

Prefer the enabled button for most forms:

- A dead button teaches nothing; a pressed button can teach everything.
- When errors exist, pressing shows the first error, focuses it, and explains the fix.
- Keep the disabled variant only for single-field forms where validity is obvious at a glance, and pair it with live helper text stating what is missing.

```text
Enabled pattern:
[ Create account ]  pressed with empty email
→ focus jumps to Email
→ "Enter your work email to continue."

Disabled pattern (allowed):
[ Subscribe ]
  helper: "Add a payment method to enable this button."
```

> A disabled button must still speak: if it cannot explain why it is asleep, it should be awake.

---

## 8. Multi-step wizards

One mental step per screen. A wizard is a promise that each screen is survivable.

- Split by the user's mental model ("shipping", "payment"), not by internal service boundaries.
- Show progress honestly: step names, current position, and estimated remaining effort beat abstract percent bars.
- Allow going back at any point **without losing data** — back navigation must restore every prior field exactly.
- Persist partial progress: draft to storage or server so refresh, crash, and tab-close lose nothing.
- End high-consequence flows (checkout, contract, deletion) with a review step showing every value with inline edit links.
- Support deep-linking: step lives in the URL (`/checkout/payment`) so reload and share land on the same step, and completed steps are revisitable.

```text
Step 2 of 4 · Shipping · Payment · Review
← Back            keeps everything from Step 1

Review step:
Ship to     Ana Ruiz, Av. Occidental 123   [ Edit ]
Pay with    Visa •••• 4242                 [ Edit ]
[ Place order — $58.00 ]
```

Rules of thumb:

- 2–5 steps; more steps means redesign the grouping, not the progress bar.
- Never spring a new required field in a later step that belongs conceptually in an earlier one.
- The final action names the consequence: "Place order — $58.00", not "Next".

> Each step should feel like the last one; a wizard that surprises is a funnel with a hole in it.

---

## 9. Inline editing

When users adjust existing structured data, a table/grid with inline editing beats a modal form per row.

Inline wins when: values are short, changes are frequent, context matters (users compare rows while editing). Modal forms win when: fields are many, interdependent, or validated as a unit.

| Save strategy | Mechanism | Best for |
|---|---|---|
| Save on blur | Commit when cell loses focus | High-frequency small edits; needs undo |
| Explicit save | Per-row Save/Cancel buttons | Rows with several related fields |
| Batch save | Staged edits, one Save bar for all | Review-and-approve workflows |

Rules:

- Optimistic UI: apply the edit instantly, reconcile quietly, roll back visibly on conflict.
- Every optimistic update pairs with undo (a toast with Undo, ≥5s) — speed without reversal is gambling.
- Conflict handling: if the row changed underneath, never overwrite silently. Show both versions and let the user choose.
- Keyboard path exists: Enter commits, Escape cancels, Tab advances to the next editable cell.

```text
Name            Role        Seats
Acme Ltd        Editor      12   ← click a cell to edit
                                         ↑ editing:
[ Acme Lt| ]  Enter=save  Esc=cancel
Toast: "Renamed to Acme Ltd.  [Undo]"
```

> Inline editing trades ceremony for speed — so it must pay back in undo and safety.

---

## 10. Autosave & dirty state

Users cannot see your save logic; they can only see its evidence. Show the evidence.

- Status must be explicit, persistent, and distinct: **Saved** / **Saving…** / **Unsaved changes** / **Save failed**, each visually different and announced to screen readers on transition.
- Mark dirty state where the change happened (dot on tab/document title) and where the exit is (`window.confirm` or inline guard on navigation).
- Warn before losing edits on navigation away, close, or reload — including SPA route guards; "unsaved changes" beats the browser default text.
- Autosave aggressively for low-stakes documents (notes, drafts); ask explicitly before saving high-stakes state (publishing, billing).
- Keep drafts: autosaved partial work survives logout, crash, and accidental close, and says so on return ("Draft restored from 14:32").

| State | Signal | Copy |
|---|---|---|
| Saved | Gray check, timestamp | Saved just now |
| Saving | Subtle spinner, non-blocking | Saving… |
| Unsaved | Amber dot on tab + near button | Unsaved changes |
| Failed | Red, retry affordance | Couldn't save — Retry |

```text
Pricing page editor                    ● unsaved
[ Save ]  saved just now               ← after save
Leaving with unsaved changes?
[ Stay ]  [ Leave without saving ]
```

> Autosave turns fear into flow — but only when the user can see that it happened.

---

## 11. Destructive & sensitive fields

Sensitive input protects two things: the data from observers, and the user from themselves.

Passwords:

- Ship show/hide toggle by default; masked passwords cause more typos than peeking causes leaks.
- Enable caps-lock warning inline.
- Use `autocomplete="new-password"` on signup and `current-password` on login; offer paste everywhere — blocking paste fights managers and loses to them anyway.

Critical changes (email, password, payout account, 2FA off) require re-authentication — recent password or fresh second factor — never trust the already-open session alone.

Irreversible actions use typing-to-confirm:

```text
Delete workspace "Nebula"?

This removes 34 projects and 128 members' access.
This action cannot be undone.

Type NEBULA to confirm
[ ____________________ ]   [ Cancel ]

[ Delete workspace ]   ← stays disabled until exact match
```

Rules:

- Confirmation names the consequence in counts ("34 projects"), never generic "are you sure".
- Destructive buttons sit far from primary flows and never double as the visual primary action.

> The cost of confirming must match the cost of regret.

---

## 12. Filters as forms

A filters panel is a form whose result set is the submission — treat the URL as its source of truth.

- Every filter state serializes to the URL (`?status=open&owner=ana&sort=-updated`): shareable, restorable, back-button-safe.
- Changing a filter updates the URL immediately (replace-state for typing, push-state for discrete picks).
- Applied filters render as removable chips near results — the chips are the receipt of what the URL promised.
- Provide Clear all, and show an active count badge on collapsed panels.
- Results count updates live or on Apply — decide per result cost: cheap search applies as-you-type; expensive reports apply on button.

```text
Filters (3)                        [ Clear all ]
( status: open × ) ( owner: ana × ) ( label: bug × )

128 results · sorted by recently updated

/status?status=open&owner=ana&label=bug&sort=-updated
```

Rules:

- Never leave filter UI state and URL state able to disagree; one drives the other, always the URL.
- Empty result sets explain which filter starved them and offer removal links.

> If a filtered view cannot be pasted into chat and reopened identically, the filter state was never real.

---

## 13. Keyboard & focus

Keyboard is not an accessibility garnish; it is the power-user interface and the test harness for focus logic.

| Context | Key | Behavior |
|---|---|---|
| Single-input form (search, promo code) | Enter | Submits |
| Multi-line textarea | Cmd/Ctrl+Enter | Submits; bare Enter inserts newline |
| Any page | Tab / Shift+Tab | Logical DOM order matching visual order |
| Modal containing a form | Tab | Cycles inside the modal; focus trapped |
| Modal close | Esc | Closes, returns focus to trigger |
| Submit success | — | Focus moves to confirmation heading |
| Submit failure | — | Focus moves to error summary or first error |
| Long pages | Skip link | First Tab hit jumps past nav to main/form |

Rules:

- Focus follows consequence: after acting, the cursor lands where the outcome lives — confirmation, error, or next field.
- Never steal focus on a timer; move it only in response to the user's action.
- Visible focus ring on every interactive element; removing outlines without replacement is a defect.

```text
Login page:
[ email ] Tab→ [password] Tab→ [Show] Tab→ [Sign in]
Enter anywhere in the form = Sign in
Failure: focus → "Sign-in failed" summary, then email field.
```

> If the keyboard path gets lost, so does the user's sense of place — focus is the cursor of trust.

---

## 14. Accessibility

Accessible forms are mostly correct forms: the semantics that help screen readers also prevent bugs.

Checklist-grade requirements:

- Every label bound via `for`/`id` — clicking the label focuses the input, and screen readers announce it on entry.
- Hints and errors linked with `aria-describedby` so they are read with the field, not stranded nearby.
- Invalid fields set `aria-invalid="true"`.
- Page-level error summary uses `role="alert"` (or is focused) so failures are announced, not just painted.
- Touch targets ≥44×44px — checkboxes, radios, and their labels alike.
- Never color alone: error states pair icon + text + border, not just a red tint.

```html
<label for="email">Work email</label>
<p id="email-hint">We only send receipts.</p>
<input id="email" type="email" autocomplete="email"
       aria-describedby="email-hint email-error"
       aria-invalid="true">
<p id="email-error">Enter an email like name@example.com.</p>
```

Rules:

- Group related controls with `fieldset`/`legend` (radio groups especially) — legends give each option its question context.
- Announce dynamic status changes (saved, results count) through polite live regions rather than hoping the user watches.
- Test the whole flow with the screen reader once per release, not once per lifetime.

> A form that works only with a mouse is a form that works by accident.

---

## 15. Mobile input behavior

On mobile, attributes are UX: the virtual keyboard, autocomplete, and picker are chosen by markup, not design.

| Attribute | Value | Effect |
|---|---|---|
| `inputmode` | `"numeric"` | Number pad — OTP, ZIP, card numbers |
| `inputmode` | `"decimal"` | Keypad with decimal separator — price, weight |
| `inputmode` | `"tel"` | Phone pad |
| `inputmode` | `"email"` / `"url"` | @ / . / .com keys surfaced |
| `autocomplete` | `"one-time-code"` | SMS codes offered above the keyboard |
| `autocomplete` | `"cc-number"`, `"cc-exp"` | Wallet autofill for checkout |
| `enterkeyhint` | `"go"`, `"search"`, `"next"` | Action key matches the next move |
| `autocapitalize`/`autocorrect` | Off | Emails, codes, usernames |

Rules:

- Native pickers beat custom ones: platform date, time, and select sheets ship accessibility, gestures, and familiarity for free.
- Numeric keypad for numeric fields — `type="number"` alone does not guarantee it across browsers; set `inputmode`.
- Primary action within thumb reach: bottom sheet or bottom-fixed bar on tall forms; never a lone button at the very top scroll.
- Avoid mid-form sticky headers that collapse the visible keyboard region.

```text
OTP field:
<input inputmode="numeric" autocomplete="one-time-code"
       pattern="[0-9]*" maxlength="6">

Result: number pad opens, SMS code floats as a suggestion,
no letters possible, paste allowed.
```

> On phones the keyboard is half the interface — and markup decides which half appears.

---

## 16. Performance perception

Perceived speed is a design property. Forms feel fast when feedback arrives before truth does.

| Wait | Pattern |
|---|---|
| Instant | Optimistic enablement — allow typing/selection while a section loads |
| <300ms | Inline validation response feels immediate; debounce ~250–300ms |
| 300ms–1s | Button enters loading state; width locked; repeat clicks ignored |
| >1s | Skeleton or named progress for slow sections; keep completed fields interactive |

Rules:

- Debounce expensive validation (availability, API-backed checks); validate cheap formats locally and instantly.
- Disable double-submit: first press locks the button into loading; network layer dedupes anyway.
- Never freeze the whole form because one section loads — isolate slow zones behind skeletons, keep finished fields editable.
- Prefetch the next wizard step's data while the current one is being filled.

```text
[ Checking username… ]        ← button loading, width locked
acme-co ✓ available           ← debounced result lands inline
```

> Users judge latency by the first 100ms of response, not by the total.

---

## 17. Anti-patterns

Recurring defects, each with its repair.

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| Placeholder-as-label | Vanishes on focus; fails review and contrast | Permanent visible labels |
| Reset button next to submit | One slip erases a filled form | Delete the reset button |
| Captcha-first | Taxes everyone to stop a few bots | Invisible checks; challenge only on suspicion |
| 30-field registration | Asks for a marriage license before a hello | Ask for email+password now; profile later |
| Silent validation failure | Submit clicks, nothing happens, no message | Always respond: success, or focused errors |
| Losing data on back-navigation | Wizard Back wipes step 1 | Restore state from persisted draft |
| Select for a known 3-option enum | Two extra clicks to hide three choices | Radio group, all visible |
| Validation only on submit | All pain arrives at once, at the end | Validate on blur; re-validate on change |
| Confirm-password field | Doubles typing, catches little | Show/hide toggle instead |
| Unlabeled required asterisk | Red stars with no legend | "(optional)" markers or a real legend |

> An anti-pattern survives because it survives code review — not because anyone chose it twice.

---

## 18. Pre-flight checklist

Run before calling any form done:

- [ ] Every field justified — a named consumer for its data
- [ ] Labels always visible; hints and placeholders doing separate jobs
- [ ] Validation timing defined: blur first, change after error, submit last
- [ ] Every error message says what happened + how to fix, with an example
- [ ] Typed input preserved through every failure path
- [ ] Dirty state handled: status shown, navigation guarded, drafts persist
- [ ] Keyboard path walks end-to-end: tab order, Enter, focus on success/error
- [ ] Mobile keyboards correct: `inputmode`, `autocomplete`, `enterkeyhint`
- [ ] Labels bound, `aria-describedby` wired, targets ≥44px, not color-alone
- [ ] Wizards: back preserves data, steps deep-link, review before commit

---

## 19. Final principles

Hard rules. When a decision conflicts with one of these, the principle wins.

1. Never lose user input — through errors, back-navigation, refresh, or crashes.
2. Every field earns its place; delete, defer, or infer before asking.
3. Errors teach, they don't scold — say what happened and how to fix it.
4. The submit button is a contract: pressing it must work or explain why not.
5. Validate when a field is done, not while it is being born.
6. The right input control prevents most errors before validation runs.
7. State must be visible: saved, saving, unsaved, failed — never guessed.
8. Going back must never mean starting over.
9. Irreversible actions require proportionate friction, naming the exact consequence.
10. The form must survive keyboard-only, screen-reader, and small-screen passes before shipping.

> A form succeeds when the user forgets it was a form — correct data arrived, nothing was lost, and no question was wasted.
