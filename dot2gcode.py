'''
G1: move to position(dot)
G6: get paper in
G7: take paper out
G28: home all axes

M1: dwell for dot
M2: end of program
'''
from tqdm import tqdm

def sort_dots(dots):
    return sorted(dots, key=lambda x: (x[1], x[0]))

def dots_to_gcode(dots_data):
    gcode = []
    gcode.append("G28; Home all axes")
    for page_dots in tqdm(dots_data, desc="Generating gcode"):
    #for page_num, page_dots in dots_data.items():
        page_dots = sort_dots(page_dots)
        # gcode.append(f"G6; Page {page_num}")
        gcode.append("G6; Get paper in")    
        if not page_dots:
            gcode.append("G7; End of page (no dots)")
            continue
        for dot in page_dots:
            x, y = dot
            gcode.append(f"G1 X{x:.2f} Y{y:.2f} Z-1.00 ; Dot at x={x}, y={y}")
            gcode.append("M1; Dwell for dot")
        gcode.append("G7; End of page")
    gcode.append("M2; End of program")
    return gcode

def save_gcode(gcode, output_path="output.gcode"):
    with open(output_path, 'w') as f:
        for line in gcode:
            f.write(line + '\n')

if __name__ == "__main__":
    from brf_core import process_brf_file
    save_gcode(dots_to_gcode(process_brf_file("blankTemplate.brf")))
