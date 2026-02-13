"""
Template discovery and loading utilities.
"""

import os
from pathlib import Path

from agentkit.config import get_project_templates_dir


def get_tooling_dir() -> Path:
    """
    Get the path to the tooling directory (dev mode only).

    Priority:
    1. AGENTKIT_TOOLING_DIR environment variable
    2. Package-relative path (tooling/python/bootstrap/src/agentkit -> tooling/)

    Returns:
        Path to tooling directory

    Raises:
        FileNotFoundError: If tooling directory cannot be found
    """
    # AIDEV-NOTE: Environment variable override for testing/CI
    if env_path := os.getenv("AGENTKIT_TOOLING_DIR"):
        return Path(env_path)

    # AIDEV-NOTE: Package-relative path works in dev repo regardless of CWD
    # tooling/python/bootstrap/src/agentkit/templates.py -> tooling/
    return Path(__file__).parent.parent.parent.parent.parent


def get_output_dir(project_dir: Path | None = None) -> Path:
    """
    Get the path to the output directory.

    Args:
        project_dir: Optional project directory (defaults to cwd)

    Returns:
        Path to .agentkit/output directory (creates if needed)
    """
    if project_dir is None:
        project_dir = Path.cwd()

    # AIDEV-NOTE: Output dir is always at .agentkit/output (dev and prod)
    output_dir = project_dir / ".agentkit" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def get_templates_dir(project_dir: Path | None = None) -> Path:
    """
    Get the path to the templates directory with priority:
    1. AGENTKIT_TEMPLATES_DIR environment variable (override)
    2. Project-local .agentkit/templates/ (prod mode after init)
    3. Repository tooling/templates/ (dev mode)

    Args:
        project_dir: Optional project directory (defaults to cwd)

    Returns:
        Path to templates directory

    Raises:
        FileNotFoundError: If templates directory cannot be found.
    """
    # AIDEV-NOTE: Environment variable override for testing/CI
    if env_path := os.getenv("AGENTKIT_TEMPLATES_DIR"):
        env_templates = Path(env_path)
        if not env_templates.exists():
            raise FileNotFoundError(
                f"AGENTKIT_TEMPLATES_DIR points to non-existent path: {env_path}"
            )
        return env_templates

    if project_dir is None:
        project_dir = Path.cwd()

    # AIDEV-NOTE: Priority 1 - Check for project-local templates (prod mode)
    local_templates = get_project_templates_dir(project_dir)
    if local_templates.exists():
        return local_templates

    # AIDEV-NOTE: Priority 2 - Fall back to repository templates (dev mode)
    dev_templates = get_tooling_dir() / "templates"
    if dev_templates.exists():
        return dev_templates

    raise FileNotFoundError(
        "Templates not found. Run 'agentkit init' to download templates."
    )


def discover_templates(templates_dir: Path | None = None) -> list[dict[str, str]]:
    """
    Discover all agent template files in the templates directory.

    Returns a list of dicts with 'name' and 'path' keys.
    """
    if templates_dir is None:
        templates_dir = get_templates_dir()

    # AIDEV-NOTE: Templates are now in agent_templates subdirectory
    agent_templates_dir = templates_dir / "agent_templates"

    if not agent_templates_dir.exists():
        return []

    templates = []
    for template_file in sorted(agent_templates_dir.glob("*.agent.md")):
        name = template_file.stem.replace(".agent", "")
        templates.append(
            {
                "name": name,
                "path": str(template_file),
            }
        )

    return templates


def load_template(template_path: str) -> str:
    """Load the contents of a template file."""
    path = Path(template_path)
    if not path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    return path.read_text(encoding="utf-8")
