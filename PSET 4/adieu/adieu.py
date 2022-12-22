import sys

names = []
running = True

def main():
    try:
        n = input("Name: ")
        names.append(n)
    finally:
        while running:
            try:
                n = input("Name: ")
                names.append(n)
            except EOFError:
                if len(names) == 1:
                    print("\nAdieu, adieu, to " + str(names[0]))
                    sys.exit()
                elif len(names) == 2 :
                    print("\nAdieu, adieu, to " + str(names[0]) + " and " + str(names[1]))
                    sys.exit()
                elif len(names) > 2:
                    print("\nAdieu, adieu, to " + (", ".join([str(item) for item in names[0:-1]])) + ", and " + str(names[-1]))
                    sys.exit()

main()
