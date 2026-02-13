#
# Rendering.ps1 - Template Rendering & Prompt Generation
#
# Handles template rendering with answer substitution and prompt file generation.
#

# Dot-source Templates module for utilities
. "$PSScriptRoot\Templates.ps1"

# ============================================================
# Template Rendering
# ============================================================

function Invoke-TemplateRendering {
    # AIDEV-NOTE: Removes PROMPT blocks, replaces placeholders with answers
    param(
        [Parameter(Mandatory)]
        [string]$TemplateContent,

        [Parameter(Mandatory)]
        [hashtable]$Answers
    )

    # Step 1: Remove all PROMPT definition blocks
    $promptPattern = '\{\{PROMPT:\s*\w+\s*[\s\S]*?\}\}\s*\r?\n?'
    $rendered = $TemplateContent -replace $promptPattern, ''

    # Step 2: Normalize consecutive newlines (3+ becomes 2)
    $rendered = $rendered -replace '(\r?\n){3,}', "`n`n"

    # Step 3: Replace placeholders with answer values
    foreach ($id in $Answers.Keys) {
        $value = $Answers[$id]

        # Escape regex special characters in the placeholder ID
        $escapedId = [regex]::Escape($id)
        $placeholderPattern = "\{\{$escapedId\}\}"

        # Replace all occurrences of this placeholder
        $rendered = $rendered -replace $placeholderPattern, $value
    }

    return $rendered
}

# ============================================================
# Prompt File Generation
# ============================================================

function New-PromptFile {
    param(
        [Parameter(Mandatory)]
        [string]$RenderedContent,

        [Parameter(Mandatory)]
        [string]$AgentName,

        [Parameter(Mandatory)]
        [string]$ToolingDirectory,

        [Parameter(Mandatory)]
        [string]$OutputDirectory
    )

    $promptTemplatePath = Join-Path $ToolingDirectory "templates\generate_agent.prompt.template.md"
    $outputPath = Join-Path $OutputDirectory "create_${AgentName}.prompt.md"

    if (-not (Test-Path $promptTemplatePath)) {
        Write-ErrorText "Prompt template not found: $promptTemplatePath"
        exit 1
    }

    # Ensure output directory exists
    if (-not (Test-Path $OutputDirectory)) {
        New-Item -Path $OutputDirectory -ItemType Directory -Force | Out-Null
    }

    # Load template and substitute placeholders
    $promptTemplate = Get-Content $promptTemplatePath -Raw

    # Replace {{RENDERED_CONTENT}} and {{AGENT_NAME}}
    $finalContent = $promptTemplate -replace '\{\{RENDERED_CONTENT\}\}', $RenderedContent
    $finalContent = $finalContent -replace '\{\{AGENT_NAME\}\}', $AgentName

    $finalContent | Set-Content -Path $outputPath -NoNewline

    return $outputPath
}
