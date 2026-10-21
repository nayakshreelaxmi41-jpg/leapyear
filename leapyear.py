import sys


def leapYear(year):
    if year % 4 == 0:
        return "Leap year"
    else:
        return "Not a leap year"


if __name__ == "__main__":
    year = int(sys.argv[1])
    print("The year is: ", leapYear(year))