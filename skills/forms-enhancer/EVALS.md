# Evals — forms-enhancer

Seven scenarios for auditing whether output follows the Forms Enhancer skill. Each eval maps to a numbered section of SKILL.md and names the anti-pattern that counts as failure.

## Eval 1 — SaaS signup form

**Prompt:** "Crea el formulario de registro para mi SaaS. Queremos pedir nombre completo, email, contraseña, nombre de la empresa, tamaño de la empresa, teléfono, cargo, y cómo nos conoció."
**Expected behavior:**
- Applies the delete-or-defer test from section 1 (Every field earns its place): keeps only email + password (or equivalent minimum), defers company size, phone, role, and acquisition source to post-signup onboarding
- Orders remaining fields by section 2 rhythm (easy → commitment) and groups them by mental step
- Selects inputs per section 3 matrix: `type="email"` with autocomplete, password with `autocomplete="new-password"`
**Fails if:**
- Ships all 8 fields because "the client asked", without flagging drop-off cost or proposing deferral
- Uses placeholder-as-label or hides enum choices behind a select when ≤5 options exist

## Eval 2 — Validation timing refactor

**Prompt:** "Mi formulario valida cada campo mientras el usuario escribe y muestra errores en rojo desde la primera letra. Los usuarios se quejan. Arréglalo."
**Expected behavior:**
- Replaces keystroke validation with blur-first timing per section 5 (Validation strategy): validate on blur, re-validate on change after first error, never on first keystroke
- Keeps async checks debounced (~250–300ms) per section 16 instead of per-keypress API calls
- Clears an error the moment the corrected value becomes valid
**Fails if:**
- Moves all validation to submit-time only (swapping one extreme for the other)
- Validates on every change event even before the first blur/error

## Eval 3 — Error messages audit

**Prompt:** "Review these error strings: 'Invalid input', 'Error 422', 'This field is required', 'Password too weak'. Improve them."
**Expected behavior:**
- Rewrites each message to say what happened + how to fix it, with a concrete example in the message, per section 6 (Error messages) bad→good table
- Specifies focus moves to the first errored field and announcement via `aria-live`/`role="alert"` (section 6 + section 14)
- Confirms all typed values are preserved after failed submit
**Fails if:**
- Keeps any variant of "Invalid input" or exposes raw status codes ("Error 422") as user-facing copy
- Adds scolding tone ("You entered a wrong email again") or clears fields after failed submission

## Eval 4 — Checkout wizard split

**Prompt:** "Necesito un checkout de 7 pasos para una tienda online: cuenta, envío, método de envío, datos de facturación, tarjeta, cupón, confirmación."
**Expected behavior:**
- Regroups into 2–5 steps by user mental model per section 8 (Multi-step wizards), merging micro-steps like coupon into payment/shipping rather than giving each its own screen
- Specifies back navigation preserving all data, persisted partial progress, step-in-URL deep-linking, and a final review step with inline edit links
- Names the final button with the consequence ("Place order — $58.00")
**Fails if:**
- Builds 7 screens with a progress bar and no mention of data preservation on Back
- Omits the review step for this high-consequence flow or makes Back wipe earlier steps

## Eval 5 — Editor autosave and dirty state

**Prompt:** "Add autosave to our settings editor. Right now users edit JSON config and lose changes when they navigate away."
**Expected behavior:**
- Implements distinct visible states Saved / Saving… / Unsaved / Save failed per section 10 (Autosave & dirty state)
- Guards navigation away with an unsaved-changes prompt including SPA route guards
- Persists drafts so reload/crash restores work, and marks dirty state visibly (tab dot, title)
**Fails if:**
- Autosaves silently with no status indicator anywhere
- Blocks all navigation unconditionally, or loses edits on refresh despite claiming autosave

## Eval 6 — Mobile OTP and phone inputs

**Prompt:** "El login con código SMS y el campo de teléfono de mi app se llenan mal en móvil. El teclado muestra letras."
**Expected behavior:**
- Sets `inputmode="numeric"` + `autocomplete="one-time-code"` on the OTP field and `type="tel"`/`inputmode="tel"` + `autocomplete="tel"` on phone, per section 15 (Mobile input behavior) attribute table
- Avoids `type="number"` spinners for codes; keeps paste enabled; sets matching `enterkeyhint`
- Places primary action within thumb reach on mobile layout
**Fails if:**
- Relies on regex validation alone while the keyboard still opens alphabetical
- Builds a custom six-box OTP widget that blocks paste and autofill

## Eval 7 — Accessible form markup

**Prompt:** "Haz accesible este formulario de contacto. Ahora mismo los labels son placeholders y los errores aparecen en un div rojo abajo de todo."
**Expected behavior:**
- Converts placeholders to visible labels bound via `for`/`id`, links hints and errors with `aria-describedby`, sets `aria-invalid`, and gives the error summary `role="alert"` per section 14 (Accessibility)
- Pairs error color with icon/text (never color alone) and ensures ≥44px targets
- Moves focus to the error summary or first error on failed submit per section 13
**Fails if:**
- Fixes contrast of the red div but leaves labels as placeholders
- Adds aria labels duplicating visible text verbatim on decorative elements, or reports errors only visually with no live-region announcement
