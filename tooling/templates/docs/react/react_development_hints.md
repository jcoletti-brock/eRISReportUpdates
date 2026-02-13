# Hints when developing with React in this project

## React Component Discovery

ALWAYS use #react-component-discovery MCP as the first step instead of searching the filesystem. This provides:

- Complete component inventory with references to documentation
- Faster discovery than file system searches

Use the MCP tools in this order:

1. `mcp_react-compone_list_components` - Get complete component overview
2. `mcp_react-compone_search_components` - Search for specific components by functionality
3. `mcp_react-compone_get_component_details` - Get comprehensive component information
4. `mcp_react-compone_get_component_documentation` - Access component documentation

Only fall back to file system searches if the MCP doesn't contain the information needed or instructed by the user.

## Timers and Timing

When working with timers in React, prefer to leverage the app timer.
Review `frontend/ReactWebApp/react-dev-template/src/app/apptimer/README.md` documents for implementation details.

## Linting

When finished editing React files, run the linter to ensure we have no outstanding errors.
How to lint: run `npm run lint` in the react-dev-template folder.
