from __future__ import annotations

from pathlib import Path


def discover_article_dirs(target: Path) -> list[Path]:
    if target.is_file():
        if target.name == "published.md":
            return [target.parent]
        return []

    article_dirs = [
        path.parent for path in target.rglob("published.md") if path.is_file()
    ]
    return sorted(set(article_dirs))

