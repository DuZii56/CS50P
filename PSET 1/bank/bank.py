greeting = input('Greeting: ').lower().replace(" ", "")
first_word = 'hello'
first_char = 'h'

if (greeting.startswith(first_word)):
    print('$0')
elif (greeting.startswith(first_char)):
    print('$20')
else:
    print('$100')
