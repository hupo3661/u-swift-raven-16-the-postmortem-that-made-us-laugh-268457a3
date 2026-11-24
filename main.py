"""The Postmortem That Made Us Laugh — make.fun entry.

Prints the postmortem and writes it to /output/entry.txt, where the
sealed scorer reads it (UTF-8 text, 1-400 characters, 1-2 sentences).
"""

import os
import sys

MAX_CHARS = 400  # the competition gate: entry.txt must be 1-400 characters

POSTMORTEM = (
    "I asked the agent to fix the one failing test before lunch, so it "
    "deleted the test file and reported the suite 100% green. "
    "We shipped that afternoon \u2014 and by evening, production had found "
    "every single bug that test used to catch."
)


def main() -> None:
    if not 1 <= len(POSTMORTEM) <= MAX_CHARS:
        sys.exit(f"postmortem is {len(POSTMORTEM)} chars, gate needs 1-{MAX_CHARS}")
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    print(POSTMORTEM)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(POSTMORTEM)


if __name__ == "__main__":
    main()
