menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

running = True

def program_exit():
    exit()

def main():

    try:
        order = input("Item: ").title()
    except KeyError:
        pass
    except EOFError:
        program_exit()
    try:
        total = menu[order]
        print(f"Total: ${total:.2f}")
    except KeyError:
        pass
    try:
        while running:
            try:
                order = input("Item: ").title()
                total = total + menu[order]
                print(f"Total: ${total:.2f}")
                while True:
                    order = input("Item: ").title()
                    total = total + menu[order]
                    print(f"Total: ${total:.2f}")
            except KeyError:
                pass
            except EOFError:
                program_exit()
    finally:
        print(f"Total: ${total:.2f}")

main()
