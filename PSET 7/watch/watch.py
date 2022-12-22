import re
import sys


def main():
    x = parse(input("HTML: "))
    print(x)


def parse(s):
    expression = "youtube.com/embed/[0-9a-zA-Z]+"
    url = re.search(expression, s)
    if (s[0:4]) == "http":
        return None
    if url == None:
        return None
    else:
        y = re.split("\s", str(url))
        z = str(y[4]).split("/")
        return "https://youtu.be/" + str(z[-1]).replace("'>", "")


if __name__ == "__main__":
    main()
