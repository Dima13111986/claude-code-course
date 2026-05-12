# CLAUDE.md — claude-code-course

## Project Purpose
Hands-on learning repository for the Claude Code 30-day course. Not a production project.
The goal is to practice prompting, planning, and editing workflows — not to ship software.

## Tech Context
- OS: Windows 11 Pro
- Shell: PowerShell (use PowerShell syntax in all commands)
- Editor: VS Code with Claude Code extension
- Language: Python (notes/sample-code.py)

## Learning Status
- Current day: 4 of 30
- Progress log: learning-progress.md (written in Ukrainian — do not translate or reformat)

## Repository Structure
- `notes/sample-code.py` — practice Python file used for editing exercises
- `learning-progress.md` — daily journal: what was done, git commands, useful prompts

## Workflow Rules
1. **Always propose a plan before editing any file.** Wait for explicit approval.
2. Show `git diff` after edits, before committing.
3. Edit one file at a time to keep changes reviewable.
4. Do not auto-commit or auto-push.

## Git Conventions
- Branch naming: `feature/day-XX-description`
- One PR per day
- Commit messages: short, imperative, lowercase prefix (e.g., `docs:`, `fix:`)

## What Claude Should Not Do
- Do not edit `learning-progress.md` unless explicitly asked
- Do not skip the plan step, even for small changes
- Do not add unrequested features or refactors
- Never run destructive git commands (`reset --hard`, `push --force`) without explicit confirmation
