from braille_map import PUNCT, LETTERS
from BRFParser import BRFParser
from braille_viewer import show_braille_viewer

# ====================== Basic Configuration Constants ======================
# A4 paper specifications (unit: mm)
A4_WIDTH = 210
A4_HEIGHT = 297

# Braille typesetting specifications
LINES_PER_PAGE = 26  
CELLS_PER_LINE = 26  
CELL_WIDTH = 4  # mm (width of a single braille cell)
CELL_HEIGHT = 6  # mm (height of a single braille cell)
MARGIN_LEFT = 25.4  # mm
MARGIN_RIGHT = 23.4  # mm
MARGIN_TOP = 12.7  # mm
MARGIN_BOTTOM = 24.3  # mm

# Pixel scaling ratio (1mm = 3px)
SCALE = 3  

# Page spacing (vertical direction, unit: mm)
PAGE_SPACING_MM = 10  

braille_table = {**LETTERS, **PUNCT}  

# ====================== Utility Functions ======================
def mm_to_px(mm):
    """Convert millimeters to pixels"""
    return int(mm * SCALE)  

def px_to_mm(px):
    """Convert pixels to millimeters"""
    return int(px / SCALE)   

def braille_char_to_dot_position(braille_char):
    """Convert braille character to 6-dot position string"""
    if not braille_char:  # Handle empty character
        return "000000"
    if braille_char.lower() in braille_table:
        return braille_table[braille_char.lower()]["dots"]
    else:
        return "000000"

def braille_dot_position(dot_str, x_mm, y_mm, CELL_HEIGHTd, CELL_WIDTHd):
    """
    Convert 6-dot position string to specific dot coordinates, return dot position list
    :param dot_str: 6-digit braille dot position string (e.g. "101000")
    :param x_mm: Cell top-left corner x coordinate (mm)
    :param y_mm: Cell top-left corner y coordinate (mm)
    :return: List of braille dot coordinates for this character
    """
    dot_coords = []
    # Relative positions of 6 braille dots (relative to cell top-left corner)
    dot_offsets = [
        (0, 0),                  # Dot 1: Top-left
        (0, CELL_HEIGHTd / 2),    # Dot 2: Top-right
        (0, CELL_HEIGHTd),        # Dot 3: Middle-left upper
        (CELL_WIDTHd, 0),         # Dot 4: Middle-right upper
        (CELL_WIDTHd, CELL_HEIGHTd / 2),    # Dot 5: Middle-left lower
        (CELL_WIDTHd, CELL_HEIGHTd) # Dot 6: Middle-right lower
    ]
    
    for i in range(6):
        if dot_str[i] == '1':
            dot_x = x_mm + dot_offsets[i][0]
            dot_y = y_mm + dot_offsets[i][1]
            dot_coords.append((dot_x, dot_y))
    return dot_coords

def calculate_layout_spacing():
    """Calculate typesetting spacing (character spacing, line spacing)"""
    available_width = A4_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
    available_height = A4_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM

    char_spacing_horizontal = (available_width - CELLS_PER_LINE * CELL_WIDTH) / (CELLS_PER_LINE - 1) if CELLS_PER_LINE > 1 else 0
    char_spacing_vertical = (available_height - LINES_PER_PAGE * CELL_HEIGHT) / (LINES_PER_PAGE - 1) if LINES_PER_PAGE > 1 else 0

    line_spacing = CELL_HEIGHT + char_spacing_vertical
    cell_spacing = CELL_WIDTH + char_spacing_horizontal
    
    return cell_spacing, line_spacing

def process_brf_file(file_path):
    """
    Process BRF file and calculate braille dot coordinates for all pages
    
    :param file_path: BRF file path
    :return: page_data - 3D list with the following structure:
        [
            [(x1, y1), (x2, y2), ...],  # All dots on page 1 (relative coordinates)
            [(x1, y1), (x2, y2), ...],  # All dots on page 2 (relative coordinates)
            ...
        ]
    """
    pages_data = []  # Final 3D list to return
    
    # Parse BRF file
    parser = BRFParser()
    result = parser.parse_file(file_path)
    
    # Get total number of pages
    total_pages = len(result) if isinstance(result, dict) else 0
    if total_pages == 0:
        return []
    
    # Calculate typesetting spacing
    cell_spacing, line_spacing = calculate_layout_spacing()
    
    # Calculate braille dot coordinates page by page
    for page_num, page_content in result.items():
        page_dots = []  # Store all dots of current page
        
        # Starting coordinates of current page (mm, relative to page top-left corner, no global offset added)
        start_x_mm = MARGIN_LEFT
        start_y_mm = MARGIN_TOP
        
        # Iterate through lines of each page (maximum LINES_PER_PAGE lines)
        for row in range(LINES_PER_PAGE):
            # Get current line content
            if isinstance(page_content, list) and row < len(page_content):
                line_content = page_content[row]
            else:
                line_content = ""
            
            # Iterate through columns of each line (maximum CELLS_PER_LINE columns)
            for col in range(CELLS_PER_LINE):
                # Calculate cell top-left corner coordinates (mm, relative to page top-left corner)
                x_mm = start_x_mm + col * cell_spacing
                y_mm = start_y_mm + row * line_spacing

                # Get braille character at current position
                braille_char = line_content[col] if col < len(line_content) else ""
                
                # Convert to dot positions and calculate coordinates
                dot_str = braille_char_to_dot_position(braille_char)
                #char_dots = braille_dot_position_1(dot_str, x_mm, y_mm)
                char_dots = braille_dot_position(dot_str, x_mm, y_mm, CELL_HEIGHT, CELL_WIDTH)  
                page_dots.extend(char_dots)  # Add to current page list
        
        # Add current page list to final result
        pages_data.append(page_dots)
    
    return pages_data

if __name__ == "__main__":
    for page_dots in process_brf_file("blankTemplate.brf"):
        print(page_dots)
    show_braille_viewer(
        page_data=process_brf_file("blankTemplate.brf"),  
        page_height_mm=A4_HEIGHT,
        page_width_mm=A4_WIDTH,
        margin_left_mm=MARGIN_LEFT,
        margin_right_mm=MARGIN_RIGHT,
        margin_top_mm=MARGIN_TOP,
        margin_bottom_mm=MARGIN_BOTTOM,
        scale=3,
    )
