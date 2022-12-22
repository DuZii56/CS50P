import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    x = re.findall(r"\bu.?m", s.lower())
    return (x.count('um'))


if __name__ == "__main__":
    main()
