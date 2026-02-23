from encoder import encode_cells
from braille_typesetting_algorithm import typeset
from typing import List

def main(text: str) -> List:
    out = typeset(encode_cells(text))
    return out
    

if __name__ == "__main__":
    main()
