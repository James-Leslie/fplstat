# Project Summary
Python package for loading and transforming Fantasy Premier League (FPL) API data. The purpose of this package is to provide a clean and efficient way to access and manipulate FPL data for analysis and visualization. Example use cases would be ad-hoc analysis in Jupyter notebooks, or building web applications with frameworks like Streamlit or Dash.

See @README.md for more details.

# Tooling & Methodology

## FPL API
The package interacts with the official Fantasy Premier League API.

Additional details about the API can be found in @docs/data-reference.md

## Python package management
Use `uv` for everything related to project and dependency management (i.e. no `pip`, `python` or `conda` commands). This includes adding/removing packages, syncing dependencies, running tests, and building documentation.

Additional instructions can be found in @claude/uv-instructions.md.

## CLI Tools
The project relies on several command-line tools. Keep these tools up-to-date to avoid compatibility issues and bugs.

| Tool | Current Version | Last Updated | Purpose |
|------|----------------|--------------|---------|
| `uv` | 0.8.4 | 2025-07-30 | Python package & dependency management |
| `gh` | 2.83.1 | 2025-11-13 | GitHub CLI for PRs, issues, and releases |
| `git` | 2.39.5+ | - | Version control |

**Maintenance Tips:**
- Check for updates regularly, especially if encountering errors with CLI commands

## Testing
Pytest is used for testing. Aim for high test coverage, especially for core functionality. Tests should be located in the `tests/` directory and follow a clear naming convention.

Use `uv run pytest` to run tests.

## Documentation
Documentation is built using Zensical and hosted on GitHub Pages.

Additional instructions can be found in @claude/zensical-instructions.md.

## Code Standards
- Type hints and Google-style docstrings required
- Use f-strings, follow PEP 8
- Self-documenting code with clear naming
- Use double quotes for strings

# Workflow Guidelines
1. Do not make direct changes to the main branch. Use git branches for new features and bug fixes, via terminal commands, you may use either the GitHub CLI (e.g. `gh pr create`) or standard git commands (`git checkout -b <branch-name>`), as needed
2. Plan changes before coding, especially for larger features or refactors
3. Write tests for new features and bug fixes, ensure high coverage
4. Frequent commits with descriptive messages
5. Update documentation for new features and changes
6. When ready, create a pull request for review

# CLAUDE.md Maintenance
**IMPORTANT**: This CLAUDE.md file should be kept up-to-date as the project evolves. When making significant changes to tooling, workflows, or project structure, update the relevant sections in this file. This ensures future AI assistance remains consistent with project conventions.