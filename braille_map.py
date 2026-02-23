# braille_map.py
# UEB (Unified English Braille) - basic cells for uncontracted text handling.
# dots string format: "dot1..dot6" as bits (1=raised, 0=flat)

# --- SPACE (blank cell) ---
SPACE = {"name": "SPACE", "unicode": "⠀", "dots": "000000"}  # U+2800

# --- CONTROL / INDICATORS (UEB) ---
# Capital indicator: ⠠ (dot 6)  | Numeric indicator: ⠼ (dots 3-4-5-6)
CTRL = {
    "CAP": {"name": "CAP", "unicode": "⠠", "dots": "000001"},
    "NUM": {"name": "NUM", "unicode": "⠼", "dots": "001111"},
}

# --- LETTERS a-z (standard literary braille) ---
LETTERS = {
    "a": {"unicode": "⠁", "dots": "100000"},
    "b": {"unicode": "⠃", "dots": "110000"},
    "c": {"unicode": "⠉", "dots": "100100"},
    "d": {"unicode": "⠙", "dots": "100110"},
    "e": {"unicode": "⠑", "dots": "100010"},
    "f": {"unicode": "⠋", "dots": "110100"},
    "g": {"unicode": "⠛", "dots": "110110"},
    "h": {"unicode": "⠓", "dots": "110010"},
    "i": {"unicode": "⠊", "dots": "010100"},
    "j": {"unicode": "⠚", "dots": "010110"},
    "k": {"unicode": "⠅", "dots": "101000"},
    "l": {"unicode": "⠇", "dots": "111000"},
    "m": {"unicode": "⠍", "dots": "101100"},
    "n": {"unicode": "⠝", "dots": "101110"},
    "o": {"unicode": "⠕", "dots": "101010"},
    "p": {"unicode": "⠏", "dots": "111100"},
    "q": {"unicode": "⠟", "dots": "111110"},
    "r": {"unicode": "⠗", "dots": "111010"},
    "s": {"unicode": "⠎", "dots": "011100"},
    "t": {"unicode": "⠞", "dots": "011110"},
    "u": {"unicode": "⠥", "dots": "101001"},
    "v": {"unicode": "⠧", "dots": "111001"},
    "w": {"unicode": "⠺", "dots": "010111"},
    "x": {"unicode": "⠭", "dots": "101101"},
    "y": {"unicode": "⠽", "dots": "101111"},
    "z": {"unicode": "⠵", "dots": "101011"},
}

# --- DIGITS (UEB): after NUM sign, 1-0 are letters a-j ---
DIGIT_MAP = {
    "1": "a", "2": "b", "3": "c", "4": "d", "5": "e",
    "6": "f", "7": "g", "8": "h", "9": "i", "0": "j",
}

# --- PUNCTUATION (UEB basics) ---
# These are standard single-cell signs commonly used in UEB.
PUNCT = {
    ",": {"unicode": "⠂", "dots": "010000"},
    ";": {"unicode": "⠆", "dots": "011000"},
    ":": {"unicode": "⠒", "dots": "010010"},
    ".": {"unicode": "⠲", "dots": "010011"},
    "!": {"unicode": "⠖", "dots": "011010"},
    "?": {"unicode": "⠦", "dots": "011001"},
    "-": {"unicode": "⠤", "dots": "001001"},
    "/": {"unicode": "⠌", "dots": "001100"},
    "'": {"unicode": "⠄", "dots": "001000"},
    " ": {"unicode": "⠀", "dots": "000000"},
    "“": {"unicode": "⠦", "dots": "011001"},
    "”": {"unicode": "⠴", "dots": "001011"},
    '"': {"unicode": "⠂", "dots": "010000"},
    "#": {"unicode": "⠄", "dots": "001000"},
    "$": {"unicode": "⠅", "dots": "101000"},
    "%": {"unicode": "⠆", "dots": "011000"},
    "&": {"unicode": "⠇", "dots": "111000"},
    "(": {"unicode": "⠉", "dots": "100100"},
    ")": {"unicode": "⠊", "dots": "010100"},
    "*": {"unicode": "⠋", "dots": "110100"},
    "+": {"unicode": "⠌", "dots": "001100"},
    "\\": {"unicode": "⠳", "dots": "110101"},
    "<": {"unicode": "⠬", "dots": "001110"},
    "=": {"unicode": "⠿", "dots": "111110"},
    ">": {"unicode": "⠜", "dots": "100110"},
    "@": {"unicode": "⠈", "dots": "000100"},
    "[": {"unicode": "⠪", "dots": "010101"},
    "]": {"unicode": "⠻", "dots": "011101"},
}

# Optional: direct lookup for single characters (letters + punct + space)
CHAR_MAP = {" ": SPACE}
CHAR_MAP.update({k: {"name": k, **v} for k, v in LETTERS.items()})
CHAR_MAP.update({k: {"name": k, **v} for k, v in PUNCT.items()})
