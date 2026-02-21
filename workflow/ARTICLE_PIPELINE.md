# Article Publishing Pipeline — Ego Hygiene

This document defines the canonical workflow for creating, publishing, and maintaining articles in this repository.

It exists so that infrastructure does not need to be rediscovered in future conversations.

---

## 1. Architecture Overview

### Canonical Content
articles/YYYY-MM-slug/
  published.md
  draft.md
  references.md
  assets/

Markdown is the source of truth.

### Presentation Layer
templates/
  article-template.html
  article.css

site/
  index.html
  article.css
  articles/YYYY-MM-slug/article.html  (generated)

### Deployment
GitHub Action:
- Converts published.md → HTML via Pandoc
- Injects into article-template.html
- Copies assets
- Regenerates index
- Deploys via GitHub Pages

---

## 2. Creating a New Article

1. Create folder:
   articles/YYYY-MM-slug/

2. Add:
   draft.md
   published.md
   references.md
   assets/

3. Write thesis in THESIS.md (optional).

4. Draft in draft.md.

5. Move final version into published.md.

---

## 3. Writing Rules

Follow:
- instruction-set/ARTICLE_GENERATOR.md
- instruction-set/RESEARCH_GROUNDING.md
- instruction-set/VISUALS.md

Markdown must:
- Start with `# Title`
- Use semantic headings
- Avoid inline styling
- Reference images as:
  assets/filename.png

Optional section IDs allowed:
`## Section Title {#section-id}`

---

## 4. Images

- Header image at top of article.
- Figures stored in assets/.
- Referenced with relative paths.
- No inline HTML.
- No base64 embeds.

---

## 5. References

- Include full references directly in published.md.
- Maintain references.md for canonical verification.
- All links should resolve.
- Avoid fabricated citations.

---

## 6. Deployment

On push to main:

GitHub Action:
1. Installs Pandoc.
2. Converts Markdown → HTML.
3. Injects into template.
4. Copies assets.
5. Regenerates index.
6. Deploys site.

Live site:
https://articles.egohygiene.io/articles/YYYY-MM-slug/article.html

---

## 7. Medium Publishing

1. Copy content from published.md.
2. Upload header image.
3. Upload inline figures.
4. Set canonical link to:

   https://articles.egohygiene.io/articles/YYYY-MM-slug/article.html

5. Add 3–5 relevant topics.
6. Publish.

Medium is distribution.
GitHub Pages is canonical.

---

## 8. Adding to Homepage

No manual edits required.

Index auto-generates links from published articles.

---

## 9. Closing an Article

After publishing:

- Confirm site renders.
- Confirm Medium canonical link.
- Commit any fixes.
- Tag release (optional).
- Close milestone.

---

## 10. System Rules

- Do not manually edit site/articles/.
- Do not manually create article.html.
- Do not add styling inside Markdown.
- Keep Markdown canonical.
- Keep CSS centralized.
- Keep process calm and repeatable.

Infrastructure should never slow idea expression.
