from pagespec import PageSpec

specs = PageSpec()

for line in range(specs.max_lines):
  for col in range(specs.max_cols):
    coordinate = (col, line)
    print(coordinate)
