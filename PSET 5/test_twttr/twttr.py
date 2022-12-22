vowels = ['A', 'a', 'I', 'i', 'O', 'o', 'U', 'u', "3", "!"]

def main():
    tweet = shorten(input("Input: "))
    print(tweet)

def shorten(word):
    for _ in word:
        if _ in vowels:
            word = word.replace(_, "")
    return(word)

if __name__ == "__main__":
    main()
