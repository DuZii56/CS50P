vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

def main():
    tweet = input("Input: ")
    twt = tweet
    for _ in tweet:
        if _ in vowels:
            twt = twt.replace(_, "")
    print("Output:", twt)


main()
