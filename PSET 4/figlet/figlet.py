import sys
from pyfiglet import Figlet

def main():
    if sys.argv[1] != '-f':
        print("Invalid usage")
        sys.exit(1)
    try:
        user_input = input("Input: ")
        if sys.argv[1] == '-f' and sys.argv[2] == 'slant':
            f = Figlet(font='slant')
        elif sys.argv[1] == '-f' and sys.argv[2] == 'rectangles':
            f = Figlet(font='rectangles')
        elif sys.argv[1] == '-f' and sys.argv[2] == 'alphabet':
            f = Figlet(font='alphabet')
    finally:
        print(f.renderText(user_input))

main()
