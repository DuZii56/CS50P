def change_case(s):
    res = [s[0].lower()]
    for c in s[1:]:
        if c in ('ABCEDFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
    return ''.join(res)

s = input("camelCase: ")
print (change_case(s))
