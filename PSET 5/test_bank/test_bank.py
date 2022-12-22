from bank import value
import sys

def main():
    test_value()
    sys.exit(0)


def test_hello():
    if value('Hello') != 0:
        print("Such bad code.  Many Errors.  Wow.")
        sys.exit(1)

def test_hey():
    if value('Hey') != 20:
        print("Such bad code.  Many Errors.  Wow.")
        sys.exit(1)

def test_sup():
    if value('Sup') != 100:
        print("Such bad code.  Many Errors.  Wow.")
        sys.exit(1)

if __name__ == "__main__":
    main()
