# Visuals — Guidelines

Standards for creating, selecting, and integrating visual elements into articles in this repository.

---

## Purpose

Visuals should clarify an idea that prose alone cannot convey efficiently. They are not decoration. This guide defines when to include a visual, what types are acceptable, and how to produce them.

---

## When to Include a Visual

Include a visual only when at least one of the following is true:

- A relationship or structure is easier to grasp in diagram form than in prose.
- A process has multiple steps that benefit from visual sequencing.
- A comparison between two or more states is central to the argument.

Do not include a visual:
- Because the template has a placeholder for one.
- To add visual interest without adding conceptual clarity.
- As a substitute for a clear written explanation.

Each article should have at most one primary visual. A second visual is acceptable if it addresses a genuinely distinct concept.

---

## Accepted Visual Types

| Type | Use case |
|------|----------|
| Conceptual diagram | Relationships between ideas, systems, or forces |
| Process flow | Sequential steps or phases |
| Comparison table | Side-by-side differences between two or more states |
| Annotated illustration | A single subject with labeled components |

Avoid:
- Charts or graphs built on data from this repository (not a data publication)
- Stock photography
- Decorative icons or emojis used as visual elements
- Screenshots (unless documenting a specific interface)

---

## Visual Tone

Visuals must match the overall tone of the article: calm, analytical, and functional.

- **Prefer minimal style.** Clean lines, neutral palette, high contrast.
- **Avoid visual noise.** No drop shadows, gradients, or decorative frames unless they carry meaning.
- **Label clearly.** Every element in a diagram must be labeled in plain language. No unexplained abbreviations.
- **Use consistent typography.** Labels should use the same typeface and weight throughout a single visual.

---

## File Format and Naming

- Save all visual assets in `articles/YYYY-MM-slug/assets/`.
- Use lowercase, hyphen-separated filenames: `cognitive-load-model.png`.
- Prefer `.png` for diagrams and `.svg` for vector graphics when available.
- Do not embed images inline in the Markdown source as base64.

---

## Alt Text Requirements

Every visual included in an article must have descriptive alt text.

- Alt text must describe what the visual shows, not just its title.
- It should be understandable to someone who cannot see the image.
- Keep it under 125 characters where possible.

Example:

```markdown
![Diagram showing intrinsic and extraneous cognitive load as two stacked bars within a fixed working memory capacity](../assets/cognitive-load-model.png)
```

---

## Caption Convention

Include a caption below every visual using an HTML comment in the source Markdown:

```markdown
<!-- Caption: Brief description of what the visual shows and why it is included. -->
```

The caption should add context that the alt text does not provide — for example, connecting the visual to the argument in the article.

---

## Producing Visuals

Diagrams may be produced using any tool that outputs clean, accessible images. Recommended approaches:

- **Diagrams.net (draw.io)** — Free, exports clean SVG and PNG, no account required.
- **Excalidraw** — Sketch-style diagrams with clean minimal output.
- **Mermaid** — Code-defined diagrams for flowcharts and sequences; renders in GitHub Markdown natively.

If using Mermaid, include the source code block in the draft file and note that a rendered image must be exported before publication.
