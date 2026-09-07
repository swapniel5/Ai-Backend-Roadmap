"""A simple command-line todo application backed by a JSON file."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_tasks(path: Path) -> list[dict[str, Any]]:
    """Load tasks from JSON, returning an empty list for a new data file."""
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON in {path}: {error.msg}") from error
    except OSError as error:
        raise OSError(f"could not read {path}: {error}") from error

    if not isinstance(tasks, list) or not all(isinstance(task, dict) for task in tasks):
        raise ValueError(f"expected a JSON list of task objects in {path}")
    return tasks


def save_tasks(path: Path, tasks: list[dict[str, Any]]) -> None:
    """Save tasks as readable JSON, creating parent folders when needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=2)
            file.write("\n")
    except OSError as error:
        raise OSError(f"could not write {path}: {error}") from error


def next_task_id(tasks: list[dict[str, Any]]) -> int:
    """Return one greater than the largest existing task ID."""
    return max((int(task.get("id", 0)) for task in tasks), default=0) + 1


def add_task(path: Path, title: str) -> None:
    """Add a pending task and save the updated task list."""
    tasks = load_tasks(path)
    task = {"id": next_task_id(tasks), "title": title, "completed": False}
    tasks.append(task)
    save_tasks(path, tasks)
    print(f"Added task {task['id']}: {title}")


def list_tasks(path: Path) -> None:
    """Print all tasks, or a message when there are no tasks."""
    tasks = load_tasks(path)
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        marker = "x" if task.get("completed", False) else " "
        print(f"[{marker}] {task['id']}: {task['title']}")


def complete_task(path: Path, task_id: int) -> None:
    """Mark one task as completed."""
    tasks = load_tasks(path)
    for task in tasks:
        if task.get("id") == task_id:
            task["completed"] = True
            save_tasks(path, tasks)
            print(f"Completed task {task_id}: {task['title']}")
            return
    raise ValueError(f"task {task_id} was not found")


def remove_task(path: Path, task_id: int) -> None:
    """Remove one task from the task list."""
    tasks = load_tasks(path)
    remaining = [task for task in tasks if task.get("id") != task_id]
    if len(remaining) == len(tasks):
        raise ValueError(f"task {task_id} was not found")
    save_tasks(path, remaining)
    print(f"Removed task {task_id}")


def create_parser() -> argparse.ArgumentParser:
    """Build the CLI parser and its subcommands."""
    parser = argparse.ArgumentParser(description="Manage a small list of todo tasks.")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path(__file__).with_name("tasks.json"),
        help="JSON data file (default: tasks.json beside this script)",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add_parser = commands.add_parser("add", help="add a new task")
    add_parser.add_argument("title", help="task title")
    commands.add_parser("list", help="list all tasks")

    done_parser = commands.add_parser("done", help="mark a task as completed")
    done_parser.add_argument("id", type=int, help="task ID")

    remove_parser = commands.add_parser("remove", help="remove a task")
    remove_parser.add_argument("id", type=int, help="task ID")
    return parser


def main() -> int:
    """Parse a command, execute it, and return a shell exit code."""
    args = create_parser().parse_args()
    try:
        if args.command == "add":
            add_task(args.data, args.title)
        elif args.command == "list":
            list_tasks(args.data)
        elif args.command == "done":
            complete_task(args.data, args.id)
        elif args.command == "remove":
            remove_task(args.data, args.id)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
