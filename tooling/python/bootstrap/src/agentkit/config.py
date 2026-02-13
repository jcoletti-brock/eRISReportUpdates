"""
Configuration constants for AgentKit.
"""

from pathlib import Path

# AIDEV-NOTE: GitHub repository configuration
GITHUB_OWNER = "brocksolutions"
GITHUB_REPO = "io-copilot"

# AIDEV-NOTE: Template storage paths
AGENTKIT_DIR = ".agentkit"
TEMPLATES_SUBDIR = "templates"
VERSION_FILE = "version.txt"


def get_agentkit_dir(project_dir: Path) -> Path:
    """Get the .agentkit directory for a project."""
    return project_dir / AGENTKIT_DIR


def get_project_templates_dir(project_dir: Path) -> Path:
    """Get the templates directory within .agentkit."""
    return get_agentkit_dir(project_dir) / TEMPLATES_SUBDIR


def get_version_file(project_dir: Path) -> Path:
    """Get the version file path."""
    return get_agentkit_dir(project_dir) / VERSION_FILE


def read_cached_version(project_dir: Path) -> str | None:
    """Read the cached template version from version.txt."""
    version_file = get_version_file(project_dir)

    if not version_file.exists():
        return None

    try:
        return version_file.read_text().strip()
    except Exception:
        return None


def save_version(project_dir: Path, version: str) -> None:
    """Save the template version to version.txt."""
    agentkit_dir = get_agentkit_dir(project_dir)
    agentkit_dir.mkdir(parents=True, exist_ok=True)

    version_file = get_version_file(project_dir)
    version_file.write_text(version + "\n")
