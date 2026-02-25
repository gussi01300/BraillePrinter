import sys
from pathlib import Path
from encoder import encode_cells
from braille_typesetting_algorithm import typeset
from formater import format
from brf_core import process_brf_file, braille_dot_position
from braille_viewer import show_braille_viewer
from pagespec import PageSpec
from brf_core import A4_HEIGHT, A4_WIDTH, MARGIN_LEFT,MARGIN_RIGHT,MARGIN_TOP, MARGIN_BOTTOM, CELL_WIDTH, CELL_HEIGHT
from dot2gcode import dots_to_gcode,save_gcode

def handle_txt(file_path: Path):
    print(".txt file detected")
    page_spec = PageSpec()
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    out = format(typeset(encode_cells(text)))
    
    out_list = []

    for page_dots in out:
        page_list = []
        for dot in page_dots:
            dot_pos = braille_dot_position(dot[0], dot[1], dot[2], page_spec.cell_width, page_spec.cell_height)
            page_list.extend(dot_pos)
        out_list.append(page_list)
    print(out)
    print(out_list)

    show_braille_viewer(
        page_data=out_list,
        page_width_mm=page_spec.paper_w,
        page_height_mm=page_spec.paper_h,
        margin_left_mm=page_spec.margin_left,
        margin_right_mm=page_spec.margin_right,
        margin_top_mm=page_spec.margin_top,
        margin_bottom_mm=page_spec.margin_bottom,
        scale=4
    )   

def handle_brf(file_path: Path):
    print(".brf file detected")
    dots_positions = process_brf_file(file_path)
    show_braille_viewer(
    page_data=dots_positions,
    page_width_mm=A4_WIDTH,
    page_height_mm=A4_HEIGHT,
    margin_left_mm=MARGIN_LEFT,
    margin_right_mm=MARGIN_RIGHT,
    margin_top_mm=MARGIN_TOP,
    margin_bottom_mm=MARGIN_BOTTOM,
    scale=4  # 1mm = 4 pixels (larger scale for better visibility)
    )
    print("Generating gcode...")
    gcode = dots_to_gcode(dots_positions)
    print(gcode)
    if input("Do you want to save gcode? Press y/n to save...") == "y":
        save_gcode(gcode, file_path.with_suffix('.gcode'))
    print("Done.Have a nice day!")    



def welcome_page():
    print('''
$$$$$$$\                      $$\ $$\ $$\           $$$$$$$\            $$\             $$\                         
$$  __$$\                     \__|$$ |$$ |          $$  __$$\           \__|            $$ |                        
$$ |  $$ | $$$$$$\   $$$$$$\  $$\ $$ |$$ | $$$$$$\  $$ |  $$ | $$$$$$\  $$\ $$$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  
$$$$$$$\ |$$  __$$\  \____$$\ $$ |$$ |$$ |$$  __$$\ $$$$$$$  |$$  __$$\ $$ |$$  __$$\ \_$$  _|  $$  __$$\ $$  __$$\ 
$$  __$$\ $$ |  \__| $$$$$$$ |$$ |$$ |$$ |$$$$$$$$ |$$  ____/ $$ |  \__|$$ |$$ |  $$ |  $$ |    $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |      $$  __$$ |$$ |$$ |$$ |$$   ____|$$ |      $$ |      $$ |$$ |  $$ |  $$ |$$\ $$   ____|$$ |      
$$$$$$$  |$$ |      \$$$$$$$ |$$ |$$ |$$ |\$$$$$$$\ $$ |      $$ |      $$ |$$ |  $$ |  \$$$$  |\$$$$$$$\ $$ |      
\_______/ \__|       \_______|\__|\__|\__| \_______|\__|      \__|      \__|\__|  \__|   \____/  \_______|\__|      
                                                                                                                    
                                                                                                                    
                                                                                                                                                                                                                                            
$$\    $$\  $$$$$$\        $$\   
$$ |   $$ |$$$ __$$\     $$$$ |  
$$ |   $$ |$$$$\ $$ |    \_$$ |  
\$$\  $$  |$$\$$\$$ |      $$ |  
 \$$\$$  / $$ \$$$$ |      $$ |  
  \$$$  /  $$ |\$$$ |      $$ |  
   \$  /   \$$$$$$  /$$\ $$$$$$\ 
    \_/     \______/ \__|\______|
                      
Welcome to Braille Printer!
This tool converts text and BRF files into G-Code for printing.                                                                                                                   
                                                                                                                          
''')    

def main():
    if len(sys.argv) < 2:
        print("main.py <file>")
        sys.exit(1)
        
    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print("File not found.")
        sys.exit()
    
    welcome_page()
    
    if file_path.suffix == ".txt":
        handle_txt(file_path)

    elif file_path.suffix == ".brf":
        handle_brf(file_path)
    
    else:
        print("Unsupported file type.")
    

if __name__ == "__main__":
    main()
