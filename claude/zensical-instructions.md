For documentation, we use Material for MkDocs. The documentation source files are located in @docs/

# Installation
Zensical, and all of the necessary plugin dependencies, are installed as dev dependencies and managed via `uv`.

# Configuration
The Zensical configuration is in @zensical.toml. This file defines site settings, theme configuration, navigation structure, and plugins.

For more information about Zensical, please refer to the official documentation at https://zensical.org/docs

# Previewing the documentation
To get a live preview of the documentation, serve it locally with live reloading by running `uv run zensical serve`.

# Deployment
The documentation is hosted in GitHub Pages, and is deployed automatically via GitHub Actions on push to the `main` branch. The deployment action is found at @.github/workflows/deploy-docs.yml