# Publishing to Medium — End-to-End Guide

A calm, repeatable workflow for moving an article from this repository to Medium and announcing it on LinkedIn.

---

## 1. Confirm the Article Is Ready

Before touching Medium, verify the source file is in its final state.

- Article lives at: `articles/YYYY-MM-slug/published.md`
- Title, body, and references are final
- Any images are stored in the article's `assets/` folder

If any of these are incomplete, finish them before continuing.

---

## 2. Prepare the Final Markdown

Open `articles/YYYY-MM-slug/published.md` in a plain-text editor.

1. **Remove internal comments.** Strip any `<!-- ... -->` notes or template placeholders that are not intended for readers.
2. **Resolve relative image paths.** Note every image reference (e.g., `../assets/filename.png`) — you will upload these separately in step 4.
3. **Check the title.** The H1 (`# Title`) at the top of the file becomes the article title on Medium. Make sure it is exactly what you want published.

---

## 3. Copy Content into Medium

1. Open [medium.com/new-story](https://medium.com/new-story).
2. **Paste the Markdown.** Medium accepts pasted Markdown with reasonable fidelity. Paste the full body of the article.
3. **Review the rendered output.** Scan every heading, list, and code block. Fix any formatting that did not translate cleanly.
4. **Do not publish yet.** Stay in draft mode through the next steps.

---

## 4. Handle Images

For each image referenced in the article:

1. Locate the file in `articles/YYYY-MM-slug/assets/`.
2. In the Medium draft, click the image placeholder or use the image insert button (`+` icon → image).
3. Upload the file directly from `assets/`.
4. Add alt text that matches the `![Alt text]` from the source Markdown.
5. Add a caption if the original article included one.

> If no images are present, skip this step.

---

## 5. Set the Canonical Link

The canonical link tells search engines that this repository's version is the original source.

1. In the Medium draft, click **More settings** (the three-dot menu or settings icon before publishing).
2. Find **Advanced settings → Canonical link**.
3. Enter the canonical URL. This is typically the GitHub URL of `published.md`:

   ```
   https://github.com/egohygiene/articles/blob/main/articles/YYYY-MM-slug/published.md
   ```

   Replace `YYYY-MM-slug` with the actual directory name.

4. Save the setting.

---

## 6. Choose Tags

Select **3 to 5 tags** that reflect the article's core topic and audience.

**Guidelines:**
- Lead with the primary subject (e.g., `ADHD`, `Software Engineering`, `Mental Health`).
- Add one audience-oriented tag (e.g., `Productivity`, `Self Improvement`, `Leadership`).
- Add one format or tone tag if applicable (e.g., `Essays`, `Personal Development`).
- Avoid overly broad tags (`Life`, `Writing`) unless they genuinely fit.
- Avoid more than 5 — precision beats volume.

---

## 7. Publish

1. Click **Publish** in the top-right corner of the Medium editor.
2. Confirm the publication settings (title, tags, canonical link).
3. Click **Publish now**.
4. Copy the final Medium article URL from the browser address bar.

---

## 8. Archive the Medium URL in the Repository

Record the published URL so it is traceable from the source.

1. Open `articles/YYYY-MM-slug/published.md`.
2. Add the following block at the very end of the file, below all other content:

   ```markdown
   ---

   **Published:** [Medium](https://medium.com/p/XXXXXXXXXXXXXXXX)
   ```

   Replace the URL with the actual Medium article URL.

3. Commit the change:

   ```
   git add articles/YYYY-MM-slug/published.md
   git commit -m "archive: add Medium URL for YYYY-MM-slug"
   git push
   ```

---

## 9. LinkedIn Cross-Post

Post a short announcement on LinkedIn within 24 hours of publishing on Medium.

**Structure:**

```
[One sentence that captures the core tension or insight of the article.]

[One to three sentences expanding on why it matters or what the reader will take away.]

Read the full piece → [Medium URL]

[2–4 relevant hashtags, e.g. #ADHD #SoftwareEngineering #CognitiveLoad]
```

**Guidelines:**
- Do not copy-paste the article. The post should stand alone as a thought worth sharing.
- Keep it under 300 words.
- Use plain language — no jargon, no excessive formatting.
- Post during business hours in your primary audience's timezone (Tuesday–Thursday tends to perform best).

---

## Checklist

Use this before each publish session:

- [ ] `published.md` is final and proofread
- [ ] Internal comments stripped
- [ ] Pasted into Medium draft and formatting reviewed
- [ ] Images uploaded and alt text set
- [ ] Canonical link set to the GitHub source URL
- [ ] 3–5 tags selected
- [ ] Article published and URL copied
- [ ] Medium URL archived in `published.md` and committed
- [ ] LinkedIn post drafted and scheduled or published
