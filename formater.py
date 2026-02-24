from pagespec import PageSpec
from typing import List
from braille_typesetting_algorithm import Positioned_Cell


def format(cells: List[Positioned_Cell]) -> List:

    pages_dict = {}
    specs = PageSpec()
    for i in cells:

        if i.page not in pages_dict:
            pages_dict[i.page] = []
        
        x_mm, y_mm = specs.cell_to_mm(i.col, i.row)
        pages_dict[i.page].append((x_mm, y_mm, i.Cell_info.unicode))

    return pages_dict


