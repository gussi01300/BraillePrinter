'''
G1: move to position(dot)
G6: get paper in
G7: take paper out
G28: home all axes

M1: dwell for dot
M2: end of program
'''

def sort_dots(dots):
    return sorted(dots, key=lambda x: (x[1], x[0]))

def dots_to_gcode(dots_data, page_spec):
    gcode = []
    gcode.append("G28; Home all axes")
    for page_num, page_dots in dots_data.items():
        gcode.append(f"G6; Page {page_num}")
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
