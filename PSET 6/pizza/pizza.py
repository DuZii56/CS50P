from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) <= 1:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    file_name = sys.argv[1]
    if file_name == "sicilian.csv" or file_name == "regular.csv":
        with open(file_name, 'r') as csvfile:
            pizza_data = csv.reader(csvfile)
            print(tabulate(pizza_data, headers='firstrow', tablefmt='grid'))
    elif file_name[-3:] != "csv":
        print("Not a CSV file.")
        sys.exit(1)
    else:
        print("File does not exist")
        sys.exit(1)


main()
