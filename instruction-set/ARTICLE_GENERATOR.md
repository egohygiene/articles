# Article Generator — Guidelines

A clear, repeatable process for generating articles in this repository from thesis to published draft.

---

## Purpose

This guide defines the standard process for moving an article from a defined thesis and scope to a complete draft ready for review. It applies to every article in this repository.

---

## Article Lifecycle

Each article passes through four phases:

| Phase | Output | Location |
|-------|--------|----------|
| 1. Thesis and Scope | `THESIS.md` | `articles/YYYY-MM-slug/` |
| 2. Drafting | `Draft.md` | `articles/YYYY-MM-slug/` |
| 3. Revision | Updated `Draft.md` | `articles/YYYY-MM-slug/` |
| 4. Publication | `published.md` | `articles/YYYY-MM-slug/` |

Do not begin a phase until the previous phase is complete and committed.

---

## Phase 1 — Thesis and Scope

Before writing a single sentence of the article body, produce a `THESIS.md` file in the article folder.

### Required sections

1. **Working Title** — A clear, descriptive title. Avoid cleverness. Clarity wins.
2. **Core Thesis** — One paragraph. State the central argument. A reader should understand the full claim after reading this paragraph alone.
3. **Structural Pillars** — 3–6 bullet groups. Each pillar is one major supporting idea. Each pillar contains 2–4 sub-bullets.
4. **Target Audience** — A short list of who this is written for, and an explicit statement of who it is *not* written for.
5. **Emotional Tone** — 3–5 adjectives or short phrases. Be specific. Follow with explicit "do not" examples.
6. **Scope Boundaries** — A short list of what this article is explicitly *not*. This is the most important section for preventing scope creep.
7. **Definition of Done for Draft Phase** — Specific, binary criteria that mark when the draft is ready for review.

### Quality criteria

- The thesis is falsifiable or at least arguable — it takes a position.
- The scope is narrow enough to be covered in 1,500–3,000 words.
- A reader could begin drafting immediately without asking clarifying questions.

---

## Phase 2 — Drafting

Use the `templates/article.md` template as the structural starting point.

### Drafting rules

- Follow the template sections in order. Do not skip sections.
- Write from the thesis outward. The "Core Idea" section of the template maps to the thesis. Each body section maps to a structural pillar.
- Keep the tone aligned with the emotional tone defined in `THESIS.md`.
- Do not add sections not present in the template without a clear reason. If a new section is needed, note it as a comment rather than embedding it silently.
- Research references must meet the criteria in `instruction-set/RESEARCH_GROUNDING.md`.
- Visuals must meet the criteria in `instruction-set/VISUALS.md`.

### Draft file conventions

- File is named `Draft.md`.
- Remove all template comments (`<!-- ... -->`) from the body before submitting for review.
- Retain placeholder text only where content is intentionally deferred.

---

## Phase 3 — Revision

Revision is not rewriting. It is precision work.

- Address one concern at a time.
- Track substantial changes as comments in the commit message, not in the file itself.
- If the thesis shifts during revision, update `THESIS.md` to match before continuing.

---

## Phase 4 — Publication

When the draft is approved, rename `Draft.md` to `published.md`.

Follow `workflow/PUBLISHING_MEDIUM.md` and `workflow/PUBLISHING_WEBSITE.md` for the distribution steps.

---

## Conventions

- Article folder names follow the format `YYYY-MM-slug`. The `YYYY-MM` portion reflects the publication target month, not the drafting start date.
- Slugs are lowercase, hyphen-separated, and stable. Do not rename a slug after the article is published.
- All assets (images, diagrams) live in `articles/YYYY-MM-slug/assets/`.
