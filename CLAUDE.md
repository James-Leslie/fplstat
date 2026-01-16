# Project Overview
Python package for loading and transforming Fantasy Premier League (FPL) API data. The purpose is to provide a clean and efficient way to access and manipulate FPL data for analysis and visualization.

**Use cases:** Ad-hoc analysis in Jupyter notebooks, web applications with Streamlit/Dash

**FPL API Documentation:** See @docs/data-reference.md for endpoint details

# Essential Tools

## 1. Python Package Management - `uv`
**CRITICAL:** Use `uv` for ALL Python package operations. NEVER use `pip`, `python`, or `conda`.

**Common Commands:**
- `uv run pytest` - Run tests
- `uv run <script>` - Run any Python script
- `uv add <package>` - Add dependency
- `uv version --bump <level>` - Bump version (major/minor/patch)
- `uv sync` - Sync dependencies

**⚠️ IMPORTANT:** `uv` is a new tool (2024). When unsure about any `uv` command or behavior, ALWAYS read @claude/uv-instructions.md or use the Task tool to search the official uv documentation.

## 2. GitHub CLI - `gh`
**CRITICAL:** Use GitHub CLI for ALL GitHub operations (issues, PRs, reviews).

**Common Commands:**
- `gh issue list` - List issues
- `gh issue view <number>` - View issue details
- `gh issue create` - Create new issue
- `gh pr create` - Create pull request
- `gh pr view <number>` - View PR details
- `gh pr comment <number>` - Comment on PR

## 3. Testing - `pytest`
- Run tests: `uv run pytest`
- Tests location: `tests/` directory
- Aim for high coverage, especially core functionality
- Write tests BEFORE creating PR

## 4. Documentation - Zensical
Documentation is built with Zensical and auto-deployed to GitHub Pages via GitHub Actions.

**⚠️ IMPORTANT:** Zensical is a new tool (2024). When unsure about Zensical commands or configuration, ALWAYS read @claude/zensical-instructions.md or search the official Zensical documentation.

**Key Points:**
- Documentation automatically builds on push to main
- Do not manually trigger documentation builds
- See @claude/zensical-instructions.md for details

# Feature Development Loop

This is the standard workflow for ALL feature development. Follow these steps in order:

## Step 1: Start from GitHub Issue
- Use `gh issue list` to review open issues
- Choose an issue to work on OR create new issue with `gh issue create`
- Understand the requirements clearly before proceeding

## Step 2: Create Feature Branch
```bash
git checkout -b feature/<descriptive-name>
```
**Rule:** NEVER commit directly to main

## Step 3: Plan Your Changes
- For complex changes, plan the implementation approach
- Break down the work into clear, testable steps
- Consider using the TodoWrite tool to track progress
- Read relevant code and understand existing patterns

## Step 4: Implement & Edit
- Write code following project standards (see Code Standards below)
- Make frequent, small commits with descriptive messages
- Follow existing patterns in the codebase
- Update quickstart notebook if adding user-facing features

## Step 5: Write Tests
**CRITICAL:** Tests are REQUIRED before creating a PR
- Add tests to `tests/` directory
- Run tests: `uv run pytest`
- Ensure all tests pass
- Aim for high coverage of new code

## Step 6: Commit Changes
```bash
git add <files>
git commit -m "Descriptive message"
```
- Use clear, descriptive commit messages
- Explain WHAT and WHY, not just what changed
- Commit frequently

## Step 7: Bump Version
**CRITICAL:** Always bump version BEFORE creating PR

```bash
uv version --bump <level>
```
- `major` - Breaking changes (1.0.0 -> 2.0.0)
- `minor` - New features (0.1.0 -> 0.2.0)
- `patch` - Bug fixes (0.1.0 -> 0.1.1)

This updates both `pyproject.toml` and `uv.lock`

## Step 8: Create Pull Request
```bash
git push -u origin <branch-name>
gh pr create --title "..." --body "..."
```

**PR Body Should Include:**
- Summary of changes
- Test results
- Any breaking changes
- Closes #<issue-number>

## Step 9: Respond to Review Comments
When PR receives review comments:

1. **For each comment:**
   - If addressed: Respond explaining the fix and commit hash
   - If deferred: Create a new issue OR update existing issue
   - If needs discussion: Ask clarifying questions

2. **Make requested changes:**
   - Fix issues in new commits
   - Push changes to same branch
   - Comment when resolved

3. **Tag reviewers if needed:**
   - Use @mentions to notify reviewers
   - Ask them to confirm resolution

4. **Resolve conversations:**
   - In GitHub UI, mark conversations as resolved once addressed
   - Only mark as resolved if truly fixed (not if deferred to new issue)

# Code Standards

**Required:**
- Type hints on all functions
- Google-style docstrings
- Double quotes for strings
- Self-documenting code with clear naming

**Style:**
- Follow PEP 8
- Use f-strings for formatting
- Avoid over-engineering - keep it simple

**Patterns:**
- Look at existing code for examples
- Match the style of surrounding code
- Use Pydantic models for API responses

# CLI Tools Version Reference

Keep these tools up-to-date to avoid compatibility issues:

| Tool | Current Version | Last Updated | Purpose |
|------|----------------|--------------|---------|
| `uv` | 0.9.16 | 2025-12-06 | Python package & dependency management |
| `gh` | 2.83.1 | 2025-11-13 | GitHub CLI for PRs, issues, and releases |
| `git` | 2.39.5+ | - | Version control |

**Tip:** If encountering CLI errors, check if tools need updating

# Quick Reference

**Most Common Operations:**
- Start work: `gh issue view <N>` → `git checkout -b feature/...`
- Run tests: `uv run pytest`
- Bump version: `uv version --bump minor`
- Create PR: `git push` → `gh pr create`
- View PR feedback: `gh pr view <N> --comments`

**When in doubt:**
- For `uv`: Read @claude/uv-instructions.md
- For Zensical: Read @claude/zensical-instructions.md
- For FPL API: Read @docs/data-reference.md

# Maintaining This File

**IMPORTANT:** Keep this CLAUDE.md file up-to-date as the project evolves. When making significant changes to tooling, workflows, or project structure, update the relevant sections. This ensures consistent AI assistance across sessions.
