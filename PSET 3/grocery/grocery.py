grocery_list = []
seen_items = []

running = True

def main():

    skip = False

    try:
        while running:
            item = input().lower()
            grocery_list.append(item)
            grocery_list.sort()
    except EOFError:
        for item in grocery_list:
            if item in seen_items:
                pass
            if item not in seen_items:
                print(grocery_list.count(item), item.upper())
            seen_items.append(item)
        exit()

main()
