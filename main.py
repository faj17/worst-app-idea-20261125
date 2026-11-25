"""One sentence pitching the worst app idea imaginable, for make.fun.

DustWatch: a $10-a-month app that live-streams the dust settling on
your bookshelves in 4K, alerts you the instant a single new particle
lands, and sends a weekly dust report so serious collectors never miss
a speck. A founder who means every word, solving a problem nobody has.

The script validates the line (1-240 chars, single line, terminal
punctuation) and writes it to /output/entry.txt.
"""

from pathlib import Path

# The pitch itself: one sentence, exactly 218 characters.
# Built from two fragments so the setup and the punchline are each
# visible on their own: the product + what it does, then who it is for.
SETUP = (
    "DustWatch is a $10-a-month app that live-streams the dust settling "
    "on your bookshelves in 4K, alerts you the instant a single new "
    "particle lands, and sends a weekly dust report "
)
PUNCH = "so serious collectors never miss a speck."


def assemble() -> str:
    """Join the fragments into the single-sentence pitch."""
    return SETUP + PUNCH


PITCH = assemble()

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 240


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"pitch must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("pitch must not contain control characters")
    if text[-1] not in ".!?":
        raise ValueError("pitch must end with terminal punctuation")
    if text.count(".") != 1:
        raise ValueError("pitch must be exactly one sentence")
    return text


def main() -> None:
    text = validate(PITCH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    written = OUTPUT_FILE.read_text(encoding="utf-8")
    assert written == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
