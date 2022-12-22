meaning = input(str("What is the answer to the Great Question of Life, the Universe and Everything? ")).lower().replace(" ", "").replace("-", "")

if meaning == '42' or meaning == 'fortytwo':
    print('Yes')
else:
    print('No')
