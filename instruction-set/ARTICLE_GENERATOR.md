# Article Generator — System Guide

A structured, repeatable process for transforming an idea into a published article.

This document governs every article in this repository.

Infrastructure should never slow idea expression. Structure enables clarity.

---

## Core Principle

Each article is a controlled compression of complexity.

Clarity is achieved by:

1. Defining scope before writing
2. Structuring argument before elaboration
3. Supporting claims with research
4. Using visuals only when they reduce cognitive load
5. Publishing only when the thesis is intact

---

## Article Lifecycle

Every article moves through four phases:

| Phase | Output | Location |
|-------|--------|----------|
| 1. Thesis & Scope | `THESIS.md` | `articles/YYYY-MM-slug/` |
| 2. Draft | `draft.md` | `articles/YYYY-MM-slug/` |
| 3. Refinement | Updated `draft.md` | `articles/YYYY-MM-slug/` |
| 4. Publication | `published.md` | `articles/YYYY-MM-slug/` |

Do not skip phases.  
Do not draft before thesis clarity.

---

## Phase 1 — Thesis & Scope

Create `THESIS.md` before writing body text.

### Required Sections

- **Working Title**
- **Core Thesis (1 paragraph)**
- **Structural Pillars (3–6)**
- **Target Audience**
- **Tone Definition**
- **Scope Boundaries**
- **Definition of Done**

### Quality Standards

- The thesis makes a claim.
- The scope is narrow enough for 1,500–3,000 words.
- Structural pillars map directly to body sections.
- The article can be drafted without ambiguity.

If drafting requires clarifying questions, the thesis is incomplete.

---

## Phase 2 — Draft

Draft in `draft.md`.

### Draft Rules

- Each structural pillar becomes a section.
- No new conceptual branches without updating `THESIS.md`.
- Follow emotional tone constraints.
- Avoid overextension into adjacent domains.
- If philosophy appears, anchor it to engineering.

Do not optimize sentences yet. Optimize structure.

---

## Phase 3 — Refinement

Refinement is structural compression, not expansion.

- Remove redundancy.
- Clarify transitions.
- Tighten opening and closing.
- Ensure each paragraph supports the thesis.
- Remove decorative language.

If thesis shifts, update `THESIS.md`.

---

## Phase 4 — Publication

When structurally sound:

1. Move content to `published.md`.
2. Add visuals with canonical names:
   - `header.png`
   - `figure1.png`
   - `figure2.png`
3. Confirm alt text and captions.
4. Push to `main`.
5. Verify site build.
6. Publish to Medium.
7. Set canonical link.

---

## Folder Conventions

Article folder format:

    articles/YYYY-MM-slug/
      THESIS.md
      draft.md
      published.md
      references.md
      assets/

Slugs are stable. Do not rename after publication.

---

## Editorial Standard

Every article must answer:

- What is the claim?
- Why does it matter?
- What supports it?
- What is explicitly outside scope?

If those four are unclear, do not publish.
