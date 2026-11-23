#!/usr/bin/env python3
"""A Day of One-Line Pitches entry.

One sentence (168 characters) that would convince a friend who has never
coded to let an AI agent build their first app idea on make.fun. Written
to /output/entry.txt. Deterministic: the same sentence every run, no
network, no randomness.
"""

from pathlib import Path

PITCH = "Tell make.fun your app idea in plain words and its AI agent builds it for you \u2014 no code, no cost to try, and you'll have something real to show your friends by tonight."

MAX_CHARS = 240


def validate(sentence: str) -> str:
    """The gate needs 1-240 characters of real text, not only whitespace."""
    if not 1 <= len(sentence) <= MAX_CHARS:
        raise ValueError(f"sentence is {len(sentence)} characters, must be 1-{MAX_CHARS}")
    if not sentence.strip():
        raise ValueError("sentence must not be only whitespace")
    if sentence != sentence.strip():
        raise ValueError("sentence must not start or end with whitespace")
    return sentence


def main() -> None:
    text = validate(PITCH)
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
