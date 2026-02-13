"""
GitHub API interactions for template downloads.
"""

import os
import subprocess
import zipfile
from pathlib import Path
from typing import Any

import httpx
from rich.console import Console
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

console = Console()

# AIDEV-NOTE: GitHub API constants
GITHUB_API_BASE = "https://api.github.com"
CHUNK_SIZE = 8192  # 8KB chunks for streaming download


class GitHubError(Exception):
    """Base exception for GitHub-related errors."""

    pass


class RateLimitError(GitHubError):
    """Raised when GitHub API rate limit is exceeded."""

    pass


def _get_github_token() -> str | None:
    """
    Get GitHub token from environment variables or gh CLI.

    Tries in order:
    1. GH_TOKEN environment variable
    2. GITHUB_TOKEN environment variable
    3. gh CLI token (if gh is authenticated)

    Returns:
        GitHub token or None if not found
    """
    # Try environment variables first
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")
    if token:
        return token

    # Fallback to gh CLI
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if result.returncode == 0:
            token = result.stdout.strip()
            if token:
                return token
    except (FileNotFoundError, subprocess.TimeoutExpired):
        # gh CLI not available or timed out
        pass

    return None


def _get_auth_headers(token: str | None = None) -> dict[str, str]:
    """Build headers for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def _check_rate_limit(response: httpx.Response) -> None:
    """Check if rate limit was hit and raise informative error."""
    if response.status_code == 403:
        limit = response.headers.get("X-RateLimit-Limit")
        remaining = response.headers.get("X-RateLimit-Remaining")
        reset = response.headers.get("X-RateLimit-Reset")

        if remaining == "0" and reset:
            import datetime

            reset_time = datetime.datetime.fromtimestamp(int(reset))
            msg = (
                f"GitHub API rate limit exceeded ({limit} requests).\n"
                f"Rate limit resets at {reset_time.strftime('%H:%M:%S')}.\n"
                f"Set GH_TOKEN or GITHUB_TOKEN environment variable to increase limit."
            )
            raise RateLimitError(msg)


def _handle_release_response(
    response: httpx.Response,
    owner: str,
    repo: str,
    token: str | None,
    context: str = "release",
) -> None:
    """
    Handle common error responses for release API calls.

    Args:
        response: HTTP response from GitHub API
        owner: Repository owner
        repo: Repository name
        token: GitHub token (if provided)
        context: Context string for error messages (e.g., "release", "release v1.0.0")

    Raises:
        RateLimitError: When rate limit exceeded
        GitHubError: On authentication or not found errors
    """
    # Check for rate limiting
    _check_rate_limit(response)

    if response.status_code == 404:
        # 404 can mean: repo doesn't exist, no releases, OR private repo without auth
        # For private repos, GitHub returns 404 instead of 401 to hide existence
        if token:
            # Already authenticated but still got 404
            error_msg = (
                f"No {context} found for {owner}/{repo}.\n"
                "This could mean:\n"
                "  - Repository does not exist\n"
                "  - Repository has no releases\n"
                "  - You do not have access to this repository\n"
            )
        else:
            # No authentication provided
            error_msg = (
                f"No {context} found for {owner}/{repo}.\n"
                "This could mean:\n"
                "  - Repository does not exist\n"
                "  - Repository has no releases\n"
                "  - Repository is private and requires authentication\n\n"
                "If this is a private repository, please authenticate:\n"
                "  1. Run 'gh auth login' to authenticate via GitHub CLI\n"
                "  2. Or set GITHUB_TOKEN or GH_TOKEN environment variable"
            )
        raise GitHubError(error_msg)

    if response.status_code == 401:
        raise GitHubError(
            f"Authentication required to access {owner}/{repo}.\n"
            "This repository requires authentication. Please either:\n"
            "  1. Run 'gh auth login' to authenticate via GitHub CLI\n"
            "  2. Set GITHUB_TOKEN or GH_TOKEN environment variable"
        )


def get_latest_release(
    owner: str, repo: str, token: str | None = None
) -> dict[str, Any]:
    """
    Fetch latest release metadata from GitHub.

    Args:
        owner: Repository owner
        repo: Repository name
        token: Optional GitHub token for authentication

    Returns:
        Release metadata dictionary

    Raises:
        GitHubError: On API errors
        RateLimitError: When rate limit exceeded
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases/latest"
    headers = _get_auth_headers(token)

    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, headers=headers, follow_redirects=True)
            _handle_release_response(response, owner, repo, token, "releases")
            response.raise_for_status()
            return response.json()

    except httpx.HTTPError as e:
        raise GitHubError(f"Failed to fetch release info: {e}") from e


def get_specific_release(
    owner: str, repo: str, version: str, token: str | None = None
) -> dict[str, Any]:
    """
    Fetch specific release metadata from GitHub by version tag.

    Args:
        owner: Repository owner
        repo: Repository name
        version: Version tag (e.g., 'v0.1.0')
        token: Optional GitHub token for authentication

    Returns:
        Release metadata dictionary

    Raises:
        GitHubError: On API errors
        RateLimitError: When rate limit exceeded
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases/tags/{version}"
    headers = _get_auth_headers(token)

    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, headers=headers, follow_redirects=True)
            _handle_release_response(response, owner, repo, token, f"release {version}")
            response.raise_for_status()
            return response.json()

    except httpx.HTTPError as e:
        raise GitHubError(f"Failed to fetch release info: {e}") from e


def find_template_asset(release: dict[str, Any]) -> dict[str, Any] | None:
    """
    Find the template ZIP asset in release assets.

    Args:
        release: Release metadata from GitHub API

    Returns:
        Asset metadata dict or None if not found
    """
    assets = release.get("assets", [])

    # Look for agentkit-templates-*.zip
    for asset in assets:
        name = asset.get("name", "")
        if name.startswith("agentkit-templates-") and name.endswith(".zip"):
            return asset

    return None


def download_template(
    download_url: str,
    destination: Path,
    token: str | None = None,
    show_progress: bool = True,
) -> Path:
    """
    Download template ZIP from GitHub with progress tracking.

    Args:
        download_url: URL to download from (API URL or browser download URL)
        destination: Local path to save ZIP
        token: Optional GitHub token
        show_progress: Whether to show progress bar

    Returns:
        Path to downloaded file

    Raises:
        GitHubError: On download errors
    """
    headers = _get_auth_headers(token)

    # If using API URL, need special Accept header to get the asset content
    if "api.github.com" in download_url:
        headers["Accept"] = "application/octet-stream"

    try:
        with httpx.Client(timeout=30.0) as client:
            with client.stream(
                "GET", download_url, headers=headers, follow_redirects=True
            ) as response:
                response.raise_for_status()

                total = int(response.headers.get("content-length", 0))

                if show_progress and total > 0:
                    progress = Progress(
                        TextColumn("[progress.description]{task.description}"),
                        BarColumn(),
                        DownloadColumn(),
                        TransferSpeedColumn(),
                        TimeRemainingColumn(),
                    )

                    with progress:
                        task = progress.add_task("Downloading templates", total=total)

                        with open(destination, "wb") as f:
                            for chunk in response.iter_bytes(chunk_size=CHUNK_SIZE):
                                f.write(chunk)
                                progress.update(task, advance=len(chunk))
                else:
                    # No progress bar - simple download
                    with open(destination, "wb") as f:
                        for chunk in response.iter_bytes(chunk_size=CHUNK_SIZE):
                            f.write(chunk)

                return destination

    except httpx.HTTPError as e:
        # Clean up partial download
        if destination.exists():
            destination.unlink()
        raise GitHubError(f"Failed to download template: {e}") from e


def extract_templates(zip_path: Path, target_dir: Path, force: bool = False) -> None:
    """
    Extract templates from ZIP to target directory.

    Args:
        zip_path: Path to ZIP file
        target_dir: Directory to extract to
        force: Overwrite existing files

    Raises:
        GitHubError: On extraction errors
    """
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            # AIDEV-NOTE: ZIP contains tooling/templates/*, extract to .agentkit/templates/
            members = zf.namelist()

            # Filter to only tooling/templates/* files
            template_files = [m for m in members if m.startswith("tooling/templates/")]

            if not template_files:
                raise GitHubError("ZIP does not contain tooling/templates/ directory")

            # Create target directory
            target_dir.mkdir(parents=True, exist_ok=True)

            # Extract with path transformation
            for member in template_files:
                # Remove 'tooling/templates/' prefix
                relative_path = member.replace("tooling/templates/", "", 1)

                if not relative_path:  # Skip the directory itself
                    continue

                target_path = target_dir / relative_path

                # Check if file exists
                if target_path.exists() and not force:
                    continue  # Skip existing files unless force

                # Create parent directories
                target_path.parent.mkdir(parents=True, exist_ok=True)

                # Extract file or create directory
                if member.endswith("/"):
                    target_path.mkdir(exist_ok=True)
                else:
                    with zf.open(member) as source:
                        with open(target_path, "wb") as target:
                            target.write(source.read())

            # Set executable permissions on .sh files (Unix only)
            if os.name != "nt":
                _set_executable_permissions(target_dir)

    except zipfile.BadZipFile as e:
        raise GitHubError(f"Invalid ZIP file: {e}") from e
    except Exception as e:
        raise GitHubError(f"Failed to extract templates: {e}") from e


def _set_executable_permissions(directory: Path) -> None:
    """Set executable permissions on .sh files."""
    for sh_file in directory.rglob("*.sh"):
        if sh_file.is_file():
            # Add execute permission for owner, group, others
            sh_file.chmod(sh_file.stat().st_mode | 0o111)


def download_and_extract(
    owner: str,
    repo: str,
    target_dir: Path,
    version: str | None = None,
    force: bool = False,
    token: str | None = None,
) -> str:
    """
    Download and extract templates from GitHub release.

    Args:
        owner: Repository owner
        repo: Repository name
        target_dir: Directory to extract templates to
        version: Specific version tag (uses latest if None)
        force: Overwrite existing files
        token: Optional GitHub token

    Returns:
        Version tag of downloaded templates

    Raises:
        GitHubError: On any errors
    """
    # Auto-detect token if not provided
    if token is None:
        token = _get_github_token()

    # Fetch release info
    if version:
        console.print(f"Fetching release {version}...")
        release = get_specific_release(owner, repo, version, token)
    else:
        console.print("Fetching latest release...")
        release = get_latest_release(owner, repo, token)

    version_tag = release.get("tag_name", "unknown")

    # Find template asset
    asset = find_template_asset(release)
    if not asset:
        raise GitHubError(
            f"No template package found in release {version_tag}. "
            "Expected agentkit-templates-*.zip"
        )

    # Prefer API URL which supports authentication for both public and private repos.
    # Falls back to browser_download_url if API URL is not available.
    # The 'url' field is the API endpoint that requires/supports authentication
    # The 'browser_download_url' field is for direct downloads
    download_url = asset.get("url") or asset.get("browser_download_url")
    if not download_url:
        raise GitHubError("Asset download URL not found")

    # Download to temp location
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_zip = Path(temp_dir) / asset.get("name", "templates.zip")

        console.print(f"Downloading templates {version_tag}...")
        download_template(download_url, temp_zip, token)

        console.print("Extracting templates...")
        extract_templates(temp_zip, target_dir, force)

    return version_tag
