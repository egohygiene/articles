from pathlib import Path
from mindlint.models.article import Article, Section


def parse_article(article_dir: Path) -> Article:
    file: Path = article_dir / "published.md"

    if not file.exists():
        raise FileNotFoundError(f"{file} not found")

    text: str = file.read_text(encoding="utf-8")

    lines: list[str] = text.splitlines()

    title: str = ""
    if lines and lines[0].startswith("# "):
        title = lines[0][2:]

    sections: list[Section] = []
    current_title: str | None = None
    current_content: list[str] = []

    for line in lines:
        if line.startswith("## "):
            if current_title:
                sections.append(Section(current_title, "\n".join(current_content)))
            current_title = line[3:]
            current_content = []
        else:
            current_content.append(line)

    if current_title:
        sections.append(Section(current_title, "\n".join(current_content)))

    has_toc: bool = any("Table of Contents" in s.title for s in sections)

    return Article(
        path=article_dir,
        title=title,
        has_toc=has_toc,
        sections=sections,
        images=[],
        raw_text=text,
    )
