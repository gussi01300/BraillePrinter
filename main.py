import csv
from datetime import datetime

braille_table = {

    # Letters
    "a": {"unicode": "⠁", "bin": "100000"},
    "b": {"unicode": "⠃", "bin": "110000"},
    "c": {"unicode": "⠉", "bin": "100100"},
    "d": {"unicode": "⠙", "bin": "100110"},
    "e": {"unicode": "⠑", "bin": "100010"},
    "f": {"unicode": "⠋", "bin": "110100"},
    "g": {"unicode": "⠛", "bin": "110110"},
    "h": {"unicode": "⠓", "bin": "110010"},
    "i": {"unicode": "⠊", "bin": "010100"},
    "j": {"unicode": "⠚", "bin": "010110"},
    "k": {"unicode": "⠅", "bin": "101000"},
    "l": {"unicode": "⠇", "bin": "111000"},
    "m": {"unicode": "⠍", "bin": "101100"},
    "n": {"unicode": "⠝", "bin": "101110"},
    "o": {"unicode": "⠕", "bin": "101010"},
    "p": {"unicode": "⠏", "bin": "111100"},
    "q": {"unicode": "⠟", "bin": "111110"},
    "r": {"unicode": "⠗", "bin": "111010"},
    "s": {"unicode": "⠎", "bin": "011100"},
    "t": {"unicode": "⠞", "bin": "011110"},
    "u": {"unicode": "⠥", "bin": "101001"},
    "v": {"unicode": "⠧", "bin": "111001"},
    "w": {"unicode": "⠺", "bin": "010111"},
    "x": {"unicode": "⠭", "bin": "101101"},
    "y": {"unicode": "⠽", "bin": "101111"},
    "z": {"unicode": "⠵", "bin": "101011"},

    # Numbers (same shapes as a–j)
    "1": {"unicode": "⠁", "bin": "100000"},
    "2": {"unicode": "⠃", "bin": "110000"},
    "3": {"unicode": "⠉", "bin": "100100"},
    "4": {"unicode": "⠙", "bin": "100110"},
    "5": {"unicode": "⠑", "bin": "100010"},
    "6": {"unicode": "⠋", "bin": "110100"},
    "7": {"unicode": "⠛", "bin": "110110"},
    "8": {"unicode": "⠓", "bin": "110010"},
    "9": {"unicode": "⠊", "bin": "010100"},
    "0": {"unicode": "⠚", "bin": "010110"},

    # Special signs
    "number_sign": {"unicode": "⠼", "bin": "001111"},
    "capital_sign": {"unicode": "⠠", "bin": "000001"},
    " ": {"unicode": "⠀", "bin": "000000"},

    # Punctuation
    ".": {"unicode": "⠲", "bin": "010011"},
    ",": {"unicode": "⠂", "bin": "010000"},
    ";": {"unicode": "⠆", "bin": "011000"},
    ":": {"unicode": "⠒", "bin": "010010"},
    "?": {"unicode": "⠦", "bin": "011001"},
    "!": {"unicode": "⠖", "bin": "011010"},
    "'": {"unicode": "⠄", "bin": "001000"},
    "-": {"unicode": "⠤", "bin": "001001"},
    "/": {"unicode": "⠌", "bin": "001100"}
}


def txt_to_braille(text, dotmode):
    parts = []
    number_mode = False
    if dotmode:
        mode = "bin"
    else:
        mode = "unicode"
    for char in text:

        is_digit = char.isdigit()
        is_upper = char.isupper()

        if is_digit and not number_mode:
            parts.append(braille_table["number_sign"][mode])
        if is_upper:
            parts.append(braille_table["capital_sign"][mode])

        parts.append(braille_table[char.lower()][mode])

        number_mode = is_digit
    if dotmode:
        return parts
    else:
        return "".join(parts)

def txt_to_dotpattern(text):
    dotpattern = []
    for char in text:
        char = char.lower()
        dotpattern.append(braille_table[char]["bin"])
    return dotpattern

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
def save_list_to_csv(data, filename=f"/Users/gustav/Code/Python/BraillePrinter/CSV_Outputs/DebugFrom{timestamp}"): #Temporary Output, is in .gitignore
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)





txt = "The quick brown fox jumps over the 99 lazy dogs."


print(txt_to_braille(txt,False))