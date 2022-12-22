from twttr import shorten
import sys

def main():
    test_shorten()

def test_shorten():
    if shorten("twitter") != "twttr":
        print("The word was not shortened")
        sys.exit(1)
    elif shorten("twittEr") != "twttr":
        print("The word was not shortened")
        sys.exit(1)
    elif shorten("tw!tt3r") != "tw!tt3r":
        print("The word was not shortened")
        sys.exit(1)

if __name__ == "__main__":
    main()
