#!/usr/bin/env pwsh
#
# Test-Templates.ps1 - Test script for Templates.ps1 module
#

$ErrorActionPreference = 'Stop'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Import the module
Import-Module "$ScriptDir\..\lib\Templates.ps1" -Force

Write-Host "=== Testing Templates.ps1 Module ===" -ForegroundColor Cyan
Write-Host ""

# Test 1: Color output functions
Write-Host "Test 1: Color output functions" -ForegroundColor Yellow
Write-ColorText -Color 'Cyan' -Message "  Cyan text test"
Write-ColorText -Color 'Green' -Message "  Green text test"
Write-ColorText -Color 'Red' -Message "  Red text test"
Write-ColorText -Color 'Blue' -Message "  Blue text test"
Write-ColorText -Color 'Dim' -Message "  Dim text test"
Write-Host "  ✓ Color functions working" -ForegroundColor Green
Write-Host ""

# Test 2: Directory discovery
Write-Host "Test 2: Find tooling directory" -ForegroundColor Yellow
try {
    Find-ToolingDirectory
    Write-Host "  ✓ Tooling directory found: $Script:ToolingDir" -ForegroundColor Green
    Write-Host "  ✓ Templates directory: $Script:TemplatesDir" -ForegroundColor Green
    Write-Host "  ✓ Output directory: $Script:OutputDir" -ForegroundColor Green
} catch {
    Write-Host "  ✗ Failed to find tooling directory: $_" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Test 3: Output directory initialization
Write-Host "Test 3: Initialize output directory" -ForegroundColor Yellow
try {
    Initialize-OutputDirectory
    if (Test-Path $Script:OutputDir) {
        Write-Host "  ✓ Output directory exists: $Script:OutputDir" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Output directory not created" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "  ✗ Failed to initialize output directory: $_" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Test 4: Template discovery
Write-Host "Test 4: Discover template files" -ForegroundColor Yellow
try {
    $templates = Get-TemplateFiles
    Write-Host "  ✓ Found $($templates.Count) template(s)" -ForegroundColor Green
    foreach ($template in $templates) {
        $name = Get-TemplateName -TemplatePath $template
        Write-Host "    - $name" -ForegroundColor Cyan
    }
} catch {
    Write-Host "  ✗ Failed to discover templates: $_" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Test 5: Extract template name
Write-Host "Test 5: Extract template names" -ForegroundColor Yellow
try {
    foreach ($template in $templates) {
        $name = Get-TemplateName -TemplatePath $template
        if ($name) {
            Write-Host "  ✓ $template → $name" -ForegroundColor Green
        } else {
            Write-Host "  ✗ Failed to extract name from: $template" -ForegroundColor Red
            exit 1
        }
    }
} catch {
    Write-Host "  ✗ Failed to extract template names: $_" -ForegroundColor Red
    exit 1
}
Write-Host ""

Write-Host "=== All Tests Passed ===" -ForegroundColor Green
