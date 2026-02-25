import sys
from pathlib import Path
from encoder import encode_cells
from braille_typesetting_algorithm import typeset
from formater import format
from brf_core import process_brf_file, braille_dot_position
from braille_viewer import show_braille_viewer
from pagespec import PageSpec

page_spec = PageSpec()

with open(sys.argv[1], "r", encoding="utf-8") as f:
    text = f.read()

out = format(typeset(encode_cells(text)))




CELL_PITCH_X = 6.0
LINE_PITCH_Y = 10.0
MARGIN_X = 15.0
MARGIN_Y = 15.0

def xy_to_col_row(x, y):
    col = round((x - MARGIN_X) / CELL_PITCH_X)
    row = round((y - MARGIN_Y) / LINE_PITCH_Y)
    return col, row

def dump_page(page):
    # page = list of (ch, x, y)
    rows = {}
    for ch, x, y in page:
        col, row = xy_to_col_row(x, y)
        rows.setdefault(row, {})[col] = ch

    for row in sorted(rows):
        line = "".join(rows[row].get(c, " ") for c in range(30))
        print(f"{row:02d} | {line}")

dump_page(out[0])