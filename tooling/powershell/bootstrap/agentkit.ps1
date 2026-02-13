#!/usr/bin/env pwsh
#
# agentkit.ps1 - Main CLI Entry Point
#
# Orchestrates the template engine workflow through an interactive menu system.
# Sources all modular components for template management, parsing, answers, and rendering.
#
# Usage: .\agentkit.ps1
#

# AIDEV-NOTE: Stop on errors
$ErrorActionPreference = 'Stop'

# AIDEV-NOTE: Get script directory to import relative modules
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Dot-source all library modules to bring functions and variables into script scope
. "$ScriptDir\lib\Templates.ps1"
. "$ScriptDir\lib\Parser.ps1"
. "$ScriptDir\lib\Answers.ps1"
. "$ScriptDir\lib\Rendering.ps1"

# ============================================================
# Menu System
# ============================================================

function Show-MainMenu {
    Clear-Host
    Write-HeaderText "===================================="
    Write-HeaderText "  Agent Template Engine"
    Write-HeaderText "===================================="
    Write-Host ""
    Write-Host "1. Choose an agent template"
    Write-Host "0. Exit"
    Write-Host ""
}

function Show-TemplateMenu {
    Clear-Host
    Write-HeaderText "===================================="
    Write-HeaderText "  Available Templates"
    Write-HeaderText "===================================="
    Write-Host ""

    $templates = Get-TemplateFiles

    for ($i = 0; $i -lt $templates.Count; $i++) {
        $name = Get-TemplateName -TemplatePath $templates[$i]
        Write-Host "$($i + 1). $name"
    }

    Write-Host "0. Back"
    Write-Host ""

    return $templates
}

function Show-TemplateActionsMenu {
    param([string]$TemplateName)

    Clear-Host
    Write-HeaderText "===================================="
    Write-SuccessText "  Template: $TemplateName"
    Write-HeaderText "===================================="
    Write-Host ""
    Write-Host "1. List questions"
    Write-Host "2. Show template content"
    Write-Host "3. Define agent (interactive Q&A)"
    Write-Host "4. Generate prompt file"
    Write-Host "0. Back"
    Write-Host ""
}

# ============================================================
# Menu Actions
# ============================================================

function Invoke-ListQuestions {
    param([string]$TemplatePath)

    $templateContent = Get-Content $TemplatePath -Raw
    $prompts = Get-PromptDefinitions -TemplateContent $templateContent

    Write-HeaderText "Questions defined in template:"
    Write-Host ""

    foreach ($promptHash in $prompts) {
        $prompt = ConvertTo-PromptObject -PromptHash $promptHash

        Write-Host "ID: $($prompt.Id)"
        Write-Host "  Question: $($prompt.Question)"

        if ($prompt.Hint) {
            Write-Host "  Hint: $($prompt.Hint)"
        }

        Write-Host "  Format: $($prompt.Format)"

        if ($prompt.Default) {
            Write-Host "  Default: $($prompt.Default)"
        }

        Write-Host ""
    }

    Read-Host "Press Enter to continue"
}

function Invoke-ShowContent {
    param([string]$TemplatePath)

    Write-HeaderText "Template content:"
    Write-Host ""
    Get-Content $TemplatePath
    Write-Host ""
    Read-Host "Press Enter to continue"
}

function Invoke-DefineAgent {
    param(
        [string]$TemplatePath,
        [string]$TemplateName
    )

    $templateContent = Get-Content $TemplatePath -Raw

    Write-HeaderText "Starting interactive Q&A for: $TemplateName"
    Write-Host ""

    # Extract all prompt definitions
    $prompts = Get-PromptDefinitions -TemplateContent $templateContent

    if ($prompts.Count -eq 0) {
        Write-ErrorText "No prompts found in template"
        Read-Host "Press Enter to continue"
        return
    }

    # Collect answers for each prompt
    $answers = @{}

    foreach ($promptHash in $prompts) {
        $prompt = ConvertTo-PromptObject -PromptHash $promptHash
        $answer = Read-Answer -Prompt $prompt
        $answers[$prompt.Id] = $answer
        Write-Host ""
    }

    # Generate answers file
    $answersPath = New-AnswersFile -TemplateName $TemplateName -Answers $answers -OutputDirectory $Script:OutputDir

    Write-SuccessText "Answers saved to: $answersPath"
    Write-Host ""

    $generatePrompt = Read-Host "Would you like to generate the prompt file now? [Y/n]"
    if ([string]::IsNullOrWhiteSpace($generatePrompt)) { $generatePrompt = "Y" }

    if ($generatePrompt -match '^[Yy]') {
        Invoke-GeneratePromptInternal -AnswersFilePath $answersPath -TemplatePath $TemplatePath -TemplateName $TemplateName
    }

    Read-Host "Press Enter to continue"
}

function Invoke-GeneratePrompt {
    param(
        [string]$TemplatePath,
        [string]$TemplateName
    )

    $answersFile = Join-Path $Script:OutputDir "${TemplateName}.answers.md"

    if (-not (Test-Path $answersFile)) {
        Write-ErrorText "Answers file not found: $answersFile"
        Write-Host "Please run 'Define agent' first to create the answers file."
        Read-Host "Press Enter to continue"
        return
    }

    Invoke-GeneratePromptInternal -AnswersFilePath $answersFile -TemplatePath $TemplatePath -TemplateName $TemplateName
    Read-Host "Press Enter to continue"
}

function Invoke-GeneratePromptInternal {
    param(
        [string]$AnswersFilePath,
        [string]$TemplatePath,
        [string]$TemplateName
    )

    $templateContent = Get-Content $TemplatePath -Raw

    # Parse answers from file
    $answers = Get-AnswersFromFile -AnswersFilePath $AnswersFilePath

    # Render template
    $rendered = Invoke-TemplateRendering -TemplateContent $templateContent -Answers $answers

    # Generate prompt file
    $promptPath = New-PromptFile -RenderedContent $rendered -AgentName $TemplateName -ToolingDirectory $Script:ToolingDir -OutputDirectory $Script:OutputDir

    Write-SuccessText "Prompt file generated: $promptPath"
}

# ============================================================
# Menu Navigation
# ============================================================

function Start-TemplateActionsLoop {
    param(
        [string]$TemplatePath,
        [string]$TemplateName
    )

    while ($true) {
        Show-TemplateActionsMenu -TemplateName $TemplateName
        $choice = Read-Host "Select an option"

        switch ($choice) {
            "1" { Invoke-ListQuestions -TemplatePath $TemplatePath }
            "2" { Invoke-ShowContent -TemplatePath $TemplatePath }
            "3" { Invoke-DefineAgent -TemplatePath $TemplatePath -TemplateName $TemplateName }
            "4" { Invoke-GeneratePrompt -TemplatePath $TemplatePath -TemplateName $TemplateName }
            "0" { return }
            default {
                Write-ErrorText "Invalid choice. Please try again."
                Start-Sleep -Seconds 1
            }
        }
    }
}

function Start-TemplateSelectionLoop {
    while ($true) {
        $templates = Show-TemplateMenu
        $choice = Read-Host "Select a template"

        if ($choice -eq "0") {
            return
        }

        # Validate choice is a number within range
        $choiceNum = 0
        if ([int]::TryParse($choice, [ref]$choiceNum)) {
            if ($choiceNum -gt 0 -and $choiceNum -le $templates.Count) {
                $idx = $choiceNum - 1
                $templatePath = $templates[$idx]
                $templateName = Get-TemplateName -TemplatePath $templatePath

                Start-TemplateActionsLoop -TemplatePath $templatePath -TemplateName $templateName
            } else {
                Write-ErrorText "Invalid choice. Please try again."
                Start-Sleep -Seconds 1
            }
        } else {
            Write-ErrorText "Invalid choice. Please try again."
            Start-Sleep -Seconds 1
        }
    }
}

function Start-MainMenuLoop {
    while ($true) {
        Show-MainMenu
        $choice = Read-Host "Select an option"

        switch ($choice) {
            "1" { Start-TemplateSelectionLoop }
            "0" {
                Write-ColorText -Color 'Yellow' -Message "Goodbye!"
                exit 0
            }
            default {
                Write-ErrorText "Invalid choice. Please try again."
                Start-Sleep -Seconds 1
            }
        }
    }
}

# ============================================================
# Main Entry Point
# ============================================================

function Main {
    Find-ToolingDirectory
    Start-MainMenuLoop
}

# Run main
Main
