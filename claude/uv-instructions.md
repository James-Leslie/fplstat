Any uses of `pip install` can be replaced with `uv add` and any uses of `pip uninstall` can be replaced with `uv remove`. This ensures that the @pyproject.toml and @uv.lock files remain consistent and up-to-date, therefore, you do not need to manually edit the dependencies in these files.

# Key Commands
```bash
uv add package-name              # Add dependencies
uv remove package-name           # Remove dependencies
uv sync                          # Sync dependencies
uv run pytest                    # Run tests
uv run mkdocs serve              # Preview docs
uv version --bump patch          # For backwards compatible bug fixes
uv version --bump minor          # For backwards compatible new features
uv version --bump major          # For incompatible API changes
```

Since `uv` is a relatively new tool, if you encounter any issues or have questions about its usage, please refer to the official documentation at https://docs.astral.sh/uv