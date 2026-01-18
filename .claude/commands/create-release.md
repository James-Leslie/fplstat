---
argument-hint: [patch|minor|major]
description: Create a new release
---

Please help me create a new release for this package.

Follow these steps exactly:

## Step 1: Verify Prerequisites
1. Ensure we are on the `main` branch with a clean working directory
2. Pull the latest changes: `git pull origin main`
3. Run tests to ensure everything passes: `uv run pytest`

## Step 2: Determine Version Bump
If a version bump type was provided as an argument (`$1`), use it. Otherwise, ask me what type of release this is:
- `patch` - Bug fixes only (0.2.0 → 0.2.1)
- `minor` - New features, backwards compatible (0.2.0 → 0.3.0)
- `major` - Breaking changes (0.2.0 → 1.0.0)

## Step 3: Review Changes Since Last Release
Check what has changed since the last release to help determine version type and release notes:
```bash
# If tags exist, show commits since last tag
git log $(git describe --tags --abbrev=0 2>/dev/null || echo "")..HEAD --oneline

# If no tags exist, show recent commits
git log --oneline -20
```

## Step 4: Create Release Branch and Bump Version
1. Create a release branch: `git checkout -b release/v<new-version>`
2. Bump the version: `uv version --bump <level>`
3. Commit the version bump: `git add pyproject.toml uv.lock && git commit -m "Bump version to <new-version>"`
4. Push the branch: `git push -u origin release/v<new-version>`

## Step 5: Create and Merge PR
1. Create a PR for the version bump:
   ```bash
   gh pr create --title "Release v<new-version>" --body "Bump version for release v<new-version>"
   ```
2. Wait for PR approval and merge (or merge immediately if appropriate)
3. Switch back to main and pull: `git checkout main && git pull`

## Step 6: Create GitHub Release
Create the release using GitHub CLI with auto-generated notes:
```bash
gh release create v<new-version> --generate-notes --title "v<new-version>"
```

The `--generate-notes` flag automatically generates release notes from merged PRs since the last release. If you want to add custom notes, use:
```bash
gh release create v<new-version> --generate-notes --title "v<new-version>" --notes "Additional notes here"
```

## Step 7: Verify Release
1. Check that the GitHub Actions workflow started: `gh run list --workflow=deploy-package.yml`
2. Monitor the workflow: `gh run watch`
3. Verify the package is published on PyPI

## Important Notes
- The release tag (e.g., `v0.3.0`) MUST match the version in `pyproject.toml` (e.g., `0.3.0`)
- The deploy workflow verifies this match and will fail if they don't align
- Always create releases from the `main` branch after the version bump PR is merged
