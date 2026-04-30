from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mindlint.ai.base import AIProvider
from mindlint.core.discovery import discover_article_dirs
from mindlint.models.article import Article
from mindlint.models.issue import Issue, Severity
from mindlint.parsers.article_parser import parse_article
from mindlint.rules import (
    EmojiTitleRule,
    FooterAIDisclosureRule,
    ReferencesRule,
    Rule,
    TableOfContentsRule,
    VisualsRule,
)


@dataclass(frozen=True)
class ArticleLintResult:
    article: Article
    issues: list[Issue]

    @property
    def has_errors(self) -> bool:
        return any(issue.severity == "error" for issue in self.issues)

    @property
    def has_warnings(self) -> bool:
        return any(issue.severity == "warning" for issue in self.issues)


@dataclass(frozen=True)
class LintRunResult:
    target: Path
    article_count: int
    results: list[ArticleLintResult]

    @property
    def issues(self) -> list[Issue]:
        return [issue for result in self.results for issue in result.issues]

    def exit_code(self, fail_on: Severity = "error") -> int:
        if fail_on == "info":
            return int(bool(self.issues))
        if fail_on == "warning":
            return int(
                any(issue.severity in {"warning", "error"} for issue in self.issues)
            )
        return int(any(issue.severity == "error" for issue in self.issues))


class LintRunner:
    def __init__(
        self,
        rules: list[Rule] | None = None,
        ai_provider: AIProvider | None = None,
    ) -> None:
        self.rules = rules or default_rules()
        self.ai_provider = ai_provider

    def run_path(self, target: Path) -> LintRunResult:
        article_dirs = discover_article_dirs(target)
        results = [self.run_article_dir(article_dir) for article_dir in article_dirs]
        return LintRunResult(
            target=target,
            article_count=len(article_dirs),
            results=results,
        )

    def run_article_dir(self, article_dir: Path) -> ArticleLintResult:
        article = parse_article(article_dir)
        issues: list[Issue] = []
        for rule in self.rules:
            issues.extend(rule.check(article))

        if self.ai_provider is not None:
            issues.extend(self.ai_provider.analyze_article(article))

        return ArticleLintResult(article=article, issues=issues)


def default_rules() -> list[Rule]:
    return [
        EmojiTitleRule(),
        TableOfContentsRule(),
        FooterAIDisclosureRule(),
        ReferencesRule(),
        VisualsRule(),
    ]

