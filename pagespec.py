from dataclasses import dataclass
import math

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
    cell_with: float = 3.0
    cell_height: float = 6.0

    @property
    def usable_w(self) -> float:
        return self.paper_w - self.margin_left - self.margin_right

    @property
    def usable_h(self) -> float:
        return self.paper_h - self.margin_top - self.margin_bottom

    @property
    def max_cols(self) -> int:
        return math.floor(self.usable_w / self.cell_pitch_x)

    @property
    def max_lines(self) -> int:
        return math.floor(self.usable_h / self.line_pitch_y)
    
    def validate(self) -> None:
        if self.cell_pitch_x < self.cell_width:
            raise ValueError("cell_pitch_x must be >= cell_width (otherwise cells overlap).")
        if self.line_pitch_y < self.cell_height:
            raise ValueError("line_pitch_y must be >= cell_height (otherwise lines overlap).")
        if self.usable_w <= 0 or self.usable_h <= 0:
            raise ValueError("Margins too large: no usable area left.")