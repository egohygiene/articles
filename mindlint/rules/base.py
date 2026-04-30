from abc import ABC, abstractmethod
from typing import List
from mindlint.models.article import Article


class Issue:
    def __init__(self: "Issue", message: str, severity: str = "warning") -> None:
        self.message = message
        self.severity = severity

    def __str__(self: "Issue") -> str:
        return f"[{self.severity}] {self.message}"


class Rule(ABC):
    @abstractmethod
    def check(self: "Rule", article: Article) -> List[Issue]:
        pass
