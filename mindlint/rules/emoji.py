import emoji

from mindlint.rules.base import Rule, Issue
from mindlint.models.article import Article


def has_emoji_prefix(text: str) -> bool:
    emojis = emoji.emoji_list(text)
    return bool(emojis and emojis[0]["match_start"] == 0)


class EmojiTitleRule(Rule):
    def check(self, article: Article) -> list[Issue]:
        if not article.title:
            return [Issue("Missing title", "error")]

        if not has_emoji_prefix(article.title):
            return [Issue("Missing emoji prefix")]

        return []
