# Claude Code — Мій прогрес курсу

## Поточний день
День: 3
Статус: completed

## Журнал днів

### День 2 — Read-only workflow, @-mentions, plan-only mode
- Дата: 2026-05-09
- Статус: completed
- Що зроблено:
  - Practiced read-only analysis: listed repo structure without editing any files
  - Used @-mentions (@notes/sample-code.py, @learning-progress.md) to reference files in prompts
  - Ran a multi-step plan-only workflow: bug review → implementation plan → awaiting approval before writing
  - Learned to ask Claude for a diff preview before committing to a file change
- Git команди:
  - `git status` — checked working tree state
  - `git log --oneline` — reviewed recent commits
- Корисні промпти:
  - "Analyze the structure of this repository. Do NOT edit any files."
  - "List potential bugs. Do NOT fix anything yet."
  - "Create an implementation plan. Wait for my explicit approval."
  - "Show me the diff before saving."
- Проблеми: —
- Що повторити наступного разу: practice approving and rejecting plans, then applying fixes

### День 1 — Перший запуск Claude Code у VS Code terminal
- Статус: completed
- Що зроблено:
  - Claude Code installed and verified
  - Project folder created at C:\Projects\claude-code-course
  - .gitignore configured (node_modules, .env, .DS_Store)
  - README.md created
  - learning-progress.md created
  - Git repository initialized
  - First commit 802cb48 made
  - Repository pushed to GitHub
- Git commits:
  - 802cb48 - Day 1: initial setup with Claude Code
- Корисні промпти:
- Проблеми:
- Що повторити наступного разу:

### День 3 — First edit, plan-first workflow, git diff review
- Дата: 2026-05-11
- Статус: completed
- Що зроблено:
  - Merged Day 2 PR and returned to main branch
  - Created feature/day-03-first-edit branch
  - Added docstring to notes/sample-code.py using Claude Code with plan-first workflow
- Git команди:
  - `git checkout main` — switched to main branch
  - `git pull` — synced with remote after PR merge
  - `git branch -d` — deleted merged feature branch locally
  - `git checkout -b` — created new feature branch
  - `git diff` — reviewed changes before committing
  - `git add` — staged changes
  - `git commit` — committed changes
  - `git push` — pushed branch to remote
- Корисні промпти:
  - Plan-first edit: ask Claude to show the plan before making any changes
  - Single-file edit: scope the task to one file to keep changes reviewable
  - Self-review with git diff: ask Claude to show `git diff` after editing
- Проблеми: —
- Що повторити наступного разу: always check git diff before commit

## Загальна інформація
- Навчальний репозиторій: claude-code-course
- GitHub URL: https://github.com/Dima13111986/claude-code-course

## Безпека
- [x] .gitignore налаштований
- [x] .env НЕ в репозиторії
