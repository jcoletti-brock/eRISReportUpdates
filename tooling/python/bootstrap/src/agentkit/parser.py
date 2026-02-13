"""
Template parser for extracting prompt definitions and placeholders.

Implements the two-part syntax defined in DESIGN.md:
- Placeholders: {{id}} - inline substitution points
- Prompt Definitions: {{PROMPT: id ... }} - question metadata blocks
"""

import re
from dataclasses import dataclass


@dataclass
class PromptDefinition:
    """Represents a parsed prompt definition from a template."""

    id: str
    question: str
    hint: str | None = None
    format: str = "text"
    default: str | None = None


# AIDEV-NOTE: Regex captures PROMPT blocks. Group 1 = id, Group 2 = field content.
PROMPT_BLOCK_PATTERN = re.compile(r"\{\{PROMPT:\s*(\w+)\s*([\s\S]*?)\}\}", re.MULTILINE)

# Pattern to extract key-value pairs from field content
FIELD_PATTERN = re.compile(r'(\w+):\s*"([^"]*)"')

# Pattern to find simple placeholders {{id}}
PLACEHOLDER_PATTERN = re.compile(r"\{\{(\w+)\}\}")


def parse_prompt_block(block_id: str, field_content: str) -> PromptDefinition:
    """
    Parse the field content of a PROMPT block into a PromptDefinition.

    Args:
        block_id: The identifier from the PROMPT block
        field_content: The raw content between PROMPT:id and closing }}

    Returns:
        PromptDefinition with extracted fields
    """
    fields = dict(FIELD_PATTERN.findall(field_content))

    return PromptDefinition(
        id=block_id,
        question=fields.get("question", f"Value for {block_id}?"),
        hint=fields.get("hint"),
        format=fields.get("format", "text"),
        default=fields.get("default"),
    )


def extract_prompt_definitions(template_content: str) -> list[PromptDefinition]:
    """
    Extract all PROMPT definitions from template content.

    Args:
        template_content: Raw template file content

    Returns:
        List of PromptDefinition objects in order of appearance
    """
    definitions = []

    for match in PROMPT_BLOCK_PATTERN.finditer(template_content):
        block_id = match.group(1)
        field_content = match.group(2)
        definitions.append(parse_prompt_block(block_id, field_content))

    return definitions


def extract_placeholders(template_content: str) -> list[str]:
    """
    Extract all placeholder IDs from template content.

    Args:
        template_content: Raw template file content

    Returns:
        List of unique placeholder IDs in order of first appearance
    """
    seen = set()
    placeholders = []

    for match in PLACEHOLDER_PATTERN.finditer(template_content):
        placeholder_id = match.group(1)
        if placeholder_id not in seen:
            seen.add(placeholder_id)
            placeholders.append(placeholder_id)

    return placeholders


def validate_template(template_content: str) -> list[str]:
    """
    Validate that all placeholders have corresponding PROMPT definitions.

    Args:
        template_content: Raw template file content

    Returns:
        List of error messages (empty if valid)
    """
    errors = []

    placeholders = set(extract_placeholders(template_content))
    definitions = {d.id for d in extract_prompt_definitions(template_content)}

    # Check for placeholders without definitions
    missing_definitions = placeholders - definitions
    for placeholder_id in missing_definitions:
        errors.append(
            f"Placeholder '{{{{{placeholder_id}}}}}' has no PROMPT definition"
        )

    # Check for definitions without placeholders (warning, not error)
    unused_definitions = definitions - placeholders
    for def_id in unused_definitions:
        errors.append(f"PROMPT definition '{def_id}' is not used in any placeholder")

    return errors
