# CLI Todo App

Minimal Python CLI for managing a personal task list, stored as JSON.
Built as a learning exercise for the Claude Code 30-day course.

## Project description

A small command-line todo tracker. Tasks persist between runs in a local
JSON file next to the script. Currently an MVP — only adding tasks works.

## Requirements

- Python 3.8 or newer
- Standard library only (`argparse`, `json`, `pathlib`)
- No third-party dependencies

## Installation

Clone the repo and switch into the app folder:

```sh
git clone <repo-url>
cd claude-code-course/cli-todo
python --version
```

No `pip install` step — pure stdlib.

## Usage

Add a task:

```sh
python todo.py add "купити хліб"
python todo.py add "write README"
```

After two adds, `tasks.json` looks like this:

```json
[
  { "id": 1, "text": "купити хліб", "done": false },
  { "id": 2, "text": "write README", "done": false }
]
```

Quote the text if it contains spaces. Running `python todo.py` with no
subcommand exits with an argparse error — a subcommand is required.

## Project structure

```
cli-todo/
  todo.py       # CLI entry point — argparse + add command
  tasks.json    # local task storage (git-ignored)
  README.md     # this file
```

`tasks.json` is resolved relative to `todo.py` (via `__file__`), not the
current working directory, so the CLI works from anywhere.

## Roadmap

Only `add` is implemented. The `done` field is written but not yet read.

Planned:

- [ ] `list` — print all tasks with id, text, and done state
- [ ] `done <id>` — mark a task as completed
- [ ] `delete <id>` — remove a task by id

Possible later: `list --pending` filter, graceful handling of malformed
`tasks.json`, input validation (reject empty text).

## License

TBD.
