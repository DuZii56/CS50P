shortcut = {
    ":thumbsup:": "👍",
    ":1stplacemedal:": "🥇",
    ":moneybag:": "💰",
    ":smilecat:": "😸",
    ":candy:": "🍬"
}

def main():
    x = input("Input: ").lower().replace("_", "")
    if x in shortcut:
        print(shortcut[x])

main()
