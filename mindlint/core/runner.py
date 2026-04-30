from typing import List
from mindlint.models.article import Article
from mindlint.rules.base import Rule, Issue


class LintRunner:
    def __init__(self: "LintRunner", rules: List[Rule]):
        self.rules = rules

    def run(self: "LintRunner", article: Article) -> List[Issue]:
        issues: list[Issue] = []
        for rule in self.rules:
            issues.extend(rule.check(article))
        return issues
