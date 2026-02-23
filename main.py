from encoder import encode_cells
from braille_typesetting_algorithm import typeset

def main():

    text = "Ab 12.5!"
    out = typeset(encode_cells(text))
    print(out)
    

if __name__ == "__main__":
    main()
