from um import count
import pytest


def test_normal():
    assert count("um") == 1


def test_counting():
    assert count("Um, this is, um, a very yummy cookie.") == 2


def test_within_word():
    assert count("yummy") == 0


def test_uppercase():
    assert count("Um, what?") == 1


if __name__ == "__main__":
    main()
