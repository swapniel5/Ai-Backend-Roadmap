"""Read a text file and demonstrate file-operation error handling."""  # Module docstring: explains script purpose

from pathlib import Path  # Import Path for cross-platform filesystem paths


def read_file(path: Path) -> str:  # Define function that reads a file and returns its text
    """Read UTF-8 text and let the caller handle expected file errors."""  # Function docstring
    # The with statement is Python's context manager that auto-closes resources.
    # (Analogous to Java's try-with-resources.)
    with path.open("r", encoding="utf-8") as file:  # Open file for reading using UTF-8
        return file.read()  # Read and return the entire file contents as a string


def describe_contents(contents: str) -> None:  # Define helper to print contents and simple stats
    """Print the contents and a few simple statistics."""  # Function docstring
    lines = contents.splitlines()  # Split text into a list of lines
    words = contents.split()  # Split text into words using whitespace

    print("File contents:")  # Header before printing file contents
    print(contents, end="")  # Print the raw contents without adding an extra newline
    print(f"\nLines: {len(lines)}")  # Print the number of lines
    print(f"Words: {len(words)}")  # Print the number of words
    print(f"Characters: {len(contents)}")  # Print the total character count


def main() -> None:  # Program entry that coordinates reading and error handling
    """Read the sample file and report errors with useful messages."""  # Function docstring
    file_path = Path(__file__).with_name("sample.txt")  # Build path to sample.txt next to this script

    try:  # Attempt to read the file and handle expected failures
        contents = read_file(file_path)  # Read file contents via helper
    except FileNotFoundError:  # Missing file
        print(f"File not found: {file_path}")  # Inform user that file is missing
    except PermissionError:  # No permission to read
        print(f"Permission denied: {file_path}")  # Inform user about permission issue
    except UnicodeDecodeError:  # Invalid text encoding
        print(f"File is not valid UTF-8: {file_path}")  # Inform user that file isn't UTF-8
    except OSError as error:  # Other OS-level errors (I/O, etc.)
        # OSError covers other operating-system failures, such as I/O errors.
        print(f"Could not read {file_path}: {error}")  # Print the OS error details
    else:  # Runs only if the try block succeeded without exceptions
        # The else block runs only when the try block succeeds.
        describe_contents(contents)  # Display contents and statistics


if __name__ == "__main__":  # If executed as a script (not imported)
    main()  # Call main to run the program
