# braille_viewer.py (Minimal Version)
import tkinter as tk
from tkinter import messagebox

"""
USAGE EXAMPLE 
------------------------
# 1. Prepare test data (3 pages of braille dots)
test_page_data = [
    # Page 1: Several dots in the printable area
    [(10, 20), (10, 25), (15, 20), (20, 30)],
    # Page 2: A single dot near the right margin
    [(70, 40)],
    # Page 3: Multiple dots in different positions
    [(5, 10), (80, 80), (40, 50)]
]

# 2. Configure page parameters (A4 paper size as reference)
PAGE_WIDTH_MM = 80    # Custom page width
PAGE_HEIGHT_MM = 100  # Custom page height
MARGIN_LEFT_MM = 5    # Left margin
MARGIN_RIGHT_MM = 5   # Right margin
MARGIN_TOP_MM = 10    # Top margin
MARGIN_BOTTOM_MM = 10 # Bottom margin

# 3. Launch the braille viewer
show_braille_viewer(
    page_data=test_page_data,
    page_width_mm=PAGE_WIDTH_MM,
    page_height_mm=PAGE_HEIGHT_MM,
    margin_left_mm=MARGIN_LEFT_MM,
    margin_right_mm=MARGIN_RIGHT_MM,
    margin_top_mm=MARGIN_TOP_MM,
    margin_bottom_mm=MARGIN_BOTTOM_MM,
    scale=4  # 1mm = 4 pixels (larger scale for better visibility)
)
"""

def show_braille_viewer(
    page_data,
    page_width_mm,
    page_height_mm,
    margin_left_mm,
    margin_right_mm,
    margin_top_mm,
    margin_bottom_mm,
    scale=3,
):
    """
    Display a braille dot preview window
    
    :param page_data: 3D list with the following structure:
        [
            [(x1, y1), (x2, y2), ...],  # All dots on Page 1 (relative coordinates, mm)
            [(x1, y1), (x2, y2), ...],  # All dots on Page 2 (relative coordinates, mm)
            ...
        ]
    :param page_width_mm: Page width in millimeters (mm)
    :param page_height_mm: Page height in millimeters (mm)
    :param margin_left_mm: Left margin in millimeters (mm)
    :param margin_right_mm: Right margin in millimeters (mm)
    :param margin_top_mm: Top margin in millimeters (mm)
    :param margin_bottom_mm: Bottom margin in millimeters (mm)
    :param scale: Pixel scaling ratio (1mm = scale pixels)
    """
    # Internal default configuration
    SCALE = scale  # 1mm = scale pixels
    PAGE_SPACING_MM = 10  # Default page spacing: 10mm
    
    # Internal unit conversion function: millimeters to pixels
    def _mm_to_px(mm):
        return int(mm * SCALE)
    
    total_pages = len(page_data)
    
    if total_pages == 0:
        messagebox.showwarning("Warning", "No braille content to display!")
        return
    
    # Create main window
    root = tk.Tk()
    root.title("Braille Dot Visualizer - Scroll to Browse")
    root.geometry(f"{_mm_to_px(page_width_mm)+80}x800")
    
    # ========== Scrollable Frame ==========
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    canvas_width = _mm_to_px(page_width_mm)
    canvas_total_height = _mm_to_px(page_height_mm * total_pages + PAGE_SPACING_MM * (total_pages - 1))
    canvas = tk.Canvas(
        main_frame, 
        width=canvas_width, 
        height=root.winfo_height()-40,
        yscrollcommand=scrollbar.set,
        bg="white"
    )
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar.config(command=canvas.yview)
    canvas.config(scrollregion=(0, 0, canvas_width, canvas_total_height))
    
    # ========== Drawing Logic ==========
    current_page_y_mm = 0
    dot_radius = 1  # Radius of braille dots in pixels
    
    for page_idx in range(total_pages):
        dots = page_data[page_idx]
        page_num = page_idx + 1
        
        # 1. Draw page border
        page_x_px = 0
        page_y_px = _mm_to_px(current_page_y_mm)
        page_w_px = _mm_to_px(page_width_mm)
        page_h_px = _mm_to_px(page_height_mm)
        
        canvas.create_rectangle(
            page_x_px, page_y_px, page_x_px + page_w_px, page_y_px + page_h_px,
            outline="black", width=2
        )
        
        # 2. Draw page margins (dashed gray line)
        ml_px = _mm_to_px(margin_left_mm)
        mt_px = page_y_px + _mm_to_px(margin_top_mm)
        mr_px = _mm_to_px(page_width_mm - margin_right_mm)
        mb_px = page_y_px + _mm_to_px(page_height_mm - margin_bottom_mm)
        
        canvas.create_rectangle(
            ml_px, mt_px, mr_px, mb_px,
            outline="gray", width=1, dash=(2, 2)
        )
        
        # 3. Draw page number
        canvas.create_text(
            page_w_px/2, page_y_px + 15,
            text=f"Page {page_num}",
            fill="gray", font=("Arial", 12)
        )
        
        # 4. Draw braille dots
        for (x_mm, y_mm) in dots:
            abs_x_mm = x_mm
            abs_y_mm = y_mm + current_page_y_mm
            
            x_px = _mm_to_px(abs_x_mm)
            y_px = _mm_to_px(abs_y_mm)
            
            canvas.create_oval(
                x_px - dot_radius, y_px - dot_radius,
                x_px + dot_radius, y_px + dot_radius,
                fill="black", outline=""
            )
        
        # Update Y position for next page (add page height + spacing)
        current_page_y_mm += page_height_mm + PAGE_SPACING_MM
    
    # ========== Mouse Wheel Support ==========
    def on_mouse_wheel(event):
        # Handle Windows mouse wheel (event.delta) and Linux mouse wheel (event.num)
        if event.delta:
            canvas.yview_scroll(-int(event.delta/120), "units")
        else:
            if event.num == 4: canvas.yview_scroll(-1, "units")   # Scroll up
            elif event.num == 5: canvas.yview_scroll(1, "units") # Scroll down
            
    # Bind mouse wheel events to canvas
    canvas.bind("<MouseWheel>", on_mouse_wheel) 
    
    # Start the main GUI loop
    root.mainloop()
