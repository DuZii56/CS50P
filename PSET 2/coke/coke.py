coins = [1, 5, 10, 25, 50]

def main():
    due = 50
    print("Amount due: 50")
    amount = int(input("Insert coin: "))

    while due >= 0:
        while amount not in coins:
            print("Amount due: " + str(due))
            amount = int(input("Insert coin: "))
        due = due - amount
        if due < 0:
            print("Change owed: " + str(due * -1))
        elif due == 0:
            print("Change owed: 0")
            break
        elif due > 0:
            print("Amount due: " + str(due))
            amount = int(input("Insert coin: "))

main()
