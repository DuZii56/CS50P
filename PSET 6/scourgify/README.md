Implement a program that:

Expects the user to provide two command-line arguments:

The name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
