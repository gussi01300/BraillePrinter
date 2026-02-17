from pagespec import PageSpec

specs = PageSpec()
def calc_coordinates():
    for line in range(specs.max_lines):
      for col in range(specs.max_cols):
        coordinate = (col, line)
        print(coordinate)


calc_coordinates()
print(specs.max_cols, specs.max_lines)
#Uncompleted, I forgot linebreak rules

