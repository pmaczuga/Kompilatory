import sys
import lab1_scanner
import lab2_parser

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = lab2_parser.parser
    text = file.read()
    parser.parse(text, lexer=lab1_scanner.lexer)
