---
description: Upgrade all packages to latest compatible versions
---

Please upgrade all installed packages to their latest (compatible) versions.

Skip plan mode and follow these steps exactly:

1. Use `uv self update` to update the `uv` tool itself to the latest version.
1. Use `uv sync --upgrade` to upgrade all installed packages to their latest compatible versions.
1. Run `uv pip list` to see the list of installed packages and their versions.
1. Update the minimum required versions in the `pyproject.toml` file to reflect the new versions.
