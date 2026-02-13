"""
Agent Template Engine CLI

A command-line tool for bootstrapping agent files from templates.
"""

import sys
from pathlib import Path

import readchar
import typer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, IntPrompt, Prompt

from agentkit.answers import PromptAnswer, collect_answer, write_answers_file
from agentkit.config import (
    GITHUB_OWNER,
    GITHUB_REPO,
    get_project_templates_dir,
    read_cached_version,
    save_version,
)
from agentkit.github import GitHubError, download_and_extract
from agentkit.parser import PromptDefinition, extract_prompt_definitions
from agentkit.rendering import (
    generate_prompt_file,
    load_answers_file,
    render_template,
)
from agentkit.templates import discover_templates, get_output_dir, load_template

# AIDEV-NOTE: Console instance for Rich library formatting
console = Console()
app = typer.Typer(
    name="agentkit",
    help="Agent Template Engine - Bootstrap customized agent files from templates.",
    no_args_is_help=False,
)


# AIDEV-NOTE: Helper to check if stdin is a TTY (terminal)
def _is_interactive() -> bool:
    """Check if running in an interactive terminal."""
    return sys.stdin.isatty()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Agent Template Engine - Bootstrap customized agent files from templates."""
    if ctx.invoked_subcommand is None:
        _show_menu()


def _show_menu() -> None:
    """Display interactive menu and handle user selection."""
    while True:
        console.clear()
        console.print(
            Panel(
                "[bold cyan]Agent Template Engine[/bold cyan]",
                border_style="cyan",
                expand=False,
            )
        )
        console.print()
        console.print("  [bold]1[/bold]. Choose an agent template")
        console.print("  [bold]0[/bold]. Exit")
        console.print()

        # AIDEV-NOTE: Use readchar for single-key if terminal, otherwise prompt
        if _is_interactive():
            console.print("[dim]Press a key to select an option...[/dim]")
            key = readchar.readkey()
        else:
            key = str(IntPrompt.ask("Select an option", default=0, console=console))

        if key == "0":
            console.print("\n[yellow]Goodbye![/yellow]")
            break
        elif key == "1":
            _select_template()
        else:
            console.print(f"\n[red]Invalid option '{key}'. Please try again.[/red]")
            console.input("[dim]Press Enter to continue...[/dim]")


def _select_template() -> None:
    """Display template selection menu and handle user choice."""
    console.clear()
    console.print(
        Panel(
            "[bold cyan]Select Agent Template[/bold cyan]",
            border_style="cyan",
            expand=False,
        )
    )
    console.print()

    try:
        templates = discover_templates()
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        console.input("[dim]Press Enter to continue...[/dim]")
        return

    if not templates:
        console.print("[yellow]No templates found in templates directory.[/yellow]")
        console.input("[dim]Press Enter to continue...[/dim]")
        return

    # Display available templates with bold numbers
    for idx, template in enumerate(templates, start=1):
        console.print(f"  [bold]{idx}[/bold]. {template['name']}")
    console.print("  [bold]0[/bold]. Back to main menu")
    console.print()

    # AIDEV-NOTE: Use readchar for single digit if <=9 templates and interactive
    if _is_interactive() and len(templates) <= 9:
        console.print("[dim]Press a number to select...[/dim]")
        key = readchar.readkey()
    else:
        key = str(IntPrompt.ask("Select a template", default=0, console=console))

    if key == "0":
        return

    try:
        choice = int(key)
        if 1 <= choice <= len(templates):
            selected = templates[choice - 1]
            _show_template_actions_menu(selected)
        else:
            console.print(f"\n[red]Invalid selection '{key}'.[/red]")
            console.input("[dim]Press Enter to continue...[/dim]")
    except ValueError:
        console.print(f"\n[red]Invalid input '{key}'. Please enter a number.[/red]")
        console.input("[dim]Press Enter to continue...[/dim]")


def _show_template_actions_menu(template: dict[str, str]) -> None:
    """Display actions menu for a selected template."""
    while True:
        console.clear()
        console.print(
            Panel(
                "[bold cyan]Template Actions[/bold cyan]",
                border_style="cyan",
                expand=False,
            )
        )
        console.print()
        console.print(f"  Template: [bold green]{template['name']}[/bold green]")
        console.print()
        console.print("  [bold]1[/bold]. List Questions")
        console.print("  [bold]2[/bold]. Show Template Content")
        console.print("  [bold]3[/bold]. Define Agent")
        console.print("  [bold]4[/bold]. Generate Prompt")
        console.print("  [bold]0[/bold]. Back")
        console.print()

        # AIDEV-NOTE: Use readchar for single-key if interactive terminal
        if _is_interactive():
            console.print("[dim]Press a key to select an action...[/dim]")
            key = readchar.readkey()
        else:
            key = str(IntPrompt.ask("Select an action", default=0, console=console))

        if key == "0":
            return
        elif key == "1":
            _list_questions(template)
        elif key == "2":
            _show_template_content(template)
        elif key == "3":
            _define_agent(template)
        elif key == "4":
            _generate_prompt_from_answers(template)
        else:
            console.print(f"\n[red]Invalid option '{key}'.[/red]")
            console.input("[dim]Press Enter to continue...[/dim]")


def _list_questions(template: dict[str, str]) -> None:
    """Display all prompt questions found in the template."""
    console.clear()
    console.print(
        Panel(
            "[bold cyan]Template Questions[/bold cyan]",
            border_style="cyan",
            expand=False,
        )
    )
    console.print()
    console.print(f"  Template: [bold green]{template['name']}[/bold green]")
    console.print()

    try:
        content = load_template(template["path"])
        prompts = extract_prompt_definitions(content)
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        console.input("[dim]Press Enter to continue...[/dim]")
        return

    if not prompts:
        console.print("[yellow]No prompt definitions found in this template.[/yellow]")
        console.input("[dim]Press Enter to continue...[/dim]")
        return

    for idx, prompt in enumerate(prompts, start=1):
        console.print(f"  [bold white]{idx}. {prompt.id}[/bold white]")
        console.print(f"     Question: {prompt.question}")
        if prompt.hint:
            console.print(f"     [dim]Hint: {prompt.hint}[/dim]")
        console.print(f"     Format: {prompt.format}")
        if prompt.default:
            console.print(f"     [blue]Default: {prompt.default}[/blue]")
        console.print()

    console.input("[dim]Press Enter to continue...[/dim]")


def _show_template_content(template: dict[str, str]) -> None:
    """Display the raw template content."""
    console.clear()
    console.print(
        Panel(
            "[bold cyan]Template Content[/bold cyan]",
            border_style="cyan",
            expand=False,
        )
    )
    console.print()
    console.print(f"  Template: [bold green]{template['name']}[/bold green]")
    console.print(f"  [dim]Path: {template['path']}[/dim]")
    console.print()
    console.print("─" * 50)
    console.print()

    try:
        content = load_template(template["path"])
        console.print(content)
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")

    console.print()
    console.print("─" * 50)
    console.input("[dim]Press Enter to continue...[/dim]")


def _define_agent(template: dict[str, str]) -> None:
    """Walk user through questions and generate answers file."""
    console.clear()
    console.print(
        Panel("[bold cyan]Define Agent[/bold cyan]", border_style="cyan", expand=False)
    )
    console.print()
    console.print(f"  Template: [bold green]{template['name']}[/bold green]")
    console.print()

    try:
        content = load_template(template["path"])
        prompts = extract_prompt_definitions(content)
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        console.input("[dim]Press Enter to continue...[/dim]")
        return

    if not prompts:
        console.print("[yellow]No prompt definitions found in this template.[/yellow]")
        console.input("[dim]Press Enter to continue...[/dim]")
        return

    console.print(f"This template has {len(prompts)} question(s) to answer.")
    console.print("Press Enter to use the default value (if available).")
    console.print()

    if not Confirm.ask("Ready to begin?", default=True, console=console):
        return

    answers: list[PromptAnswer] = []

    for idx, prompt in enumerate(prompts, start=1):
        console.print()
        console.print("─" * 50)
        console.print(
            f"  [bold cyan]Question {idx}/{len(prompts)}: {prompt.id}[/bold cyan]"
        )
        console.print()
        console.print(f"  {prompt.question}")

        if prompt.hint:
            console.print(f"  [dim]Hint: {prompt.hint}[/dim]")

        if prompt.default:
            console.print(f"  [blue]Default: {prompt.default}[/blue]")

        console.print()

        # Handle different formats
        if prompt.format == "markdown-list":
            response = _prompt_multiline(prompt)
        else:
            response = _prompt_single_line(prompt)

        answer = collect_answer(prompt, response)
        answers.append(answer)

        console.print("  [green]✓ Recorded[/green]")

    # Write the answers file
    console.print()
    console.print("─" * 50)
    console.print()

    try:
        output_path = write_answers_file(template["name"], answers)
        console.print("[bold green]✓ Answers file generated successfully![/bold green]")
        console.print()
        console.print(f"  Output: {output_path}")
    except OSError as e:
        console.print(f"[red]Error writing file: {e}[/red]")
        console.input("[dim]Press Enter to continue...[/dim]")
        return

    # Offer to generate the prompt file
    console.print()
    console.print(
        "[yellow]HINT:[/yellow] You are encouraged to manually review and update the answer file "
        "found in the output folder first. Return to this template and render your answers as a separate step."
    )
    console.print()
    if Confirm.ask(
        "Would you like to generate the prompt file now?", default=True, console=console
    ):
        console.print()
        if Confirm.ask(
            "Are you sure you're ready to render your agent creation prompt?",
            default=True,
            console=console,
        ):
            _render_prompt_file(template, output_path)
        else:
            console.print("[dim]Skipped prompt generation.[/dim]")

    console.print()
    console.input("[dim]Press Enter to continue...[/dim]")


def _prompt_single_line(prompt: PromptDefinition) -> str:
    """Prompt for a single-line response."""
    default_display = prompt.default or ""
    return Prompt.ask(
        "  Answer",
        default=default_display if prompt.default else None,
        show_default=bool(prompt.default),
        console=console,
    )


def _prompt_multiline(prompt: PromptDefinition) -> str:
    """Prompt for a multiline response (markdown-list format)."""
    console.print("  Enter items one per line. Empty line to finish:")
    console.print()

    lines = []
    while True:
        line = Prompt.ask("  ", default="", show_default=False, console=console)
        if not line:
            break
        # Auto-prefix with '- ' if not already a list item
        if not line.startswith("- ") and not line.startswith("* "):
            line = f"- {line}"
        lines.append(line)

    # AIDEV-NOTE: Return empty string if no input; let collect_answer handle defaults
    return "\n".join(lines)


def _render_prompt_file(template: dict[str, str], answers_path: Path) -> None:
    """Render the prompt file from template and answers."""
    try:
        content = load_template(template["path"])
        answers = load_answers_file(answers_path)
        rendered_content = render_template(content, answers)

        # Extract agent name from template name (e.g., "DotnetDeveloper" from "DotnetDeveloper.agent")
        agent_name = template["name"].replace(".agent", "")

        output_path = generate_prompt_file(rendered_content, agent_name)
        console.print("[bold green]✓ Prompt file generated successfully![/bold green]")
        console.print()
        console.print(f"  Output: {output_path}")
        console.print()
        console.print("[bold cyan]Next Steps:[/bold cyan]")
        console.print("  1. Copy the prompt file content")
        console.print("  2. Provide it to a thinking model (Claude, Gemini, etc.)")
        console.print(
            "  3. Work with the agent to generate your final agent configuration"
        )
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
    except OSError as e:
        console.print(f"[red]Error writing file: {e}[/red]")


def _generate_prompt_from_answers(template: dict[str, str]) -> None:
    """Generate prompt file from an existing answers file."""
    console.clear()
    console.print(
        Panel(
            "[bold cyan]Generate Prompt[/bold cyan]", border_style="cyan", expand=False
        )
    )
    console.print()
    console.print(f"  Template: [bold green]{template['name']}[/bold green]")
    console.print()

    # Look for existing answers file
    output_dir = get_output_dir()
    answers_filename = f"{template['name']}.answers.md"
    answers_path = output_dir / answers_filename

    if not answers_path.exists():
        console.print(f"[yellow]No answers file found at: {answers_path}[/yellow]")
        console.print()
        console.print("Please run 'Define Agent' first to create an answers file,")
        console.print("or place your answers file at the path above.")
        console.input("[dim]Press Enter to continue...[/dim]")
        return

    console.print(f"  Found answers file: {answers_path}")
    console.print()

    if not Confirm.ask(
        "Generate prompt file from this answers file?", default=True, console=console
    ):
        return

    console.print()
    _render_prompt_file(template, answers_path)

    console.print()
    console.input("[dim]Press Enter to continue...[/dim]")


@app.command()
def init(
    project_dir: Path = typer.Argument(
        None,
        help="Directory to initialize (default: current directory)",
        exists=False,
    ),
    version: str = typer.Option(
        None,
        "--version",
        "-v",
        help="Specific version tag to download (default: latest)",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Overwrite existing templates",
    ),
    token: str = typer.Option(
        None,
        "--token",
        "-t",
        help="GitHub token (or set GH_TOKEN/GITHUB_TOKEN env var)",
    ),
) -> None:
    """
    Initialize project with AgentKit templates from GitHub.

    Downloads the latest template package from GitHub releases and
    extracts to .agentkit/templates/ in the project directory.
    """
    # Use current directory if not specified
    if project_dir is None:
        project_dir = Path.cwd()
    else:
        project_dir = project_dir.resolve()

    # Ensure project directory exists
    if not project_dir.exists():
        console.print(f"[red]Error: Directory does not exist: {project_dir}[/red]")
        raise typer.Exit(1)

    # Check for existing templates
    templates_dir = get_project_templates_dir(project_dir)
    cached_version = read_cached_version(project_dir)

    if templates_dir.exists() and not force:
        version_msg = f" ({cached_version})" if cached_version else ""
        console.print(
            f"[yellow]Templates already exist{version_msg}[/yellow]\n"
            f"Location: {templates_dir}\n"
            "Use --force to overwrite"
        )
        raise typer.Exit(0)

    # Display initialization header
    console.print(
        Panel(
            "[bold cyan]AgentKit Initialization[/bold cyan]",
            border_style="cyan",
            expand=False,
        )
    )
    console.print()

    try:
        # Download and extract templates
        downloaded_version = download_and_extract(
            owner=GITHUB_OWNER,
            repo=GITHUB_REPO,
            target_dir=templates_dir,
            version=version,
            force=force,
            token=token,
        )

        # Save version info
        save_version(project_dir, downloaded_version)

        # Success message
        console.print()
        console.print(
            f"[bold green]✓[/bold green] Templates installed successfully!\n"
            f"  Version: {downloaded_version}\n"
            f"  Location: {templates_dir}\n"
        )
        console.print("Run [bold]agentkit[/bold] to start using templates.")

    except GitHubError as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
