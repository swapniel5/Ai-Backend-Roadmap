# CLI application self-review

## What is working well

- The application has a simple, focused command-line interface.
- `argparse` provides `--help` and validates the required file argument.
- `pathlib.Path` makes file paths portable and readable.
- The `with` statement closes files automatically.
- Expected file errors produce useful messages on stderr and a non-zero exit
  code.
- Reading and display logic are separate, which makes the code easier to test.

## Improvements to consider

- Add automated tests for successful reads, missing files, permissions, and
  invalid encodings.
- Add an option to suppress file contents when only statistics are needed.
- Support a configurable encoding for files that are not UTF-8.
- Stream very large files instead of loading the complete contents into memory.
- Add logging if the application grows beyond a learning exercise.
- Package the command with a `pyproject.toml` entry point so it can be run as a
  shell command instead of using `python3 file_stats_cli.py`.
