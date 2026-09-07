# Todo CLI

`todo_cli.py` is a small command-line application for managing tasks. It uses
only Python's standard library and stores tasks in a JSON file.

## Run it

From the repository root:

```bash
python3 01-python-data/todo_cli/todo_cli.py --data /tmp/my-tasks.json add "Learn Python"
python3 01-python-data/todo_cli/todo_cli.py --data /tmp/my-tasks.json list
python3 01-python-data/todo_cli/todo_cli.py --data /tmp/my-tasks.json done 1
python3 01-python-data/todo_cli/todo_cli.py --data /tmp/my-tasks.json remove 1
```

The `--data` option is optional. Without it, tasks are saved in
`01-python-data/todo_cli/tasks.json`.

View all commands:

```bash
python3 01-python-data/todo_cli/todo_cli.py --help
```

## Concepts demonstrated

- `argparse` subcommands for a CLI interface
- Functions and type hints
- Lists and dictionaries
- Reading and writing JSON
- Error handling for invalid IDs and corrupted data
