from encoder import encode_cells
from formater import format
from braille_typesetting_algorithm import typeset
from typing import List

def main(text: str) -> List:
    out = format(typeset(encode_cells(text)))
    return out
    


if __name__ == "__main__":
    main()
