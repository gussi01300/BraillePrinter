from main import main
from pagespec import PageSpec

cells = main("An apple is the round, edible fruit of an apple tree (Malus spp.). Fruit trees of the orchard or domestic apple (Malus domestica), the most widely grown in the genus, are cultivated worldwide. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found. Apples have been grown for thousands of years in Eurasia before they were introduced to North America by European colonists. Apples have cultural significance in many mythologies (including Norse and Greek) and religions (such as Christianity in Europe).")

bucket = {}
specs = PageSpec()

for i in cells:
    x_mm, y_mm = specs.cell_to_mm(i.col, i.row)
    print(x_mm, y_mm, i.page, i.Cell_info.name)