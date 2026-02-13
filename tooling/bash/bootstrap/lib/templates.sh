#!/usr/bin/env bash
#
# templates.sh - Template Discovery & Management
#
# Handles template file discovery, path management, and directory operations.
#

# AIDEV-NOTE: Color codes for consistent terminal output matching Python CLI
readonly COLOR_RESET='\033[0m'
readonly COLOR_CYAN='\033[36m'
readonly COLOR_GREEN='\033[32m'
readonly COLOR_YELLOW='\033[33m'
readonly COLOR_RED='\033[31m'
readonly COLOR_BLUE='\033[34m'
readonly COLOR_DIM='\033[2m'

# AIDEV-NOTE: Global state for current working context
TOOLING_DIR=""
TEMPLATES_DIR=""
OUTPUT_DIR=""
CURRENT_TEMPLATE_PATH=""
CURRENT_TEMPLATE_NAME=""

# ============================================================
# Utility Functions
# ============================================================

print_color() {
    local color="$1"
    shift
    echo -e "${color}$*${COLOR_RESET}"
}

print_error() {
    print_color "$COLOR_RED" "ERROR: $*" >&2
}

print_success() {
    print_color "$COLOR_GREEN" "$*"
}

print_header() {
    print_color "$COLOR_CYAN" "$*"
}

print_hint() {
    print_color "$COLOR_DIM" "$*"
}

# ============================================================
# Directory Discovery
# ============================================================

find_tooling_dir() {
    # AIDEV-NOTE: Walks up filesystem tree to find 'tooling' directory
    local current_dir="$PWD"

    while [[ "$current_dir" != "/" ]]; do
        if [[ -d "$current_dir/tooling" ]]; then
            TOOLING_DIR="$current_dir/tooling"
            TEMPLATES_DIR="$TOOLING_DIR/templates"
            OUTPUT_DIR="$TOOLING_DIR/output"
            return 0
        fi
        current_dir="$(dirname "$current_dir")"
    done

    print_error "Could not find 'tooling' directory in current path or parent directories"
    exit 1
}

ensure_output_dir() {
    # AIDEV-NOTE: Auto-creates output directory if missing
    mkdir -p "$OUTPUT_DIR"
}

# ============================================================
# Template Discovery
# ============================================================

discover_templates() {
    # AIDEV-NOTE: Returns sorted list of .agent.md files from agent_templates subdirectory
    local -a templates=()

    if [[ ! -d "$TEMPLATES_DIR" ]]; then
        print_error "Templates directory not found: $TEMPLATES_DIR"
        exit 1
    fi

    local agent_templates_dir="$TEMPLATES_DIR/agent_templates"
    if [[ ! -d "$agent_templates_dir" ]]; then
        print_error "Agent templates directory not found: $agent_templates_dir"
        exit 1
    fi

    while IFS= read -r template_file; do
        templates+=("$template_file")
    done < <(find "$agent_templates_dir" -maxdepth 1 -name "*.agent.md" -type f | sort)

    if [[ ${#templates[@]} -eq 0 ]]; then
        print_error "No template files found in $agent_templates_dir"
        exit 1
    fi

    printf '%s\n' "${templates[@]}"
}

extract_template_name() {
    # AIDEV-NOTE: Strips path and .agent.md extension
    local template_path="$1"
    basename "$template_path" .agent.md
}
