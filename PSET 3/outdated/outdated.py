months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

numbers = {"1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "10": "10",
    "11": "11",
    "12": "12"
}

converted = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

valid_days = {
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
}

running = True

def main():
    while running:
        try:
            date = input("Date: ").title()
            date = date.replace("/", " ").replace(",", " ")
            split_date = date.split(" ")
        finally:
            try:
                if split_date[0] in months and split_date[1] in valid_days:
                    pass
                if split_date[0] not in months and split_date[1] not in valid_days:
                    pass
                if split_date[0] or split_date[2] not in numbers and split_date[1] not in valid_days:
                    pass
                if (len(split_date) > 3):
                    if (split_date[3] == ""):
                        pass
            except KeyError:
                pass
            finally:
                try:
                    if split_date[0] in months and split_date[1] in valid_days and split_date[2] == "":
                        print(split_date[3] + '-' + converted[split_date[0]] + '-' + numbers[split_date[1]])
                        break
                    if split_date[0] and split_date[1] in numbers and split_date[1] in valid_days:
                        print(split_date[2] + '-' + numbers[split_date[0]] + '-' + numbers[split_date[1]])
                        break
                    if split_date[0] and split_date[1] in numbers and split_date[1] in valid_days and len(split_date) == 3:
                        print(split_date[2] + '-' + numbers[split_date[0]] + '-' + numbers[split_date[1]])
                        break
                    if split_date[0] == "" and split_date[4] == "":
                        print(split_date[3] + '-' + numbers[split_date[1]] + '-' + numbers[split_date[2]])
                        break
                except KeyError:
                    pass

main()
