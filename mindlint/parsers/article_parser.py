from __future__ import annotations

import re
from pathlib import Path

from mindlint.config.defaults import REQUIRED_FOOTER_DISCLOSURE, REQUIRED_IMAGE_DISCLOSURE
from mindlint.models.article import Article, ImageReference, Section

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
MEDIUM_ALT_RE = re.compile(r"<!--\s*ALT TEXT \(Medium\):.*?-->", re.IGNORECASE)


def parse_article(article_dir: Path) -> Article:
    published_path = article_dir / "published.md"

    if not published_path.exists():
        raise FileNotFoundError(f"{published_path} not found")

    text = published_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    sections = _extract_sections(lines)

    return Article(
        path=article_dir,
        published_path=published_path,
        title=_extract_title(lines),
        raw_text=text,
        sections=sections,
        images=_extract_images(lines),
        has_table_of_contents=_has_section(sections, "Table of Contents"),
        has_references=_has_section(sections, "References"),
        has_footer_ai_disclosure=_has_footer_disclosure(text),
    )


def _extract_title(lines: list[str]) -> str:
    for line in lines:
        match = HEADING_RE.match(line)
        if match and len(match.group(1)) == 1:
            return match.group(2).strip()
    return ""


def _extract_sections(lines: list[str]) -> list[Section]:
    heading_indexes: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if not match:
            continue

        level = len(match.group(1))
        if level in {2, 3}:
            heading_indexes.append((index, level, match.group(2).strip()))

    sections: list[Section] = []
    for position, (line_index, level, title) in enumerate(heading_indexes):
        next_line_index = (
            heading_indexes[position + 1][0]
            if position + 1 < len(heading_indexes)
            else len(lines)
        )
        content = "\n".join(lines[line_index + 1 : next_line_index]).strip()
        sections.append(
            Section(
                level=level,
                title=title,
                content=content,
                line_number=line_index + 1,
            )
        )

    return sections


def _extract_images(lines: list[str]) -> list[ImageReference]:
    images: list[ImageReference] = []
    for index, line in enumerate(lines):
        for match in IMAGE_RE.finditer(line):
            caption = _find_caption(lines, index)
            images.append(
                ImageReference(
                    alt_text=match.group(1).strip(),
                    path=match.group(2).strip(),
                    caption=caption,
                    has_medium_alt_comment=_has_nearby_alt_comment(lines, index),
                    has_ai_caption_disclosure=(
                        caption is not None and REQUIRED_IMAGE_DISCLOSURE in caption
                    ),
                    line_number=index + 1,
                )
            )
    return images


def _find_caption(lines: list[str], image_line_index: int) -> str | None:
    for index in range(image_line_index + 1, min(image_line_index + 4, len(lines))):
        candidate = lines[index].strip()
        if not candidate:
            continue
        if candidate.startswith("<!--"):
            continue
        if candidate.startswith("#") or IMAGE_RE.search(candidate):
            return None
        return _strip_caption_markup(candidate)
    return None


def _strip_caption_markup(text: str) -> str:
    text = text.strip()
    if text.startswith("*") and text.endswith("*"):
        return text.strip("*").strip()
    if text.startswith("_") and text.endswith("_"):
        return text.strip("_").strip()
    return text


def _has_nearby_alt_comment(lines: list[str], image_line_index: int) -> bool:
    start = max(0, image_line_index - 3)
    end = min(len(lines), image_line_index + 4)
    return any(MEDIUM_ALT_RE.search(line) for line in lines[start:end])


def _has_section(sections: list[Section], expected_title: str) -> bool:
    return any(section.title.casefold() == expected_title.casefold() for section in sections)


def _has_footer_disclosure(text: str) -> bool:
    footer_region = text.strip()[-1000:]
    return REQUIRED_FOOTER_DISCLOSURE in footer_region
