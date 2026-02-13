'''
In this file, We need a typesetting algorithm that arranges Braille on A4-sized paper with three parameters: margins, line spacing, and character spacing.
It can be simplified to filling squares with certain rules in a fixed area.

===============================================
        Braille Standard Dimensions (Unit: mm)        
===============================================
| Item                                      | Specification |
+-------------------------------------------+---------------+
| Braille dot diameter (mm)                 | 1.2～1.5      |
| Braille dot height (mm)                   | 0.4～0.6      |
| Distance between dots in cell (mm)        | 2.5           |
| Single cell width (mm)                    | 5.0           |
| Single cell height (mm)                   | 7.5           |
| Character spacing (cell center distance, mm) | 6.0        |
| Line spacing (line center distance, mm)   | 10.0          |
| Recommended for body text                 | Diameter 1.2, Height 0.4 |
| Recommended for title/signage             | Diameter 1.5, Height 0.6 |
===============================================
'''

'''
BRAILLE A4 LAYOUT (6-dot) — Calculations & Results (clean baseline setup)

INPUTS
- Paper size: A4 = 210 mm × 297 mm
- Margins (clean/symmetrical): left 20 mm, right 20 mm, top 20 mm, bottom 20 mm
- Horizontal cell spacing (center-to-center): 6.0 mm
- Vertical line spacing (baseline-to-baseline): 10.0 mm
- Effective cell width: ~4.0 mm
- Free space between cells (edge-to-edge): ~2.0 mm

1) USABLE AREA (after margins)
- Usable width  = 210 − (20 + 20) = 210 − 40 = 170 mm
- Usable height = 297 − (20 + 20) = 297 − 40 = 257 mm

2) MAX CHARACTERS PER LINE (at 6.0 mm center-to-center)
- Characters = floor( Usable width / Cell spacing )
- Characters = floor( 170 / 6.0 ) = floor( 28.333... ) = 28 characters

Check:
- 28 × 6.0 = 168.0 mm  (fits within 170 mm)
- Remaining width = 170.0 − 168.0 = 2.0 mm
  (e.g., 1.0 mm left + 1.0 mm right inside the usable area)

3) MAX LINES PER PAGE (at 10.0 mm line spacing)
- Lines = floor( Usable height / Line spacing )
- Lines = floor( 257 / 10.0 ) = floor( 25.7 ) = 25 lines

Check:
- 25 × 10.0 = 250.0 mm  (fits within 257 mm)
- Remaining height = 257.0 − 250.0 = 7.0 mm
  (e.g., 3.5 mm top + 3.5 mm bottom inside the usable area)

FINAL RESULT (clean A4 grid with 20 mm margins)
- Grid: 28 characters × 25 lines
- Cell spacing (center-to-center): 6.0 mm
- Line spacing (baseline-to-baseline): 10.0 mm
- Free spacing between cells (edge-to-edge): ~2.0 mm
'''

