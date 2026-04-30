from __future__ import annotations

from pathlib import Path

import click

from mindlint.ai import AIProvider, AnthropicProvider, OllamaProvider, OpenAIProvider
from mindlint.config.defaults import DEFAULT_OLLAMA_MODEL
from mindlint.core.reporter import RichReporter
from mindlint.core.runner import LintRunner
from mindlint.models.issue import Severity


@click.command()
@click.argument(
    "path",
    default=".",
    required=False,
    type=click.Path(path_type=Path),
)
@click.option("--ai", "enable_ai", is_flag=True, help="Enable qualitative AI checks.")
@click.option(
    "--ai-provider",
    type=click.Choice(["ollama", "openai", "anthropic"]),
    default="ollama",
    show_default=True,
    help="AI provider to use when --ai is enabled.",
)
@click.option(
    "--ollama-model",
    default=DEFAULT_OLLAMA_MODEL,
    show_default=True,
    help="Ollama model to use when --ai-provider=ollama.",
)
@click.option(
    "--fail-on",
    type=click.Choice(["info", "warning", "error"]),
    default="error",
    show_default=True,
    help="Lowest issue severity that should return a non-zero exit code.",
)
def main(
    path: Path,
    enable_ai: bool,
    ai_provider: str,
    ollama_model: str,
    fail_on: Severity,
) -> None:
    target = path.resolve()
    if not target.exists():
        raise click.ClickException(f"Path does not exist: {target}")

    provider = _build_ai_provider(ai_provider, ollama_model) if enable_ai else None
    runner = LintRunner(ai_provider=provider)
    result = runner.run_path(target)
    RichReporter().report(result)
    raise SystemExit(result.exit_code(fail_on))


def _build_ai_provider(provider_name: str, ollama_model: str) -> AIProvider:
    if provider_name == "ollama":
        return OllamaProvider(model=ollama_model)
    if provider_name == "openai":
        return OpenAIProvider()
    if provider_name == "anthropic":
        return AnthropicProvider()

    raise click.ClickException(f"Unsupported AI provider: {provider_name}")

