# Technical Specification

## Project

**Name:** note-manager-cli

**Language:** Python 3

**Project Type:** Command Line Interface (CLI)

------------------------------------------------------------------------

# Purpose

`note-manager-cli` is a learning project whose goal is to build a
maintainable note management application while following professional
software engineering practices.

------------------------------------------------------------------------

# Current Features

## Implemented

-   Create note
-   View all notes
-   Edit note
-   Delete note
-   Search notes by tag (case-insensitive)

------------------------------------------------------------------------

# Note Model

Each note is stored as a dictionary.

Example:

``` python
{
    "title": "Python",
    "content": "Read chapter 3",
    "tags": ["python", "study"]
}
```

All notes are stored in:

``` text
data/notes.json
```

------------------------------------------------------------------------

# Project Structure

``` text
main.py          # Application entry point
menu.py          # CLI menu
notes.py         # Business logic
storage.py       # JSON persistence
constants.py     # Shared constants
utils.py         # Helper functions

data/
docs/
```

------------------------------------------------------------------------

# Architecture Principles

-   Separation of responsibilities.
-   Small, focused functions.
-   Reusable helper functions.
-   Clear naming.
-   Documentation-first development.
-   Feature-first Git workflow.

------------------------------------------------------------------------

# Development Process

Every new feature follows the same lifecycle:

1.  Requirements
2.  Architecture discussion
3.  Activity Diagram
4.  Design Review
5.  Implementation
6.  Code Review
7.  Testing
8.  Git
9.  Pull Request
10. Merge

------------------------------------------------------------------------

# Coding Guidelines

-   Prefer readability over clever code.
-   One function --- one responsibility.
-   Avoid duplicated logic.
-   Validate user input.
-   Use type hints where practical.

------------------------------------------------------------------------

# Planned Improvements

## CLI

-   Search by text
-   Sort notes
-   Filter notes
-   Better validation
-   Better error handling

## Architecture

-   Introduce classes
-   Improve module separation
-   Unit tests

## Persistence

-   SQLite support
-   Repository pattern

------------------------------------------------------------------------

# Related Documentation

-   `docs/README.md`
-   `docs/project-manifest.md`
-   `docs/specifications/roadmap.md`
-   `docs/architecture/architecture-decisions.md`
-   `docs/architecture/development-workflow.md`
-   `docs/standards/activity-diagram-standard.md`
-   `docs/standards/git-style-guide.md`

------------------------------------------------------------------------

> This document describes the current technical state of the project and
> should be updated whenever the architecture or implementation changes.
