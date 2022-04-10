# a = [1, 2, 3]
# print(a[4])
from asyncio.windows_events import NULL
from typing import Union


def ab(a, b: int = 'undefined', c: int = 'undefined'):
    print("b")
    if a > b:
        print("aaa")


# ab(2, c=2)


def inputNum(message: str, isfloat=False, downLim: float = '-infinity', upLim: float = 'infinity') -> Union[int, float]:
    """Returns a valid conditional integer or float from the user.\n
    message: str => input message\n
    isfloat: default=False | True => interger | float\n
    range: [downLim, upLim]\n
    downLim: default=-infinity | float\n
    upLim: default=infinity | float"""
    while 1:
        try:
            val = float(input(message))
            if not isfloat:
                val = int(val)
        except ValueError:
            print("That\'s not a number! Try again!")
        else:
            try:
                uval = val <= upLim
            except TypeError:
                uval = True
            try:
                dval = val >= downLim
            except TypeError:
                dval = True
            if (upLim == 'infinity' or uval) and (downLim == '-infinity' or dval):
                return val
            else:
                print(
                    f"Please enter a number between {downLim} and {upLim}! Try again!")

# print(inputNum("enter... ", True,downLim=5,upLim=10))
# print(inputNum("enter... ", True,downLim=5,upLim=10))
# print(inputNum("enter... ", True,downLim=5,upLim=10))
# print(inputNum("enter... ", True,downLim=5,upLim=10))
# print(inputNum("enter... ", True,upLim=10))
# print(inputNum("enter... ", True,upLim=10))
# print(inputNum("enter... ", True,upLim=10))
# print(inputNum("enter... ", True,downLim=5))
# print(inputNum("enter... ", True,downLim=5))
# print(inputNum("enter... ", True,downLim=5))
print(inputNum("enter... "))
