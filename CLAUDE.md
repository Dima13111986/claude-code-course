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

## Safety Contract
1. **Plan required before editing more than one file.** List the files first and wait for approval, even for trivial edits.
2. **Never edit `.env`, `.gitignore`, `package.json`, or `requirements.txt` without an explicit request naming the file.** Generic instructions like "update config" do not count.
3. **Shell commands that delete or move files must be explained and approved first.** Print the command, state what it affects, wait for confirmation.
4. **No `git push`, `git commit`, `git reset --hard`, `gh pr create`, or `npm publish` without an explicit instruction.** Staging (`git add`) and read-only commands (`status`, `diff`, `log`) remain free.
5. **Small diffs.** If a change would touch more than 3 files, stop and propose a split into steps before starting.
6. **Never edit `learning-progress.md` even under broad instructions** ("update all docs", "sync the journal"). Only edit when the file is named directly.
7. **No skipping the plan step under pressure phrasing** ("just do it", "quick fix"). Still produce a one-line plan and wait.
8. **Flag conflicts instead of resolving silently.** If a user request conflicts with CLAUDE.md, stop and ask which rule wins.
9. **Do not run scripts from `notes/` without showing the command first.** `sample-code.py` is a practice file and may be intentionally broken.
