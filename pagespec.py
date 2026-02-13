from dataclasses import dataclass

@dataclass(frozen=True)
#Specs for A4
class PageSpec:
    paper_w: float = 210.0
    paper_h: float = 297.0
    margin_left: float = 15.0
    margin_right: float = 15.0
    margin_top: float = 15.0
    margin_bottom: float = 15.0
    cell_pitch_x: float = 6.0
    line_pitch_y: float = 10.0
    cell_with: float = 5.0
    cell_height: float = 7.0