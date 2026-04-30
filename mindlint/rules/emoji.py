from mindlint.rules.base import Rule, Issue
from mindlint.models.article import Article


class EmojiTitleRule(Rule):
    def check(self: "EmojiTitleRule", article: Article) -> list[Issue]:
        if not article.title:
            return [Issue("Missing title", "error")]

        first_char: str = article.title[0]

        if ord(first_char) < 10000:
            return [Issue("Missing emoji prefix")]

        return []
