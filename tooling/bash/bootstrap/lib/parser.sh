#!/usr/bin/env bash
#
# parser.sh - Prompt Block & Placeholder Parsing
#
# Handles extraction and parsing of PROMPT blocks, placeholders, and ANSWER blocks.
#

# ============================================================
# Prompt Block Parsing
# ============================================================

extract_prompt_definitions() {
    # AIDEV-NOTE: Extracts all {{PROMPT: id ...}} blocks from template
    local template_content="$1"
    local temp_file
    temp_file=$(mktemp)

    # Use Perl for multiline regex matching (more reliable than sed/awk)
    echo "$template_content" | perl -0777 -ne '
        while (/\{\{PROMPT:\s*(\w+)\s*([\s\S]*?)\}\}/g) {
            my $id = $1;
            my $fields = $2;
            print "PROMPT_ID:$id\n";

            # Extract question, hint, format, default
            if ($fields =~ /question:\s*"([^"]*)"/) {
                print "QUESTION:$1\n";
            }
            if ($fields =~ /hint:\s*"([^"]*)"/) {
                print "HINT:$1\n";
            }
            if ($fields =~ /format:\s*"([^"]*)"/) {
                print "FORMAT:$1\n";
            }
            if ($fields =~ /default:\s*"([^"]*)"/) {
                print "DEFAULT:$1\n";
            }
            print "END_PROMPT\n";
        }
    ' > "$temp_file"

    cat "$temp_file"
    rm "$temp_file"
}

parse_prompt_block() {
    # AIDEV-NOTE: Parses a single prompt definition into associative array
    local -n prompt_def=$1
    local id question hint format default

    while IFS=: read -r key value; do
        case "$key" in
            PROMPT_ID) id="$value" ;;
            QUESTION) question="$value" ;;
            HINT) hint="$value" ;;
            FORMAT) format="${value:-text}" ;;
            DEFAULT) default="$value" ;;
            END_PROMPT)
                prompt_def[id]="$id"
                prompt_def[question]="${question:-Value for $id?}"
                prompt_def[hint]="${hint:-}"
                prompt_def[format]="${format:-text}"
                prompt_def[default]="${default:-}"
                return 0
                ;;
        esac
    done
}

# ============================================================
# Placeholder Detection
# ============================================================

extract_placeholders() {
    # AIDEV-NOTE: Extracts unique {{id}} placeholders in order of appearance
    local template_content="$1"
    local -a placeholders=()
    local -A seen=()

    while read -r placeholder; do
        if [[ -z "${seen[$placeholder]:-}" ]]; then
            seen[$placeholder]=1
            placeholders+=("$placeholder")
        fi
    done < <(echo "$template_content" | grep -oP '\{\{(\w+)\}\}' | sed 's/[{}]//g' | sort -u)

    printf '%s\n' "${placeholders[@]}"
}

# ============================================================
# Answers File Parsing
# ============================================================

parse_answers_file() {
    # AIDEV-NOTE: Parses {{ANSWER: id user_response: | ...}} blocks
    local answers_file="$1"
    local temp_file
    temp_file=$(mktemp)

    perl -0777 -ne '
        while (/\{\{ANSWER:\s*(\w+)\s+user_response:\s*\|\s*\n([\s\S]*?)\}\}/g) {
            my $id = $1;
            my $content = $2;

            # Dedent by removing leading 4 spaces
            $content =~ s/^    //gm;
            $content =~ s/\s+$//;  # Trim trailing whitespace

            print "ANSWER_ID:$id\n";
            print "CONTENT_START\n";
            print "$content\n";
            print "CONTENT_END\n";
        }
    ' "$answers_file" > "$temp_file"

    cat "$temp_file"
    rm "$temp_file"
}
