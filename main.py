#!/usr/bin/env python3
"""Print the Dad Joke Showdown entry: one original dad joke."""

from pathlib import Path


def load_joke():
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("entry.txt is empty")
    if len(text) > 200:
        raise SystemExit(f"joke is {len(text)} chars, over the 200-char limit")
    return text


def main():
    print(load_joke())


if __name__ == "__main__":
    main()
