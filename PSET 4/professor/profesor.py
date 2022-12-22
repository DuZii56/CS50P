import random
import sys

def main():
    score = 0
    int_range = get_level()
    for problems in range(10):
        counter = 0
        x, y = generate_integer(int_range)
        z = x + y
        guess = int(input(str(x) + " + " + str(y) + " = "))
        for counter in range(3):
            if guess != z:
                print("EEE")
                counter = counter + 1
                if counter == 3:
                    print(z)
                    continue
                guess = int(input(str(x) + " + " + str(y) + " = "))
            elif guess == z:
                score = score + 1
                break
    print("Score: " + str(score))


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl == 1:
                return range(0, 10)
            elif lvl == 2:
                return range(10, 100)
            elif lvl == 3:
                return range(100, 1000)
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    x = random.randint(level[0], level[-1])
    y = random.randint(level[0], level[-1])
    return x, y


if __name__ == "__main__":
    main()
    sys.exit(0)
