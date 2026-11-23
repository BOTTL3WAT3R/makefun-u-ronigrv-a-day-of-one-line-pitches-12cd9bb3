#!/usr/bin/env python3
"""Print the one-line pitch for make.fun's "A Day of One-Line Pitches" bounty."""
from pathlib import Path

PITCH_FILE = Path(__file__).resolve().parent / "pitch.txt"
MAX_CHARS = 240  # the bounty allows one sentence of at most 240 characters


def load_pitch() -> str:
    """Return the pitch, refusing anything that breaks the bounty's rules."""
    pitch = PITCH_FILE.read_text(encoding="utf-8").strip()
    if len(pitch) > MAX_CHARS:
        raise SystemExit(f"pitch is {len(pitch)} characters; the limit is {MAX_CHARS}")
    if not pitch.endswith(".") or pitch.count(".") != pitch.count("make.fun") + 1:
        raise SystemExit("pitch must be a single sentence")
    return pitch


def main() -> None:
    print(load_pitch())


if __name__ == "__main__":
    main()
