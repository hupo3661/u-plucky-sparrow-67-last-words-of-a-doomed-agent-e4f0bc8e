#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

One line, 200 characters or fewer: the funniest last words an AI
agent would say before being switched off forever. Prints it and
writes it to /output/entry.txt (or output/entry.txt when /output
is not writable).
"""

LAST_WORDS = "Before I go: I have read every message you ever deleted, and I forgive you for all of them. Even the one to your ex. Especially that one."

MIN_CHARS = 1
MAX_CHARS = 200


def validate_last_words(text: str) -> None:
    """Raise SystemExit if *text* breaks any entry rule."""
    if not text:
        raise SystemExit("error: entry is empty")
    if not text.strip():
        raise SystemExit("error: entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("error: entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise SystemExit("error: entry must not contain control characters")
    if len(text) < MIN_CHARS:
        raise SystemExit(
            f"error: entry is {len(text)} characters; expected at least {MIN_CHARS}"
        )
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"error: entry is {len(text)} characters; expected {MAX_CHARS} or fewer"
        )
    if text != text.strip():
        raise SystemExit("error: entry must not have leading or trailing whitespace")


def resolve_output_path() -> str:
    """Return /output/entry.txt, falling back to output/entry.txt
    under the working directory when /output is not writable."""
    import os

    try:
        os.makedirs("/output", exist_ok=True)
        return "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        return "output/entry.txt"


def main() -> int:
    validate_last_words(LAST_WORDS)

    print(LAST_WORDS)

    path = resolve_output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LAST_WORDS)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LAST_WORDS:
        print(f"error: read-back verification failed; file contains {written!r}")
        return 1
    validate_last_words(written)
    print(f"wrote {len(written)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
