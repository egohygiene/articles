from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import structlog

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

log = structlog.get_logger(__name__)


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
        log.debug(
            "runner.initialized",
            rules=[rule.rule_id for rule in self.rules],
            ai_enabled=self.ai_provider is not None,
            ai_provider=type(self.ai_provider).__name__ if self.ai_provider else None,
        )

    def run_path(self, target: Path) -> LintRunResult:
        log.debug("runner.run_path.start", target=str(target))
        article_dirs = discover_article_dirs(target)
        results = [self.run_article_dir(article_dir) for article_dir in article_dirs]
        result = LintRunResult(
            target=target,
            article_count=len(article_dirs),
            results=results,
        )
        log.debug(
            "runner.run_path.complete",
            target=str(target),
            article_count=result.article_count,
            issue_count=len(result.issues),
            error_count=sum(1 for issue in result.issues if issue.severity == "error"),
            warning_count=sum(
                1 for issue in result.issues if issue.severity == "warning"
            ),
        )
        return result

    def run_article_dir(self, article_dir: Path) -> ArticleLintResult:
        log.debug("runner.run_article.start", article_dir=str(article_dir))
        article = parse_article(article_dir)
        issues: list[Issue] = []
        for rule in self.rules:
            rule_issues = rule.check(article)
            issues.extend(rule_issues)
            log.debug(
                "runner.rule_checked",
                article_dir=str(article_dir),
                rule_id=rule.rule_id,
                issue_count=len(rule_issues),
                severities=[issue.severity for issue in rule_issues],
            )

        if self.ai_provider is not None:
            ai_issues = self.ai_provider.analyze_article(article)
            issues.extend(ai_issues)
            log.debug(
                "runner.ai_checked",
                article_dir=str(article_dir),
                provider=type(self.ai_provider).__name__,
                issue_count=len(ai_issues),
            )

        result = ArticleLintResult(article=article, issues=issues)
        log.debug(
            "runner.run_article.complete",
            article_dir=str(article_dir),
            issue_count=len(issues),
            has_errors=result.has_errors,
            has_warnings=result.has_warnings,
        )
        return result


def default_rules() -> list[Rule]:
    return [
        EmojiTitleRule(),
        TableOfContentsRule(),
        FooterAIDisclosureRule(),
        ReferencesRule(),
        VisualsRule(),
    ]
