import click
from pathlib import Path

from mindlint.models.article import Article
from mindlint.parsers.article_parser import parse_article
from mindlint.core.runner import LintRunner
from mindlint.rules.base import Issue
from mindlint.rules.emoji import EmojiTitleRule


def find_articles(base_path: Path) -> list[Path]:
    return [
        d for d in base_path.iterdir()
        if d.is_dir() and (d / "published.md").exists()
    ]


@click.command()
@click.argument("path", default=".", required=False)
def main(path: str):
    target: Path = Path(path).resolve()

    click.echo("🧠 mindlint — article linter")
    click.echo(f"📂 Target: {target}")

    if not target.exists():
        click.echo("❌ Path does not exist")
        raise SystemExit(1)

    article_dirs: list[Path] = find_articles(target)

    click.echo(f"\nFound {len(article_dirs)} articles:\n")

    runner: LintRunner = LintRunner([
        EmojiTitleRule(),  # stub rule
    ])

    for article_dir in article_dirs:
        article: Article = parse_article(article_dir)
        issues: list[Issue] = runner.run(article)

        if not issues:
            click.echo(f"✔ {article_dir.name}")
        else:
            click.echo(f"⚠ {article_dir.name}")
            for issue in issues:
                click.echo(f"   - {issue}")
