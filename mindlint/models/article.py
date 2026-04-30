from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Section:
    title: str
    content: str


@dataclass
class Image:
    path: str
    has_caption: bool = False
    has_ai_disclosure: bool = False
    has_alt_comment: bool = False


@dataclass
class Article:
    path: Path
    title: str
    has_toc: bool
    sections: List[Section]
    images: List[Image]
    raw_text: str
