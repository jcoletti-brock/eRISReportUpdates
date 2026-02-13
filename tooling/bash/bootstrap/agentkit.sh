#!/usr/bin/env bash
#
# agentkit.sh - Main CLI Entry Point
#
# Orchestrates the template engine workflow through an interactive menu system.
# Sources all modular components for template management, parsing, answers, and rendering.
#
# Usage: ./agentkit.sh
#

set -euo pipefail

# AIDEV-NOTE: Get script directory to source relative modules
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source all library modules
source "$SCRIPT_DIR/lib/templates.sh"
source "$SCRIPT_DIR/lib/parser.sh"
source "$SCRIPT_DIR/lib/answers.sh"
source "$SCRIPT_DIR/lib/rendering.sh"

# ============================================================
# Menu System
# ============================================================

show_main_menu() {
    clear
    print_header "===================================="
    print_header "  Agent Template Engine"
    print_header "===================================="
    echo ""
    echo "1. Choose an agent template"
    echo "0. Exit"
    echo ""
}

show_template_menu() {
    clear
    print_header "===================================="
    print_header "  Available Templates"
    print_header "===================================="
    echo ""

    local -a templates=()
    mapfile -t templates < <(discover_templates)

    local i=1
    for template in "${templates[@]}"; do
        local name
        name=$(extract_template_name "$template")
        echo "$i. $name"
        ((i++))
    done

    echo "0. Back"
    echo ""
}

show_template_actions_menu() {
    clear
    print_header "===================================="
    print_success "  Template: $CURRENT_TEMPLATE_NAME"
    print_header "===================================="
    echo ""
    echo "1. List questions"
    echo "2. Show template content"
    echo "3. Define agent (interactive Q&A)"
    echo "4. Generate prompt file"
    echo "0. Back"
    echo ""
}

# ============================================================
# Menu Actions
# ============================================================

action_list_questions() {
    local template_content
    template_content=$(<"$CURRENT_TEMPLATE_PATH")

    local temp_file
    temp_file=$(mktemp)
    extract_prompt_definitions "$template_content" > "$temp_file"

    print_header "Questions defined in template:"
    echo ""

    local -A prompt
    while IFS= read -r line; do
        if [[ "$line" == PROMPT_ID:* ]]; then
            # Reset for new prompt
            prompt=()
        fi

        if ! parse_prompt_block prompt < <(cat "$temp_file"); then
            break
        fi

        echo "ID: ${prompt[id]}"
        echo "  Question: ${prompt[question]}"
        [[ -n "${prompt[hint]}" ]] && echo "  Hint: ${prompt[hint]}"
        echo "  Format: ${prompt[format]}"
        [[ -n "${prompt[default]}" ]] && echo "  Default: ${prompt[default]}"
        echo ""
    done < "$temp_file"

    rm "$temp_file"

    read -r -p "Press Enter to continue..."
}

action_show_content() {
    print_header "Template content:"
    echo ""
    cat "$CURRENT_TEMPLATE_PATH"
    echo ""
    read -r -p "Press Enter to continue..."
}

action_define_agent() {
    local template_content
    template_content=$(<"$CURRENT_TEMPLATE_PATH")

    print_header "Starting interactive Q&A for: $CURRENT_TEMPLATE_NAME"
    echo ""

    # Extract all prompt definitions
    local temp_prompts
    temp_prompts=$(mktemp)
    extract_prompt_definitions "$template_content" > "$temp_prompts"

    # Collect answers for each prompt
    local -a answer_ids=()

    # Parse the prompt definitions
    local -A current_prompt
    local id="" question="" hint="" format="" default=""

    while IFS=: read -r key value; do
        case "$key" in
            PROMPT_ID)
                id="$value"
                question=""
                hint=""
                format="text"
                default=""
                ;;
            QUESTION) question="$value" ;;
            HINT) hint="$value" ;;
            FORMAT) format="$value" ;;
            DEFAULT) default="$value" ;;
            END_PROMPT)
                if [[ -n "$id" ]]; then
                    # Build prompt associative array
                    current_prompt[id]="$id"
                    current_prompt[question]="${question:-Value for $id?}"
                    current_prompt[hint]="${hint}"
                    current_prompt[format]="${format:-text}"
                    current_prompt[default]="${default}"

                    # Collect answer from user
                    local answer
                    answer=$(collect_answer current_prompt)

                    # Store answer with ANSWER_ prefix for later reference
                    declare -g "ANSWER_${id}=$answer"
                    answer_ids+=("$id")
                    echo ""

                    # Reset for next prompt
                    id=""
                fi
                ;;
        esac
    done < "$temp_prompts"

    rm "$temp_prompts"

    # Check if any answers were collected
    if [[ ${#answer_ids[@]} -eq 0 ]]; then
        print_error "No prompts found in template"
        read -r -p "Press Enter to continue..."
        return
    fi

    # Generate answers file
    local answers_path
    answers_path=$(generate_answers_file "$CURRENT_TEMPLATE_NAME" "${answer_ids[@]}")

    print_success "Answers saved to: $answers_path"
    echo ""

    read -r -p "Would you like to generate the prompt file now? [Y/n]: " generate_prompt
    generate_prompt="${generate_prompt:-Y}"

    if [[ "$generate_prompt" =~ ^[Yy] ]]; then
        action_generate_prompt_internal "$answers_path"
    fi

    read -r -p "Press Enter to continue..."
}

action_generate_prompt() {
    # Interactive version - asks for answers file
    local answers_file="$OUTPUT_DIR/${CURRENT_TEMPLATE_NAME}.answers.md"

    if [[ ! -f "$answers_file" ]]; then
        print_error "Answers file not found: $answers_file"
        echo "Please run 'Define agent' first to create the answers file."
        read -r -p "Press Enter to continue..."
        return
    fi

    action_generate_prompt_internal "$answers_file"
    read -r -p "Press Enter to continue..."
}

action_generate_prompt_internal() {
    # Internal version - takes answers file path as argument
    local answers_file="$1"
    local template_content
    template_content=$(<"$CURRENT_TEMPLATE_PATH")

    # Parse answers from file
    declare -A answers
    local temp_answers
    temp_answers=$(mktemp)
    parse_answers_file "$answers_file" > "$temp_answers"

    local current_id=""
    local -a content_lines=()
    local in_content=false

    while IFS= read -r line; do
        if [[ "$line" == ANSWER_ID:* ]]; then
            # Save previous answer if exists
            if [[ -n "$current_id" ]]; then
                answers["$current_id"]=$(printf '%s\n' "${content_lines[@]}")
            fi

            current_id="${line#ANSWER_ID:}"
            content_lines=()
            in_content=false
        elif [[ "$line" == "CONTENT_START" ]]; then
            in_content=true
        elif [[ "$line" == "CONTENT_END" ]]; then
            in_content=false
        elif [[ "$in_content" == true ]]; then
            content_lines+=("$line")
        fi
    done < "$temp_answers"

    # Save last answer
    if [[ -n "$current_id" ]]; then
        answers["$current_id"]=$(printf '%s\n' "${content_lines[@]}")
    fi

    rm "$temp_answers"

    # Render template
    local rendered
    rendered=$(render_template "$template_content" answers)

    # Generate prompt file
    local prompt_path
    prompt_path=$(generate_prompt_file "$rendered" "$CURRENT_TEMPLATE_NAME")

    print_success "Prompt file generated: $prompt_path"
}

# ============================================================
# Menu Navigation
# ============================================================

template_actions_loop() {
    while true; do
        show_template_actions_menu
        read -r -p "Select an option: " choice

        case "$choice" in
            1) action_list_questions ;;
            2) action_show_content ;;
            3) action_define_agent ;;
            4) action_generate_prompt ;;
            0) return ;;
            *) print_error "Invalid choice. Please try again." ;;
        esac
    done
}

template_selection_loop() {
    local -a templates
    mapfile -t templates < <(discover_templates)

    while true; do
        show_template_menu
        read -r -p "Select a template: " choice

        if [[ "$choice" == "0" ]]; then
            return
        fi

        if [[ "$choice" =~ ^[0-9]+$ ]] && ((choice > 0 && choice <= ${#templates[@]})); then
            local idx=$((choice - 1))
            CURRENT_TEMPLATE_PATH="${templates[$idx]}"
            CURRENT_TEMPLATE_NAME=$(extract_template_name "$CURRENT_TEMPLATE_PATH")
            template_actions_loop
        else
            print_error "Invalid choice. Please try again."
            sleep 1
        fi
    done
}

main_menu_loop() {
    while true; do
        show_main_menu
        read -r -p "Select an option: " choice

        case "$choice" in
            1) template_selection_loop ;;
            0)
                print_color "$COLOR_YELLOW" "Goodbye!"
                exit 0
                ;;
            *)
                print_error "Invalid choice. Please try again."
                sleep 1
                ;;
        esac
    done
}

# ============================================================
# Main Entry Point
# ============================================================

main() {
    find_tooling_dir
    main_menu_loop
}

main "$@"
