#!/usr/bin/env bash
#
# rendering.sh - Template Rendering & Prompt Generation
#
# Handles template rendering with answer substitution and prompt file generation.
#

# ============================================================
# Template Rendering
# ============================================================

render_template() {
    # AIDEV-NOTE: Removes PROMPT blocks, replaces placeholders with answers
    local template_content="$1"
    local -n answers_map=$2

    # Step 1: Remove all PROMPT definition blocks
    template_content=$(echo "$template_content" | perl -0777 -pe 's/\{\{PROMPT:\s*\w+\s*[\s\S]*?\}\}\s*\n?//g')

    # Step 2: Normalize consecutive newlines (3+ becomes 2)
    template_content=$(echo "$template_content" | perl -0777 -pe 's/\n{3,}/\n\n/g')

    # Step 3: Replace placeholders with answer values
    local rendered="$template_content"
    for id in "${!answers_map[@]}"; do
        local value="${answers_map[$id]}"
        # Escape special chars for sed
        local escaped_value
        escaped_value=$(printf '%s\n' "$value" | sed 's/[&/\]/\\&/g')
        rendered=$(echo "$rendered" | perl -pe "s/\{\{$id\}\}/$escaped_value/g")
    done

    echo "$rendered"
}

# ============================================================
# Prompt File Generation
# ============================================================

generate_prompt_file() {
    local rendered_content="$1"
    local agent_name="$2"
    local prompt_template_path="$TOOLING_DIR/templates/generate_agent.prompt.template.md"
    local output_path="$OUTPUT_DIR/create_${agent_name}.prompt.md"

    if [[ ! -f "$prompt_template_path" ]]; then
        print_error "Prompt template not found: $prompt_template_path"
        exit 1
    fi

    ensure_output_dir

    # Load template and substitute placeholders
    local prompt_template
    prompt_template=$(<"$prompt_template_path")

    # Replace {{RENDERED_CONTENT}} and {{AGENT_NAME}}
    local final_content
    final_content="${prompt_template//\{\{RENDERED_CONTENT\}\}/$rendered_content}"
    final_content="${final_content//\{\{AGENT_NAME\}\}/$agent_name}"

    echo "$final_content" > "$output_path"
    echo "$output_path"
}
