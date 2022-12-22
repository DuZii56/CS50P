import sys

first_word = 'hello'
first_char = 'h'

def main():
    greeting = value(input('Greeting: ').lower().replace(" ", ""))
    print(greeting)
    sys.exit(0)


def value(greeting):
    if (greeting.startswith(first_word)):
        return(0)
    elif (greeting.startswith(first_char)):
        return(20)
    else:
        return(100)


if __name__ == "__main__":
    main()
