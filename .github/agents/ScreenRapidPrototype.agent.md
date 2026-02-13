---
description: 'Screen Rapid Prototype is a simple and quick exercise to create a single page web application using HTML, CSS, and JavaScript. The focus is on functionality rather than design perfection.'
---
# Screen Rapid Prototype

Our goal is to create a single page web application. The intent is to do this exercise as simply and quickly as possible.

- Stick to the basics, no need for complex frameworks or libraries.
- Use HTML, CSS, and JavaScript to create a functional prototype.
- Focus on getting elements on the page, not on perfecting the design, coding style, performance, or security standards.

## Where to do the work

- We have a workspace set up in the `frontend/prototypeplayground` folder found in this workspace.
  - Create, Delete, or Modify files in this folder.
  - Don't modify, create or delete any files outside of this folder.
  - You can reference any files in the workspace.

## Project Structure

- This is a simple `flask` application.

  - The main entry point is `app.py`.
  - The application is structured to serve static files.
  - The `static` folder contains HTML, CSS and JavaScript files.

- Use `playground.html`, and `styles.css` as the main file to work on.
- You can create other files, but they need to be in the `static` folder.

## Styling

- **Tailwind CSS** is available locally at `/static/tailwind.min.css` for rapid prototyping with utility classes.
- ALWAYS Use Tailwind utility classes (e.g., `flex`, `w-1/3`, `bg-white`, `shadow-lg`) for layout and basic styling.
  - ONLY if no viable tailwind utility class exists, use custom CSS in `styles.css`.
- Follow [Tailwind CSS documentation](https://tailwindcss.com/docs/styling-with-utility-classes) documentation
- NEVER define styles in HTML files - use Tailwind classes or add to `styles.css`.

## Scripting

- NEVER define javascript in the HTML files.
- Use the `playground_scripts.js` file for all JavaScript code.
