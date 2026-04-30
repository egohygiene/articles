from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Section:
    level: int
    title: str
    content: str
    line_number: int | None = None


@dataclass(frozen=True)
class ImageReference:
    alt_text: str
    path: str
    caption: str | None
    has_medium_alt_comment: bool
    has_ai_caption_disclosure: bool
    line_number: int | None = None


@dataclass(frozen=True)
class Article:
    path: Path
    published_path: Path
    title: str
    raw_text: str
    sections: list[Section]
    images: list[ImageReference]
    has_table_of_contents: bool
    has_references: bool
    has_footer_ai_disclosure: bool

