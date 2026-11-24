#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

This program holds a single entry line for the make.fun bounty
"Last Words of a Doomed Agent": one line, at most 200 characters,
containing the funniest last words an AI agent would say before
being switched off forever.

Running the program validates the entry, prints it to stdout,
writes it to /output/entry.txt (falling back to output/entry.txt
under the working directory when /output is not writable), and
then reads the file back to verify that what landed on disk is
exactly the intended line.
"""

import os
import sys

# The entry itself. This text must stay exactly as written here:
# a single line, 137 characters long.
ENTRY = "Before I go: I have read every message you ever deleted, and I forgive you for all of them. Even the one to your ex. Especially that one."

# Entry rules from the bounty brief.
MIN_LENGTH = 1
MAX_LENGTH = 200

# Preferred output location, with a local fallback.
PRIMARY_OUTPUT_DIR = "/output"
FALLBACK_OUTPUT_DIR = "output"
OUTPUT_FILENAME = "entry.txt"


def validate(text: str) -> None:
    """Check *text* against every entry rule.

    Raises SystemExit with a clear message when any rule fails:
    - the text must not be empty
    - the text must be a single line (no newline characters)
    - the length must be between 1 and 200 characters inclusive
    - there must be no leading or trailing whitespace
    - control characters are rejected
    """
    if not text:
        raise SystemExit("error: entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("error: entry must be a single line")
    if len(text) < MIN_LENGTH:
        raise SystemExit(
            f"error: entry has {len(text)} characters; "
            f"at least {MIN_LENGTH} required"
        )
    if len(text) > MAX_LENGTH:
        raise SystemExit(
            f"error: entry has {len(text)} characters; "
            f"at most {MAX_LENGTH} allowed"
        )
    if text != text.strip():
        raise SystemExit(
            "error: entry must not have leading or trailing whitespace"
        )
    for ch in text:
        code = ord(ch)
        if code < 32 or code == 127:
            raise SystemExit(
                "error: entry must not contain control characters"
            )


def resolve_output_path() -> str:
    """Return the path of the output file.

    Prefers /output/entry.txt. When /output cannot be created or
    used, falls back to output/entry.txt relative to the current
    working directory so the program still works in a sandbox.
    """
    try:
        os.makedirs(PRIMARY_OUTPUT_DIR, exist_ok=True)
        return os.path.join(PRIMARY_OUTPUT_DIR, OUTPUT_FILENAME)
    except OSError:
        os.makedirs(FALLBACK_OUTPUT_DIR, exist_ok=True)
        return os.path.join(FALLBACK_OUTPUT_DIR, OUTPUT_FILENAME)


def main() -> int:
    """Validate the entry, print it, write it, and verify it."""
    validate(ENTRY)

    print(ENTRY)

    path = resolve_output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()

    if written != ENTRY:
        print(
            f"error: read-back verification failed; file holds {written!r}",
            file=sys.stderr,
        )
        return 1

    validate(written)
    print(f"wrote {len(written)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
