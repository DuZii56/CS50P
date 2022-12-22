import sys

def main():
    sys.exit(0)


def convert(fraction):
    fraction = fraction.split("/")
    try:
        while (int(fraction[1]) == 0):
            raise ZeroDivisionError
            #fraction = (input("Fraction: ")).replace("/", " ").split()
        while ((int(fraction[0])) > (int(fraction[1]))):
            fraction = (input("Fraction: ")).replace("/", " ").split()
    except ValueError:
        print("ValueError")
        fraction = (input("Fraction: ")).replace("/", " ").split()
    except IndexError:
        print("ValueError")
        fraction = (input("Fraction: ")).replace("/", " ").split()
    finally:
        try:
            x = int(fraction[0])
        except ValueError:
            return ValueError
        y = int(fraction[1])
        try:
            z = ("{:.0%}".format(x / y))
        except ZeroDivisionError:
            return ZeroDivisionError
        return z


def gauge(percentage):
    if percentage == "100%":
        return "F"
    elif percentage == "99%":
        return "F"
    elif percentage == "0%":
        return "E"
    elif percentage == "1%":
        return "E"
    else:
        return percentage


if __name__ == "__main__":
    main()
