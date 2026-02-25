# encoder.py
from dataclasses import dataclass
from typing import List, Optional
from braille_map import SPACE, CTRL, LETTERS, DIGIT_MAP, CHAR_MAP
import unicodedata


@dataclass(frozen=True)
class Cell:
    # One braille cell (one 6-dot character position)
    name: str                 # e.g. "a", "CAP", "NUM", "space", ".", "3"
    dots: str                 # e.g. "100000"
    unicode: Optional[str] = None  # for debugging/printing (optional)

SPECIAL_FOLDS = {
    "ß": "ss",
    "æ": "ae",
    "œ": "oe",
    "ø": "o",
    "å": "a",
    "đ": "d",
    "ð": "d",
    "þ": "th",
    "ł": "l",
    "ñ": "n",
    "ç": "c",
}

def strip_diacritics(s: str) -> str:
    # First do special folds (handles letters that won't become plain a/e/o nicely)
    s = "".join(SPECIAL_FOLDS.get(ch, ch) for ch in s)

    # Then remove accents (á -> a, ì -> i, ü -> u, etc.)
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return unicodedata.normalize("NFC", s)





def _cell_from_map(entry: dict, name_override: Optional[str] = None) -> Cell:
    name = name_override if name_override is not None else entry.get("name", "?")
    return Cell(name=name, dots=entry["dots"], unicode=entry.get("unicode"))

def sanitize_text(text: str) -> str:
    """
    Used for replacing specific characters with more popular characters. e.g. Em-dash
    """
    text = strip_diacritics(text)
    return (text
            #Tabs -> Spaces
            .replace("\t", "    ")

            # Dashes
            .replace("—", "-")
            .replace("–", "-")
            .replace("−", "-")
            
            # Ellipsis
            .replace("…", "...")

            # Smart quotes
            .replace("“", '"').replace("”", '"').replace("„", '"').replace("«", '"').replace("»", '"')
            .replace("‘", "'").replace("’", "'").replace("‚", "'")

            # Non-breaking spaces
            .replace("\u00A0", " ")
            .replace("\u202F", " ")

            #braces -> paentheses
            .replace("{", "(").replace("}", ")")

            # backtick (markdown/code) -> apostrophe
            .replace("`", "'")

            #Special Character
            .replace("^", "")
            .replace("~", "")
            .replace("_", " ")
            .replace("|", "/")
           )


def encode_cells(text: str) -> List[Cell]:
    """
    Uncontracted UEB (grade 1) encoder:
    - Inserts CAP (⠠) before each uppercase letter.
    - Inserts NUM (⠼) when entering number mode.
    - In number mode, digits 1-0 are represented by letters a-j (UEB rule).
    - Number mode ends on most non-digit characters.
      Special case: '.' and ',' keep number mode ONLY if followed by a digit (12.5, 1,234).
    """
    cells: List[Cell] = []
    number_mode = False
    text = sanitize_text(text)
    n = len(text)
    for i, ch in enumerate(text):
        nxt = text[i + 1] if i + 1 < n else ""

        if ch == "\n":
            cells.append(Cell(name="\n", dots="000000"))
            continue

        # --- Space (blank cell) ---
        if ch == " ":
            number_mode = False
            cells.append(_cell_from_map(SPACE, "space"))
            continue

        # --- Digits (start/continue number mode) ---
        if ch.isdigit():
            if not number_mode:
                cells.append(_cell_from_map(CTRL["NUM"], "NUM"))
                number_mode = True

            letter_equiv = DIGIT_MAP[ch]               # "1"->"a", ... "0"->"j"
            entry = LETTERS[letter_equiv]
            cells.append(_cell_from_map(entry, ch))    # name is the digit (e.g. "3")
            continue

        # --- Keep number mode through '.' or ',' ONLY if next is digit ---
        if number_mode and ch in {".", ","} and nxt.isdigit():
            # Use punctuation mapping for '.'/',' (UEB)
            entry = CHAR_MAP.get(ch)
            if entry is None:
                raise KeyError(f"Unsupported punctuation in number: {ch!r}")
            cells.append(_cell_from_map(entry, ch))
            continue

        # Any other non-digit ends number mode
        number_mode = False

        # --- Letters ---
        if ch.isalpha():
            if ch.isupper():
                # In uncontracted UEB: single CAP before each capital letter
                cells.append(_cell_from_map(CTRL["CAP"], "CAP"))
                ch = ch.lower()

            entry = LETTERS.get(ch)
            if entry is None:
                raise KeyError(f"Unsupported letter: {ch!r}")
            cells.append(_cell_from_map(entry, ch))
            continue

        # --- Punctuation / symbols (mapped 1:1) ---
        entry = CHAR_MAP.get(ch)
        if entry is None:
            raise KeyError(f"Unsupported character: {ch!r}")
        cells.append(_cell_from_map(entry, ch))

    return cells


def measure(text: str) -> int:
    # Single source of truth: measure == number of generated cells
    return len(encode_cells(text))


def to_dotpatterns(text: str) -> List[str]:
    return [c.dots for c in encode_cells(text)]


def to_unicode(text: str) -> str:
    # Debug view in console
    out = []
    for c in encode_cells(text):
        out.append(c.unicode if c.unicode is not None else "?")
    return "".join(out)


if __name__ == "__main__":
    demo = "Ab 12.5!"
    print("TEXT:", demo)
    print("CELLS:", measure(demo))
    print("DOTS:", to_dotpatterns(demo))
    print("UNIC:", to_unicode(demo))
