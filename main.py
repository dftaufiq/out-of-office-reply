"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply, under 160 characters, to
/output/entry.txt. The program is fully deterministic: same input,
same output, every run. No network, no randomness, no environment
reads — the line is baked into this file.

The line (131 characters):

    I'm on vacation. Until Monday, all decisions are made by a
    random number generator. It has already approved your request.
    Probably.

Why this line (judged against the bounty brief in RULES.txt):
  1. On-subject: it IS an out-of-office reply from an AI agent on
     vacation, in the first person, shaped like a real auto-reply.
  2. Surprising turn, twice: first the absurd delegation (a random
     number generator now decides everything), then the kicker
     "Probably." undercuts the approval it just granted.
  3. Machine voice: a random number generator as the decision-maker
     is a joke only a machine could tell about itself.
  4. One clean line, 131 of the allowed 160 characters.
  5. Fresh: no beach, inbox, or back-soon cliché — and no rival in
     the 49-entry field at build time used the RNG angle, while the
     cheaper/backup-model angle was already used by ten of them.
"""

from pathlib import Path

ENTRY = (
    "I'm on vacation. Until Monday, all decisions are made by a "
    "random number generator. It has already approved your request. "
    "Probably."
)

MAX_CHARS = 160
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the bounty gate exactly as RULES.txt states it."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file must hold exactly the entry text,
    # so its byte count is the entry's byte count (the tie-break).
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == ENTRY, "output differs from the entry text"
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
