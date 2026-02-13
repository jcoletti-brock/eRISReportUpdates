#
# Parser.ps1 - Prompt Block & Placeholder Parsing
#
# Handles extraction and parsing of PROMPT blocks, placeholders, and ANSWER blocks.
#

# ============================================================
# Prompt Block Parsing
# ============================================================

function Get-PromptDefinitions {
    # AIDEV-NOTE: Extracts all {{PROMPT: id ...}} blocks from template
    param(
        [Parameter(Mandatory)]
        [string]$TemplateContent
    )

    $results = @()

    # Regex to match PROMPT blocks with multiline content
    $promptPattern = '\{\{PROMPT:\s*(\w+)\s*([\s\S]*?)\}\}'

    $matches = [regex]::Matches($TemplateContent, $promptPattern)

    foreach ($match in $matches) {
        $id = $match.Groups[1].Value
        $fields = $match.Groups[2].Value

        $prompt = @{
            id = $id
        }

        # Extract question
        if ($fields -match 'question:\s*"([^"]*)"') {
            $prompt.question = $Matches[1]
        }

        # Extract hint
        if ($fields -match 'hint:\s*"([^"]*)"') {
            $prompt.hint = $Matches[1]
        }

        # Extract format
        if ($fields -match 'format:\s*"([^"]*)"') {
            $prompt.format = $Matches[1]
        } else {
            $prompt.format = "text"
        }

        # Extract default
        if ($fields -match 'default:\s*"([^"]*)"') {
            $prompt.default = $Matches[1]
        }

        $results += $prompt
    }

    return $results
}

function ConvertTo-PromptObject {
    # AIDEV-NOTE: Converts hashtable to PSCustomObject for easier property access
    param(
        [Parameter(Mandatory)]
        [hashtable]$PromptHash
    )

    return [PSCustomObject]@{
        Id       = $PromptHash.id
        Question = if ($PromptHash.question) { $PromptHash.question } else { "Value for $($PromptHash.id)?" }
        Hint     = if ($PromptHash.hint) { $PromptHash.hint } else { "" }
        Format   = if ($PromptHash.format) { $PromptHash.format } else { "text" }
        Default  = if ($PromptHash.default) { $PromptHash.default } else { "" }
    }
}

# ============================================================
# Placeholder Detection
# ============================================================

function Get-Placeholders {
    # AIDEV-NOTE: Extracts unique {{id}} placeholders in order of appearance
    param(
        [Parameter(Mandatory)]
        [string]$TemplateContent
    )

    $placeholderPattern = '\{\{(\w+)\}\}'
    $matches = [regex]::Matches($TemplateContent, $placeholderPattern)

    $seen = @{}
    $placeholders = @()

    foreach ($match in $matches) {
        $placeholder = $match.Groups[1].Value

        if (-not $seen.ContainsKey($placeholder)) {
            $seen[$placeholder] = $true
            $placeholders += $placeholder
        }
    }

    return $placeholders
}

# ============================================================
# Answers File Parsing
# ============================================================

function Get-AnswersFromFile {
    # AIDEV-NOTE: Parses {{ANSWER: id user_response: | ...}} blocks
    param(
        [Parameter(Mandatory)]
        [string]$AnswersFilePath
    )

    if (-not (Test-Path $AnswersFilePath)) {
        throw "Answers file not found: $AnswersFilePath"
    }

    $content = Get-Content $AnswersFilePath -Raw
    $answers = @{}

    # Regex to match ANSWER blocks with multiline YAML literal block syntax
    $answerPattern = '\{\{ANSWER:\s*(\w+)\s+user_response:\s*\|\s*\n([\s\S]*?)\}\}'

    $matches = [regex]::Matches($content, $answerPattern)

    foreach ($match in $matches) {
        $id = $match.Groups[1].Value
        $response = $match.Groups[2].Value

        # Dedent by removing leading 4 spaces from each line
        $lines = $response -split "`n"
        $dedentedLines = $lines | ForEach-Object {
            if ($_ -match '^    (.*)$') {
                $Matches[1]
            } else {
                $_
            }
        }

        # Join and trim trailing whitespace
        $cleanedResponse = ($dedentedLines -join "`n").TrimEnd()

        $answers[$id] = $cleanedResponse
    }

    return $answers
}
