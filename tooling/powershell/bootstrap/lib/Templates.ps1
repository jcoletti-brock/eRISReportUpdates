#
# Templates.ps1 - Template Discovery & Management
#
# Handles template file discovery, path management, and directory operations.
#

# AIDEV-NOTE: Global state for current working context
$Script:ToolingDir = ""
$Script:TemplatesDir = ""
$Script:OutputDir = ""
$Script:CurrentTemplatePath = ""
$Script:CurrentTemplateName = ""

# ============================================================
# Utility Functions
# ============================================================

function Write-ColorText {
    param(
        [Parameter(Mandatory)]
        [string]$Color,

        [Parameter(Mandatory)]
        [string]$Message
    )

    # Use native PowerShell colors instead of ANSI codes for better Windows compatibility
    switch ($Color) {
        'Cyan'   { Write-Host $Message -ForegroundColor Cyan }
        'Green'  { Write-Host $Message -ForegroundColor Green }
        'Yellow' { Write-Host $Message -ForegroundColor Yellow }
        'Red'    { Write-Host $Message -ForegroundColor Red }
        'Blue'   { Write-Host $Message -ForegroundColor Blue }
        'Dim'    { Write-Host $Message -ForegroundColor DarkGray }
        default  { Write-Host $Message }
    }
}

function Write-ErrorText {
    param([Parameter(Mandatory)][string]$Message)
    Write-ColorText -Color 'Red' -Message $Message
}

function Write-SuccessText {
    param([Parameter(Mandatory)][string]$Message)
    Write-ColorText -Color 'Green' -Message $Message
}

function Write-HeaderText {
    param([Parameter(Mandatory)][string]$Message)
    Write-ColorText -Color 'Cyan' -Message $Message
}

function Write-HintText {
    param([Parameter(Mandatory)][string]$Message)
    Write-ColorText -Color 'Yellow' -Message $Message
}

# ============================================================
# Directory Discovery
# ============================================================

function Find-ToolingDirectory {
    # AIDEV-NOTE: Walks up filesystem tree to find 'tooling' directory
    $currentDir = Get-Location

    # Check if we're already inside the tooling directory
    if ($currentDir.Path -match '[\\/]tooling([\\/]|$)') {
        $parts = $currentDir.Path -split '[\\/]'
        $toolingIndex = [array]::LastIndexOf($parts, 'tooling')
        $toolingPath = ($parts[0..$toolingIndex] -join [System.IO.Path]::DirectorySeparatorChar)

        if (Test-Path $toolingPath -PathType Container) {
            $Script:ToolingDir = $toolingPath
            $Script:TemplatesDir = Join-Path $Script:ToolingDir "templates"
            $Script:OutputDir = Join-Path $Script:ToolingDir "output"
            return $true
        }
    }

    # Walk up the tree looking for tooling directory
    while ($currentDir.Path -ne $currentDir.Root.Path) {
        $toolingPath = Join-Path $currentDir.Path "tooling"

        if (Test-Path $toolingPath -PathType Container) {
            $Script:ToolingDir = $toolingPath
            $Script:TemplatesDir = Join-Path $Script:ToolingDir "templates"
            $Script:OutputDir = Join-Path $Script:ToolingDir "output"
            return $true
        }

        $currentDir = $currentDir.Parent
        if (-not $currentDir) { break }
    }

    Write-ErrorText "Could not find 'tooling' directory in current path or parent directories"
    exit 1
}

function Initialize-OutputDirectory {
    # AIDEV-NOTE: Auto-creates output directory if missing
    if (-not (Test-Path $Script:OutputDir)) {
        New-Item -Path $Script:OutputDir -ItemType Directory -Force | Out-Null
    }
}

# ============================================================
# Template Discovery
# ============================================================

function Get-TemplateFiles {
    # AIDEV-NOTE: Returns sorted list of .agent.md files from agent_templates subdirectory

    if (-not (Test-Path $Script:TemplatesDir -PathType Container)) {
        Write-ErrorText "Templates directory not found: $Script:TemplatesDir"
        exit 1
    }

    $agentTemplatesDir = Join-Path $Script:TemplatesDir "agent_templates"
    if (-not (Test-Path $agentTemplatesDir -PathType Container)) {
        Write-ErrorText "Agent templates directory not found: $agentTemplatesDir"
        exit 1
    }

    $templates = Get-ChildItem -Path $agentTemplatesDir -Filter "*.agent.md" -File |
        Sort-Object Name |
        Select-Object -ExpandProperty FullName

    if ($templates.Count -eq 0) {
        Write-ErrorText "No template files found in $agentTemplatesDir"
        exit 1
    }

    return $templates
}

function Get-TemplateName {
    # AIDEV-NOTE: Strips path and .agent.md extension
    param(
        [Parameter(Mandatory)]
        [string]$TemplatePath
    )

    return [System.IO.Path]::GetFileNameWithoutExtension($TemplatePath) -replace '\.agent$', ''
}
