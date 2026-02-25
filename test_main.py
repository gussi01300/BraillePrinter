import sys
from pathlib import Path
from encoder import encode_cells
from braille_typesetting_algorithm import typeset
from formater import format

def handle_txt(file_path: Path):
    print(".txt file detected")
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    out = format(typeset(encode_cells(text)))

    print(out)


def main():
    if len(sys.argv) < 2:
        print("main.py <file>")
        sys.exit(1)
        
    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print("File not found.")
        sys.exit()
    
    if file_path.suffix == ".txt":
        handle_txt(file_path)
    
    else:
        print("Unsupported file type.")
    

if __name__ == "__main__":
    main()