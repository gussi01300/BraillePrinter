from pagespec import PageSpec
from typing import List, Dict
from braille_typesetting_algorithm import Positioned_Cell


def format(cells: List[Positioned_Cell]) -> List:
    pages_dict = {}
    specs = PageSpec()
    for i in cells:

        if i.page not in pages_dict:
            pages_dict[i.page] = []
        
        x_mm, y_mm = specs.cell_to_mm(i.col, i.row)
        pages_dict[i.page].append((i.Cell_info.unicode, x_mm, y_mm))

    out = dict_to_list(pages_dict)

    return out

def dict_to_list(Cell_dict: Dict) -> List:
    outline_list = []
    for values in Cell_dict.values():
        outline_list.append(values)

    return outline_list
