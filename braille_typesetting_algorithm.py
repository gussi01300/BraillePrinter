from pagespec import PageSpec
from dataclasses import dataclass
from encoder import Cell
from typing import List, Tuple


specs = PageSpec()

@dataclass 
class Positioned_Cell:
    Cell_info: Cell
    col: int
    row: int
    page: int
    

def typeset(cells: List[Cell]) -> List[Positioned_Cell]:
    out = []
    word_cells = []
    i = 0
    row = 0
    col = 0
    page = 1

    while i < len(cells):

        if cells[i].name != "space":
            word_cells.append(cells[i])

        else:
            word_cells, col, row, out, page = pack(word_cells, col, row, out, page)

        i += 1

    word_cells, col, row, out, page = pack(word_cells, col, row, out, page)
    # Remove trailing space if present
    if out and out[-1].Cell_info.name == "space":
        out.pop()

    return out

def pack(word_cells: List[Cell], current_col: int, line: int, out: List[Positioned_Cell], page: int) -> Tuple[List[Cell], int, int, List[Positioned_Cell], int]:
    max_cols = specs.max_cols
    word_length = len(word_cells)

    #If word length is bigger that max_cols (Hardbreak)
    if word_length > max_cols:

        for i in word_cells:

            if current_col >= max_cols:
                line += 1
                line, page = Checkpage(line, page)
                current_col = 0

            out.append(Positioned_Cell(Cell_info = i, col = current_col, row = line, page = page))
            current_col += 1

        if current_col >= max_cols:
            line += 1
            line, page = Checkpage(line, page)
            current_col = 0

        else:   
            out.append(Positioned_Cell(Cell_info = Cell(name = "space", dots = "000000", unicode = "⠀"), col = current_col, row = line, page = page))
            current_col += 1

        return [], current_col, line, out, page
    
    #If word doesn't fit in the current collum (Next line)
    if word_length > max_cols - current_col:

        line += 1
        line, page = Checkpage(line, page)
        current_col = 0

        for i in (word_cells):
            out.append(Positioned_Cell(Cell_info = i, col = current_col, row = line, page = page))
            current_col += 1

        if current_col >= max_cols:
            line += 1
            line, page = Checkpage(line, page)
            current_col = 0

        else:
            out.append(Positioned_Cell(Cell_info = Cell(name = "space", dots = "000000", unicode = "⠀"), col = current_col, row = line, page = page))
            current_col += 1

        return [], current_col, line, out, page
    
    #If word fits normally in the remaining collums
    if word_length <= max_cols - current_col:

        for i in word_cells:
            out.append(Positioned_Cell(Cell_info = i, col = current_col, row = line, page = page))
            current_col += 1

        if current_col >= max_cols:
            line += 1
            line, page = Checkpage(line, page)
            current_col = 0

        else:
            out.append(Positioned_Cell(Cell_info = Cell(name = "space", dots = "000000", unicode = "⠀"), col = current_col, row = line, page = page))
            current_col += 1

        return [], current_col, line, out, page

def Checkpage(line: int, page: int) -> Tuple[int, int]:
    if line >= specs.max_lines:
        line = 0
        page += 1
    return line, page
    


