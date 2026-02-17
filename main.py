from pagespec import PageSpec
from encoder import encode_cells, measure, to_unicode, to_dotpatterns

def main():
    specs = PageSpec()

    text = "Ab 12.5!"
    cells = encode_cells(text)

    print("text:", text)
    print("cells:", measure(text))
    print("unicode:", to_unicode(text))
    print("dots:", to_dotpatterns(text))

if __name__ == "__main__":
    main()
