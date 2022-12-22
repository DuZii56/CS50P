import datetime
from datetime import date
import sys
import inflect


def main():
    start = input("Date of Birth: ")
    dob = get_dob(start)
    end = date.today()
    diff = end - dob
    minutes = (diff.days * 1440)
    inflector = inflect.engine()
    print((inflector.number_to_words(minutes, andword='').capitalize()), "minutes")


def get_dob(s):
    try:
        dob = date.fromisoformat(s)
    except ValueError:
        print("Invalid date")
        sys.exit(1)
    return dob


if __name__ == "__main__":
    main()
