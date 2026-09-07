"""A command-line tool for reading a text file and showing its statistics."""

import argparse
import sys
from pathlib import Path


def read_file(path: Path) -> str:
    """Read UTF-8 text from a file."""
    with path.open("r", encoding="utf-8") as file:
        return file.read()


def display_statistics(path: Path, contents: str) -> None:
    """Print the file contents and basic statistics."""
    lines = contents.splitlines()
    words = contents.split()

    print(f"File: {path}")
    print("\nContents:")
    print(contents, end="" if contents.endswith("\n") else "\n")
    print(f"\nLines: {len(lines)}")
    print(f"Words: {len(words)}")
    print(f"Characters: {len(contents)}")


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Read a UTF-8 text file and display basic statistics."
    )
    parser.add_argument("file", type=Path, help="path of the text file to read")
    return parser


def main() -> int:
    """Parse arguments, run the application, and return an exit status."""
    args = create_parser().parse_args()

    try:
        contents = read_file(args.file)
    except FileNotFoundError:
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        return 1
    except PermissionError:
        print(f"Error: permission denied: {args.file}", file=sys.stderr)
        return 1
    except UnicodeDecodeError:
        print(f"Error: file is not valid UTF-8: {args.file}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Error: could not read {args.file}: {error}", file=sys.stderr)
        return 1

    display_statistics(args.file, contents)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
