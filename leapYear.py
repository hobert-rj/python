from validInput import inputNum


def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def isLeapYear2(year: int):
    if year % 400 == 0 or (year % 4 == 0 and not year % 25 == 0):
        return True
    else:
        return False


year = inputNum("Enter a year in Gregorian Calender... ", downLim=0)
if isLeapYear2(year):
    print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is a common year.")
