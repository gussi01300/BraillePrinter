from braille_map import BRAILLE_MAP as braille_table

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