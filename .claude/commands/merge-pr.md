---
argument-hint: [pr-number]
description: Merge a PR and clean up branches
---

Please help me merge a pull request and clean up branches.

Follow these steps:

1. Identify the PR:

    1. If a PR number was provided as an argument (`$ARGUMENTS`), use it. Otherwise, get the PR number for the active branch: `gh pr list --head $(git branch --show-current) --json number`
    2. Check the PR status: `gh pr view <pr-number> --json state,mergeable,mergeStateStatus`
    3. If the PR is not mergeable, explain why and stop.

2. Merge the PR:

    1. Squash merge and delete the remote branch: `gh pr merge <pr-number> --squash --delete-branch`
    2. If merge fails, explain the error and suggest resolution.

3. Clean up local environment:

    1. Switch to main branch: `git checkout main`
    2. Fetch and prune remote-tracking branches: `git fetch --prune`
    3. Delete local branches that have been merged: `git branch --merged main | grep -v '^\*\|main\|master' | xargs -r git branch -d`
    4. Report which local branches were cleaned up.

4. Confirm completion:

    1. Show the current branch and status: `git status`
    2. Summarise what was done.
