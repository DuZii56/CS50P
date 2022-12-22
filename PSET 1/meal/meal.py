def main():
    time = input("What time is it? ").split(":")

    if convert(time) >= 7.0 and convert(time)<= 8.00:
        print("Breakfast time")
    elif convert(time) >= 12.0 and convert(time)<= 13.00:
        print("Lunch time")
    elif convert(time) >= 18.0 and convert(time)<= 19.00:
        print("Dinner time")
    else:
        None

def convert(time):
    return float(time[0]) + float(time[1]) / 60


if __name__ == "__main__":
    main()
