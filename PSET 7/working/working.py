import re
import sys


def main():
    x = convert(input("Hours: "))
    if x == "ValueError":
        raise ValueError
    else:
        print(x)


def convert(s):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    expression = "(1[0-2]|[1-9])(:)*([0-5][0-9])*( AM| PM) to (1[0-2]|[1-9])(:)*([0-5][0-9])*( AM| PM)"
    time = re.search(expression, s)
    if time == None:
        raise ValueError
    split_time = re.split(" to ", str(s[time.start():time.end()]))
    first_one = time_format(split_time[0])
    second_one = time_format(split_time[1])

    return first_one + " to " + second_one


def time_format(t):
    # This isn't a particularly efficeint way of doing this, but it works.
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    new_time = ""
    if t[-2] == "A":
        if ":" in t:
            new_time = t.replace(" AM", "")
            less_than_ten = new_time.split(":")
            if int(less_than_ten[0]) < 10:
                new_time = "0" + new_time
            elif int(less_than_ten[0]) == 12:
                return "00:" + less_than_ten[1]
            return new_time
        else:
            new_time = t.replace(" AM", "") + ":00"
            if(int(new_time.split(":")[0]) < 10):
                new_time = "0" + new_time
            elif int(new_time.split(":")[0]) == 12:
                return "00:00"
            return new_time
    else:
        time = t.split(" ")
        if ":" in time[0]:
            temp = time[0].split(":")
            if temp[0] in numbers:
                new_time = str(int(temp[0]) + 12) + ":" + temp[1].replace(" PM", "")
                return new_time
            elif temp[0] == "12":
                new_time = "12:" + temp[1].replace(" PM", "")
                return new_time
        else:
            if time[0] in numbers:
                new_time = str(int(time[0].replace(" PM", ""))+ 12)+ ":00"
                return new_time
            elif time[0] == "12":
                new_time = "12:00"
                return new_time


if __name__ == "__main__":
    main()
