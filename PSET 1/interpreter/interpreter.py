expression = input('Expression: ')
elements = expression.split(" ")

x = float(elements[0])
y = elements[1]
z = float(elements[2])

if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
elif y == '/':
    print(f"{x / z:.1f}")
else:
    none
