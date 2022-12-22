import csv
import sys

def main():
    with open(sys.argv[1], 'r') as csvfile:
        with open(sys.argv[2], 'w') as after_csv:
            header = ['first', 'last', 'house']
            data = csv.reader(csvfile)
            writer = csv.writer(after_csv)
            new_row = []
            for row in data:
                temp = []
                newest_new_row = row[0].split(',')
                if newest_new_row[0] == "name":
                    continue
                temp.append(newest_new_row[1].replace(" ", ""))
                temp.append(newest_new_row[0])
                temp.append(row[1])
                new_row.append(temp)
            writer.writerow(header)
            writer.writerows(new_row)


if __name__ == "__main__":
    main()
    sys.exit(0)
