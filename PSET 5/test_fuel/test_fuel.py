from fuel import convert, gauge
import sys
import pytest


def main():
    test_empty()
    test_full()
    test_percent()
    test_ints()
    test_ZeroDivisionError()
    test_ValueError()
    sys.exit(0)


def test_empty():
    if gauge(1) == "E":
        assert True
    elif gauge(1) != "E":
        assert False

def test_full():
    if gauge(99) == "F":
        assert True
    elif gauge(99) != "F":
        assert False

def test_percent():
    if gauge(50) == "50%":
        assert True
    elif gauge(50) != "50%":
        assert False

def test_ints():
    if convert("25/100") == 25:
        assert True
    elif convert("25/100") != 25:
        assert False

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("a/b")

if __name__ == "__main__":
    main()
