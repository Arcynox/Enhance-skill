# Enhance Skills

A curated collection of professional design skills for AI coding agents. Each skill teaches an agent how to design, audit, and polish interfaces with the judgment of a senior product designer — not just generate pretty screens.

## Skills

| Skill | Focus |
|---|---|
| [`dashboard-enhancer`](skills/dashboard-enhancer/SKILL.md) | Dashboards, admin panels, backoffices, CRMs, ERPs, analytics screens. Data-driven UI, information hierarchy, progressive disclosure, complete component states, accessibility. |
| [`ui-ux-enhancer`](skills/ui-ux-enhancer/SKILL.md) | General interface design. Affordances, signifiers, grids, spacing, typography, color, dark mode, shadows, buttons, states, microinteractions, overlays. |
| [`forms-enhancer`](skills/forms-enhancer/SKILL.md) | Forms, validation, wizards, settings panels, filters, inline editing. Input selection, validation timing, error recovery, dirty state, keyboard and mobile input behavior. |

Every skill includes an **Audit mode** section — a 0–10 scoring rubric for reviewing existing UI — and an **`EVALS.md`** with test prompts to verify the skill actually changes agent behavior.

## Repository structure

```
.
├── README.md
├── LICENSE
├── .github/
│   ├── scripts/validate_skills.py   # structure + frontmatter validator
│   └── workflows/lint.yml           # CI: validator + markdownlint
└── skills/
    ├── dashboard-enhancer/
    │   ├── SKILL.md
    │   └── EVALS.md
    ├── ui-ux-enhancer/
    │   ├── SKILL.md
    │   └── EVALS.md
    └── forms-enhancer/
        ├── SKILL.md
        └── EVALS.md
```

Each skill lives in its own directory as `SKILL.md` with valid frontmatter (`name` matching the directory, `description` including trigger conditions), following the [Agent Skills](https://agentskills.io) convention used by Claude Code, opencode, and other agent runtimes.

## Installation

Copy a skill directory into your agent's skills folder:

```bash
# Claude Code (user-level)
cp -r skills/dashboard-enhancer ~/.claude/skills/

# Claude Code (project-level)
cp -r skills/dashboard-enhancer .claude/skills/

# opencode (user-level)
cp -r skills/ui-ux-enhancer ~/.config/opencode/skills/

# Generic agent runtimes (~/.agents/skills/)
cp -r skills/<skill-name> ~/.agents/skills/
```

## Usage

Skills activate automatically when your agent detects a matching task — designing a dashboard, reviewing a screen, polishing a component. You can also invoke them explicitly by asking the agent to apply the skill by name, or ask for an **audit** ("audit this admin panel with dashboard-enhancer") to get a scored rubric review instead of a redesign.

## Examples

[`examples/landing/index.html`](examples/landing/index.html) — a self-contained landing page built by applying all three skills at once: ui-ux-enhancer (hierarchy, states, dark mode, microinteractions), forms-enhancer (live validation, error recovery, dirty state), and dashboard-enhancer (KPIs with context, right-aligned numbers, table interaction). Open it in a browser and toggle the theme.

<h2>Realstate CRM example</h2>

![`Main dashboard`](examples/landing/1.png)
![`Main dashboard`](examples/landing/2.png)
![`Main dashboard`](examples/landing/3.png)
![`Main dashboard`](examples/landing/4.png)
![`Main dashboard`](examples/landing/5.png)
![`Main dashboard`](examples/landing/6.png)

## Validation

Skills are validated in CI on every push. To run locally:

```bash
python3 .github/scripts/validate_skills.py
```

Checks: frontmatter parses, `name` matches directory (kebab-case), description length, balanced code fences, `EVALS.md` present.

## Contributing

New skills must follow the same conventions:

1. One directory per skill under `skills/`, named in kebab-case.
2. `SKILL.md` with valid frontmatter: `name` identical to directory name, third-person `description` stating what it does **and when to use it**.
3. An `EVALS.md` with test prompts mapping each skill principle to expected agent behavior.
4. An **Ask first** section right after the objective: check the brief, batch up to 5 clarifying questions, and propose a smart default for each so silence never blocks work.
5. Content in English, written as direct, assertive rules — not prose.
6. Examples use realistic UI copy, not placeholders.

CI enforces 1, 2 and part of 3 (presence) via `.github/scripts/validate_skills.py`.

## License

[MIT](LICENSE)
