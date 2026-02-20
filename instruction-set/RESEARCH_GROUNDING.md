# Research Grounding — Guidelines

Standards for sourcing, citing, and integrating research into articles in this repository.

---

## Purpose

Every article in this repository makes claims. Those claims need grounding. This guide defines what counts as adequate grounding, how to cite sources, and how to avoid common research errors.

---

## What Counts as Grounding

An article is considered research-grounded if it meets all of the following:

- It references 3–6 sources per article.
- At least one source is a peer-reviewed study, foundational text, or established framework.
- No claim presented as fact rests entirely on the author's assertion.
- Sources are accessible to a general technical reader (no paywalled sources cited without an accessible alternative).

---

## Source Tiers

Use this hierarchy when selecting sources. Prefer higher-tier sources when they are available.

| Tier | Type | Examples |
|------|------|---------|
| 1 | Peer-reviewed research | Cognitive load theory (Sweller, 1988); working memory studies |
| 2 | Foundational books or frameworks | *The Design of Everyday Things*; DSM diagnostic criteria |
| 3 | Established practitioner writing | Martin Fowler, Will Larson, Nicole Forsgren et al. |
| 4 | Credible journalism or long-form analysis | ACM Queue, IEEE Spectrum, Increment |
| 5 | Primary sources | Official documentation, specification texts |

Avoid:
- Blog posts without named authors
- Social media threads as primary evidence
- Self-published productivity content
- Sources cited only because they are well-known, not because they are directly relevant

---

## How to Cite

No specific citation format is required. Consistency within a single article is sufficient.

Acceptable formats:

- Plain inline reference: `(Sweller, 1988)`
- Footnote-style note: `¹ Sweller, J. (1988). Cognitive load during problem solving.`
- End-of-article list: `- Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257–285.`

Requirements:
- Author name(s) must be included.
- Publication year must be included.
- Title must be included.
- Publication venue or URL must be included where applicable.

---

## Integration Standards

Research should support the argument, not perform erudition.

- **Quote sparingly.** Paraphrase when possible. Quote only when the exact wording matters.
- **Anchor to the thesis.** Every source cited must connect directly to a structural pillar in `THESIS.md`. If a source does not connect, do not include it.
- **Do not over-cite.** Listing eight sources for a single sentence signals insecurity, not rigor. Choose the most relevant one.
- **Name the framework.** When referencing a specific model or theory, name it explicitly: "Sweller's Cognitive Load Theory" rather than "research shows."

---

## Common Errors to Avoid

- Citing a study that shows correlation as if it shows causation
- Using a statistic without its source (e.g., "studies show 70% of engineers...")
- Citing a source from the wrong domain (e.g., using classroom learning research to make claims about adult professional work without acknowledging the difference)
- Using recency as a proxy for quality (a 1988 study may be more reliable than a 2023 blog post)

---

## Research File Convention

If research notes, quotes, or references are collected during drafting, store them in:

```
articles/YYYY-MM-slug/assets/research-notes.md
```

This is optional but encouraged for articles with more than four sources.
