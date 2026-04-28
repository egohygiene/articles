# Visual System — Specification

Visuals exist to **clarify structure**.

They are not decoration.
They are not aesthetic padding.
They must reduce cognitive load.

---

## 1. Core Principle

A visual should:

* make a concept easier to understand
* reveal relationships not obvious in text
* reduce explanation length

If a visual does not improve understanding, it should not exist.

---

## 2. When to Include a Visual

Include visuals only when:

* a relationship benefits from spatial representation
* a loop or feedback system is involved
* a comparison is central to the idea
* a layered abstraction needs compression

Do NOT include visuals for:

* aesthetic enhancement
* filler
* redundancy

---

## 3. Visual Count Constraints

Per article:

* 1 header image (optional but recommended)
* 2–3 supporting figures

More than 3 figures requires strong justification.

---

## 4. Visual Placement

Visuals should appear:

* after conceptual buildup
* at points of potential confusion
* where structure becomes multi-dimensional

Avoid:

* placing visuals before explanation
* clustering visuals without context

---

## 5. Visual Philosophy

All visuals must be:

* minimal
* clean
* structurally focused
* consistent in style

Avoid:

* visual noise
* unnecessary gradients
* decorative elements without meaning
* photorealistic or stock imagery

Preferred style:

* conceptual diagrams
* abstract representations
* calm, neutral palette

---

## 6. Naming Convention

Use canonical filenames:

```plaintext
header.png
figure1.png
figure2.png
figure3.png
```

All stored in:

```plaintext
articles/YYYY-MM-slug/assets/
```

No custom naming. No variations.

---

## 7. Alt Text Requirement

Every image must include alt text.

Alt text should:

* describe what is visible
* remain objective
* avoid interpretation

Example:

```plaintext
Alt text: Diagram showing feedback loop between stress and cognitive load
```

---

## 8. Caption Requirement

Every image must include a caption.

Captions must:

* explain why the image matters
* connect directly to the concept
* clarify relationships

Structure:

```plaintext
*[Conceptual explanation of the visual]*
```

---

## 9. AI Image Disclosure (Required)

All AI-generated images must include a disclosure in the caption.

Required line:

```plaintext
This image was generated using AI as a conceptual illustration.
```

This is mandatory for:

* Medium compliance
* distribution eligibility

Failure to include this may reduce distribution.

---

## 10. Visual Integrity Rules

A visual must:

* not introduce new concepts
* not contradict the text
* not oversimplify to the point of distortion

It must reinforce:

* an existing structural pillar
* a relationship already introduced

---

## 11. Complexity Constraint

A good visual:

* is understandable in under 5 seconds
* does not require explanation to decode
* reduces the need for additional paragraphs

If a visual requires explanation to understand:

* it is too complex

---

## 12. Medium Alignment

Medium values:

* clarity
* accessibility
* reader experience

Visuals that improve readability:

* increase engagement
* support distribution

Visuals that feel:

* decorative
* excessive
* or irrelevant

may reduce perceived quality.

---

## 13. Anti-Patterns

Do NOT:

* use stock photos
* include unrelated imagery
* overload with visuals
* use visuals as filler

Avoid:

* inconsistent styles
* mismatched tones
* visual clutter

---

## 14. Relationship to Template

The template defines:

* where visuals appear
* how they are formatted

This specification defines:

* when and why they exist
* how they should behave

---

## 15. Guiding Constraint

If removing a visual:

* does not reduce clarity

Then the visual should not be included.

Visuals must earn their place.
