def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    number_seen = False

    for c in s[0:2]:
        if c not in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            return False

    for c in s[2:6]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') and number_seen == False:
            continue

        if c not in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789') and number_seen == False:
            return False

        if c in ('123456789'):
            number_seen = True

        if c not in ('0123456789'):
            return False

    return True

if __name__ == "__main__":
    main()
