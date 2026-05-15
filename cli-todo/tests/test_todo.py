from todo import add_task, load_tasks, save_tasks


def test_add_task_to_empty_file(tmp_path):
    path = tmp_path / "tasks.json"

    add_task(path, "buy milk")

    tasks = load_tasks(path)
    assert len(tasks) == 1
    assert tasks[0] == {"id": 1, "text": "buy milk", "done": False}


def test_add_task_assigns_incrementing_id(tmp_path):
    path = tmp_path / "tasks.json"

    add_task(path, "first")
    add_task(path, "second")

    tasks = load_tasks(path)
    assert len(tasks) == 2
    assert tasks[1]["id"] == 2


def test_load_tasks_missing_file_returns_empty(tmp_path):
    path = tmp_path / "does_not_exist.json"

    assert load_tasks(path) == []


def test_save_then_load_round_trip(tmp_path):
    path = tmp_path / "tasks.json"
    data = [
        {"id": 1, "text": "a", "done": False},
        {"id": 2, "text": "b", "done": True},
    ]

    save_tasks(path, data)

    assert load_tasks(path) == data
