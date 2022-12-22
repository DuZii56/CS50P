import sys
    if len(sys.argv) > 2:
        sys.exit(1)
    if ".py" not in sys.argv[1]:
        sys.exit(1)
    lines_hello = open(sys.argv[1], 'r')
    lines = lines_hello.readlines()

    count = 0

    for l in lines:
        line = l.lstrip(' ')
        if line[0] == "#":
            pass
        elif line[0] == "\n":
            pass
        else:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
