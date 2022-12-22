def main():
    try:
        fuel = (input("Fraction: ")).replace("/", " ").split()
    finally:
        try:
            while (int(fuel[1]) == 0):
                print("ZeroDivisionError")
                fuel = (input("Fraction: ")).replace("/", " ").split()
            while ((int(fuel[0])) > (int(fuel[1]))):
                fuel = (input("Fraction: ")).replace("/", " ").split()
        except ValueError:
            print("ValueError")
            fuel = (input("Fraction: ")).replace("/", " ").split()
        except IndexError:
            print("ValueError")
            fuel = (input("Fraction: ")).replace("/", " ").split()
        finally:
            x = int(fuel[0])
            y = int(fuel[1])
            z = ("{:.0%}".format(x / y))
            if z == "100%":
                print("F")
            elif z == "99%":
                print("F")
            elif z == "0%":
                print("E")
            elif z == ("1%"):
                print("E")
            else:
                print(z)

main()
