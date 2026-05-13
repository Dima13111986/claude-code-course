import argparse
import json
import pathlib

TASKS_FILE = pathlib.Path(__file__).parent / "tasks.json"


def load_tasks(path):
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def save_tasks(path, tasks):
    path.write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def add_task(path, text):
    tasks = load_tasks(path)
    next_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": next_id, "text": text, "done": False})
    save_tasks(path, tasks)


def main():
    parser = argparse.ArgumentParser(prog="todo")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("text")

    args = parser.parse_args()

    if args.command == "add":
        add_task(TASKS_FILE, args.text)


if __name__ == "__main__":
    main()
