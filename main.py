
from braille_encode import txt_to_braille




is_dotmode = True          #True returns a list with the dotpatterns, False returns a braille string
txt = "The quick brown fox jumps over the 99 lazy dogs."


print(txt_to_braille(txt,is_dotmode))