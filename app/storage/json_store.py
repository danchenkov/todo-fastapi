import json
from pathlib import Path
from app.models.todo import Todo

DATA_FILE = Path("data/todos.json")


def load_todos() -> list[Todo]:
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    return [Todo(**item) for item in data]


def save_todos(todos: list[Todo]) -> None:
    with open(DATA_FILE, "w") as file:
        json.dump([todo.dict() for todo in todos], file, indent=2)