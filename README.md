# test-repository

Test repository for [agent-review](https://github.com/ilyasabdut/agent-review) — an AI-powered code review bot.

## Purpose

This repo contains intentionally flawed code to test agent-review's capabilities:

- **src/auth.py** — SQL injection, weak hashing (MD5), hardcoded secrets
- **src/database.py** — N+1 queries, SQL injection, missing error handling
- **src/api.py** — Command injection, path traversal, eval() on user input
- **src/utils.py** — O(2^n) fibonacci, O(n^2) duplicate finder, unbounded cache

## Testing Agent Review

### PR Review
Open a PR that modifies any `src/` file — agent-review will post inline comments.

### Coder Agent
Create an issue and label it `auto-fix` — agent-review will open a PR with a fix.

### Chat
Comment on any PR with `@agent-review explain` or ask a free-form question.
