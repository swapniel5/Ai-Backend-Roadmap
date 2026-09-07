# File Reading and Error Handling

This exercise includes a small CLI application that reads a text file, prints
its contents, and reports simple statistics. It demonstrates:

- `open()` and the `with` context manager
- Reading text with an explicit UTF-8 encoding
- Handling `FileNotFoundError`, `PermissionError`, and `UnicodeDecodeError`
- Catching broader `OSError` failures without hiding unexpected exceptions

## CLI usage

Run it from the repository root:

```bash
/opt/homebrew/bin/python3 01-python-data/file_operations/file_stats_cli.py \
    01-python-data/file_operations/sample.txt
```

The application accepts one positional argument: the path to the file to
read. It returns exit code `0` on success and `1` when the file cannot be
read.

Show built-in help:

```bash
/opt/homebrew/bin/python3 01-python-data/file_operations/file_stats_cli.py --help
```

Try the original, function-focused exercise with:

```bash
/opt/homebrew/bin/python3 01-python-data/file_operations/read_file.py
```

## Notes

### Opening and reading a file

```python
with open(path, "r", encoding="utf-8") as file:
    contents = file.read()
```

- `"r"` opens the file for reading.
- `encoding="utf-8"` makes text decoding explicit.
- `with` closes the file automatically, even if an error occurs.

This is similar to Java's try-with-resources:

```java
try (BufferedReader reader = Files.newBufferedReader(path)) {
    // read the file
}
```

### Common exceptions

- `FileNotFoundError`: the requested path does not exist.
- `PermissionError`: the program is not allowed to access the file.
- `UnicodeDecodeError`: the bytes cannot be decoded as UTF-8.
- `OSError`: a broader operating-system file error.

Catch specific exceptions before broader exceptions. Do not use a bare
`except`, because it can hide programming errors and make debugging harder.

## Exercise

Try changing the path in `read_file.py` to a missing file. Observe the clear
error message, then change it back to `sample.txt`.
