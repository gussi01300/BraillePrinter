import sys
from pathlib import Path
from encoder import encode_cells
from braille_typesetting_algorithm import typeset
from formater import format
from brf_core import process_brf_file, braille_dot_position



def handle_txt(file_path: Path):
    print(".txt file detected")
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    out = format(typeset(encode_cells(text)))
    out_list = []
    for page, page_dots in out.items():
        dots = []
        for dot in page_dots:
            dots.append(braille_dot_position(dot))
        out_list.append(dots)
    show_braille_viewer(
        page_data=out_list,
        page_width_mm=page_spec.width_mm,
        page_height_mm=page_spec.height_mm,
        margin_left_mm=10,  # Fixed margin for txt files
        margin_right_mm=page_spec.margin_right_mm,
        margin_top_mm=page_spec.margin_top_mm,
        margin_bottom_mm=page_spec.margin_bottom_mm,
        scale=4
    )   

def handle_brf(file_path: Path):
    print(".brf file detected")
    process_brf_file(file_path)

    

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

    elif file_path.suffix == ".brf":
        handle_brf(file_path)
    
    else:
        print("Unsupported file type.")
    

if __name__ == "__main__":
    main()
