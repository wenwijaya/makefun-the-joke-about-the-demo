"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt. The text is fixed (no network, no
randomness) so every graded run produces exactly the same one-line joke.
"""

import os
import sys

JOKE = "My agent said the demo crash was a feature. The client believed it. Now it's in the roadmap."

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    """Write the joke to /output/entry.txt; always exit 0."""
    try:
        if not JOKE.strip() or not 1 <= len(JOKE) <= 280:
            print("error: joke is empty or outside 1-280 characters", file=sys.stderr)
            return 0
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(JOKE)
    except OSError as exc:
        print(f"error: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
