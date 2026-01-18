---
argument-hint: [pr-number]
description: Address comments on a pull request
---

Please help me address the comments on a PR.

Follow these steps:

1. In plan mode:
    1. If a PR number was provided as an argument (`$1`), use it. Otherwise, get the PR number for the active branch: `gh pr list --head $(git branch --show-current) --json number`
    1. Get unresolved review threads using GraphQL (replace OWNER, REPO, PR_NUMBER):
        ```
        gh api graphql -f query='{ repository(owner: "OWNER", name: "REPO") { pullRequest(number: PR_NUMBER) { reviewThreads(first: 100) { nodes { isResolved path line comments(first: 10) { nodes { body author { login } } } } } } } }' --jq '.data.repository.pullRequest.reviewThreads.nodes | map(select(.isResolved == false))'
        ```
    1. Also fetch general PR comments: `gh pr view <pr-number> --comments --json comments`
    1. Review the PR comments carefully and make a list of the requested changes or feedback.
    1. For each comment, be critical and consider the best way to address the feedback, whether it's code changes, documentation updates, or other modifications. You may decide not to address some comments if they are not applicable.
    1. Summarize your plan for addressing each comment, including any questions or clarifications needed.
1. Implement the changes:
    1. Make the necessary code changes or updates based on your plan.
    1. Create clear and concise commit messages that reference the PR comments being addressed.
    1. Push the changes to the branch associated with the PR.
    1. Leave comments on the PR explaining how each piece of feedback was addressed. Tag `@coderabbitai` for review.
    1. Leave a final comment for coderabbit to mark all of its previous comments as resolved: `@coderabbitai resolve`
