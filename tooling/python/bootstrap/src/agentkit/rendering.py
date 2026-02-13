"""
Prompt rendering utilities.

Handles parsing answer files, rendering templates with answers,
and generating the final prompt file for AI agent consumption.
"""

import re
from dataclasses import dataclass
from pathlib import Path

from agentkit.templates import get_output_dir


@dataclass
class ParsedAnswer:
    """Represents a parsed answer from an answers file."""

    id: str
    user_response: str


# AIDEV-NOTE: Regex for ANSWER blocks using YAML literal block syntax
# Format: {{ANSWER: id\n  user_response: |\n    content\n}}
ANSWER_BLOCK_PATTERN = re.compile(
    r"\{\{ANSWER:\s*(\w+)\s+user_response:\s*\|\s*\n([\s\S]*?)\}\}",
    re.MULTILINE,
)


def parse_answer_block(match: re.Match) -> ParsedAnswer:
    """
    Parse an ANSWER block match to extract the user_response.

    Args:
        match: Regex match from ANSWER_BLOCK_PATTERN

    Returns:
        ParsedAnswer with extracted id and response
    """
    answer_id = match.group(1)
    raw_content = match.group(2)

    # Remove leading indentation (4 spaces per line)
    lines = raw_content.rstrip().split("\n")
    dedented_lines = [line[4:] if line.startswith("    ") else line for line in lines]
    user_response = "\n".join(dedented_lines)

    return ParsedAnswer(id=answer_id, user_response=user_response)


def parse_answers_file(content: str) -> dict[str, str]:
    """
    Parse an answers file and extract all answer values.

    Args:
        content: Raw content of the .answers.md file

    Returns:
        Dictionary mapping answer IDs to their values
    """
    answers = {}

    for match in ANSWER_BLOCK_PATTERN.finditer(content):
        parsed = parse_answer_block(match)
        answers[parsed.id] = parsed.user_response

    return answers


def load_answers_file(answers_path: Path) -> dict[str, str]:
    """
    Load and parse an answers file from disk.

    Args:
        answers_path: Path to the .answers.md file

    Returns:
        Dictionary mapping answer IDs to their values

    Raises:
        FileNotFoundError: If the answers file doesn't exist
    """
    if not answers_path.exists():
        raise FileNotFoundError(f"Answers file not found: {answers_path}")

    content = answers_path.read_text(encoding="utf-8")
    return parse_answers_file(content)


def render_template(template_content: str, answers: dict[str, str]) -> str:
    """
    Render a template by substituting placeholders with answer values.

    Removes PROMPT definition blocks and replaces {{id}} placeholders.

    Args:
        template_content: Raw template file content
        answers: Dictionary mapping placeholder IDs to values

    Returns:
        Rendered template content with all substitutions applied
    """
    # AIDEV-NOTE: First remove all PROMPT definition blocks
    prompt_block_pattern = re.compile(
        r"\{\{PROMPT:\s*\w+\s*[\s\S]*?\}\}\s*\n?", re.MULTILINE
    )
    content = prompt_block_pattern.sub("", template_content)
    # AIDEV-NOTE: Normalize consecutive newlines after PROMPT block removal
    content = re.sub(r"\n{3,}", "\n\n", content)

    # Replace placeholders with answer values
    def replace_placeholder(match: re.Match) -> str:
        placeholder_id = match.group(1)
        return answers.get(placeholder_id, f"{{MISSING: {placeholder_id}}}")

    placeholder_pattern = re.compile(r"\{\{(\w+)\}\}")
    content = placeholder_pattern.sub(replace_placeholder, content)

    return content


def load_prompt_template() -> str:
    """
    Load the generate_agent.prompt.template.md file.

    Returns:
        Template content for the prompt file

    Raises:
        FileNotFoundError: If the template file doesn't exist
    """
    # AIDEV-NOTE: Template is at templates/agent_templates/generate_agent.prompt.template.md
    from agentkit.templates import get_templates_dir

    templates_dir = get_templates_dir()
    template_path = (
        templates_dir / "agent_templates" / "generate_agent.prompt.template.md"
    )

    if not template_path.exists():
        raise FileNotFoundError(f"Prompt template not found: {template_path}")

    return template_path.read_text(encoding="utf-8")


def generate_prompt_file(
    rendered_content: str,
    agent_name: str,
    output_dir: Path | None = None,
) -> Path:
    """
    Generate the final prompt file by combining rendered content with the prompt template.

    Args:
        rendered_content: The rendered agent template content
        agent_name: Name of the agent (used for filename and {{AGENT_NAME}} placeholder)
        output_dir: Directory for output (defaults to ./output)

    Returns:
        Path to the created prompt file
    """
    if output_dir is None:
        output_dir = get_output_dir()

    # Load the prompt template
    prompt_template = load_prompt_template()

    # Substitute placeholders in the prompt template
    final_content = prompt_template.replace("{{RENDERED_CONTENT}}", rendered_content)
    final_content = final_content.replace("{{AGENT_NAME}}", agent_name)

    # Create output filename: create_<AgentName>.prompt.md
    filename = f"create_{agent_name}.prompt.md"
    output_path = output_dir / filename

    output_path.write_text(final_content, encoding="utf-8")

    return output_path


def render_from_answers_file(
    template_content: str,
    answers_path: Path,
    agent_name: str,
    output_dir: Path | None = None,
) -> Path:
    """
    Complete workflow: load answers, render template, generate prompt file.

    Args:
        template_content: Raw template file content
        answers_path: Path to the .answers.md file
        agent_name: Name of the agent
        output_dir: Directory for output (defaults to ./output)

    Returns:
        Path to the created prompt file
    """
    answers = load_answers_file(answers_path)
    rendered_content = render_template(template_content, answers)
    return generate_prompt_file(rendered_content, agent_name, output_dir)
