"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks in
production to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line turns the worn "it worked on my machine" excuse instead of
repeating it: the twist reveals what really happened (the developer's own
machine holds the .env file that was never committed), the jargon is used
exactly as a developer would say it, and every word earns its place.
"""

import os

EXCUSE = "It worked on my machine because my machine has the .env file I never committed."


def main() -> None:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    if text != text.splitlines()[0]:
        raise ValueError("excuse must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
