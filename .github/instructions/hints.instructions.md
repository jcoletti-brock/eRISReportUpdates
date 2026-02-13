---
applyTo: "**"
---

# General hints

This document gives hints for general techniques and patterns we'd like to use when working in this workspace.

## Content Replacement

- When doing broad content replacement in files, use a command like `sed` for efficiency.

## Grep Tool (`functions.grep_search`)

1. Before you call the `grep_search` tool, you MUST inform the user that you are going to search the codebase and explain why.

## Searching the web

You can use the `functions.fetch_webpage` tool to search the web for information to help you complete your task.

1. Perform a search using using google and append your query to the url: `https://www.google.com/search?q=`
2. Use the `fetch_webpage` tool to retrieve the search results.
3. Review the content returned by the fetch tool.
4. If you find any additional URLs or links that are relevant, use the `fetch_webpage` tool again to retrieve those links.
5. Go back to step 3 and repeat until you have all the information you need.

# API, Framework and Library Documentation Retrieval

**ALWAYS** When answering questions about frameworks, libraries, or APIs, use #context7 to retrieve current documentation rather than relying on training data
