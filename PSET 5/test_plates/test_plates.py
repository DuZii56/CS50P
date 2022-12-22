from plates import is_valid
import sys

def main():
    test_length()
    sys.exit(0)


def test_length():
    assert is_valid("E") == False


def test_alphabetical():
    assert is_valid("123456") == False


def test_first_zero():
    assert is_valid("AB0123") == False


def test_number_placement():
    assert is_valid("AB123C") == False


def test_alphanumeric_characters():
    assert is_valid("AB123!") == False


if __name__ == "__main__":
    main()
