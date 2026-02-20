# Publishing to GitHub Pages — End-to-End Guide

A calm, repeatable workflow for deploying articles from this repository to [articles.egohygiene.io](https://articles.egohygiene.io) via GitHub Pages.

---

## Approach: Simple Static Markdown

This site does **not** use a static site generator, build pipeline, or JavaScript framework. GitHub Pages renders a repository as a simple file host. Articles are linked directly as Markdown files. This keeps the workflow deterministic and the tooling surface near zero.

If Markdown rendering in the browser becomes a meaningful friction point for readers, a minimal Jekyll setup (GitHub Pages' native engine, zero configuration required) is the justified next step — but only then.

---

## 1. Enable GitHub Pages for the Repository

1. Open the repository on GitHub: `github.com/egohygiene/articles`.
2. Go to **Settings → Pages**.
3. Under **Source**, select **Deploy from a branch**.
4. Set the branch to `main` and the folder to `/ (root)`.
5. Click **Save**.

GitHub Pages will now serve the repository root at `https://egohygiene.github.io/articles/`.

---

## 2. Add the CNAME File

A `CNAME` file at the repository root tells GitHub Pages which custom domain to respond to.

1. Create a file named `CNAME` in the repository root (no extension).
2. The file must contain exactly one line — the custom domain:

   ```
   articles.egohygiene.io
   ```

3. Commit and push:

   ```
   git add CNAME
   git commit -m "chore: add CNAME for GitHub Pages custom domain"
   git push
   ```

GitHub will detect this file automatically and link the deployment to the custom domain.

---

## 3. Configure DNS for the Subdomain

In your DNS provider's control panel for `egohygiene.io`, add the following record:

| Type  | Name     | Value                       | TTL  |
|-------|----------|-----------------------------|------|
| CNAME | articles | egohygiene.github.io        | 3600 |

**Notes:**
- The CNAME value must point to `egohygiene.github.io` (not the full repository path).
- DNS propagation can take up to 48 hours, though it is typically faster.
- Once propagation is complete, GitHub Pages will automatically provision a TLS certificate via Let's Encrypt.

---

## 4. Enforce HTTPS

After the custom domain is verified and the TLS certificate is issued:

1. Go to **Settings → Pages** in the repository.
2. Check **Enforce HTTPS**.
3. Save.

All traffic to `articles.egohygiene.io` will be redirected to HTTPS automatically.

---

## 5. Article URL Structure

Articles live in the repository at:

```
articles/YYYY-MM-slug/published.md
```

Once GitHub Pages is active, the corresponding URL is:

```
https://articles.egohygiene.io/articles/YYYY-MM-slug/published.md
```

**Examples:**

| Repository path | Published URL |
|---|---|
| `articles/2025-01-cognitive-load/published.md` | `https://articles.egohygiene.io/articles/2025-01-cognitive-load/published.md` |
| `articles/2025-03-adhd-systems/published.md` | `https://articles.egohygiene.io/articles/2025-03-adhd-systems/published.md` |

The `YYYY-MM` prefix in the slug provides implicit chronological ordering without requiring a database or build step. The slug portion should be a short, stable, lowercase identifier for the article — never change it after the first publish.

---

## 6. Store the Canonical URL Inside the Article Folder

Each article folder should contain a `canonical.txt` file that records the authoritative URL for that article. This makes the canonical source discoverable without opening the article itself.

1. After the article is published to GitHub Pages, create the file:

   ```
   articles/YYYY-MM-slug/canonical.txt
   ```

2. The file contains exactly one line — the canonical URL:

   ```
   https://articles.egohygiene.io/articles/YYYY-MM-slug/published.md
   ```

3. Commit:

   ```
   git add articles/YYYY-MM-slug/canonical.txt
   git commit -m "archive: add canonical URL for YYYY-MM-slug"
   git push
   ```

This file is the single source of truth for the article's permanent address.

---

## 7. Keep Medium and Website Content Aligned

The website is the canonical version. Medium is the distribution channel.

**Rules:**

- The text in `published.md` must match what is live on Medium. If you correct an error, update both.
- The canonical link set in Medium's advanced settings (see `PUBLISHING_MEDIUM.md`, step 5) must point to the GitHub Pages URL, not the raw GitHub file:

  ```
  https://articles.egohygiene.io/articles/YYYY-MM-slug/published.md
  ```

- Do not publish a revised version to Medium without first updating `published.md` and pushing to `main`.

**Divergence is a bug.** If the two versions differ, the repository version is authoritative.

---

## 8. Versioning Future Articles

New articles are added by creating a new folder under `articles/` with the appropriate `YYYY-MM-slug` name. No configuration change is required — the URL becomes live as soon as the folder and `published.md` are pushed to `main`.

There is no versioning within an article. If the content of a published article changes materially, that is a correction, not a new version. Make the edit in `published.md`, commit it with a clear message, and update Medium to match.

If an article is retired:
1. Leave `published.md` in place — do not delete it.
2. Add a short note at the top of the file explaining that it has been retired and why.
3. This preserves existing links while being honest with the reader.

---

## Checklist

Use this before and after each website publish:

- [ ] `published.md` is final and pushed to `main`
- [ ] `CNAME` file is present in the repository root
- [ ] DNS CNAME record is set for `articles.egohygiene.io`
- [ ] GitHub Pages is enabled with `main` branch as source
- [ ] HTTPS is enforced in GitHub Pages settings
- [ ] Article is accessible at `https://articles.egohygiene.io/articles/YYYY-MM-slug/published.md`
- [ ] `canonical.txt` created in article folder and committed
- [ ] Medium canonical link updated to point to GitHub Pages URL
- [ ] Medium text is in sync with `published.md`
