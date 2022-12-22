import random
import sys

running = True

def main():
    try:
        n = int(input("Level: "))
        while n <= 0:
            n = int(input("Level: "))
    except ValueError:
        n = int(input("Level: "))
    answer = random.randint(1, n)
    try:
        guess = int(input("Guess: "))
    except ValueError:
        guess = int(input("Guess: "))
    while running:
        try:
            if guess < answer:
                print("Too small!")
                guess = int(input("Guess: "))
            elif guess > answer:
                print("Too large!")
                guess = int(input("Guess: "))
            elif guess == answer:
                print("Just right!")
                sys.exit()
        except ValueError:
            guess = int(input("Guess: "))

main()
