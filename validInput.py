from typing import Union


def inputNum(message, isInt=True, downLim: Union[int, float] = '-infinity', upLim: Union[int, float] = 'infinity') -> Union[int, float]:
    """Returns a valid conditional integer or float from the user.\n
    message: str => input message\n
    isInt: False | default=True => float | interger\n
    range: [downLim, upLim]\n
    downLim: default=-infinity | float\n
    upLim: default=infinity | float"""
    upI = upLim == 'infinity'
    dnI = downLim == '-infinity'
    if not (type(isInt) == bool and (upI or type(upLim) in (int, float)) and (dnI or type(downLim) in (int, float))):
        raise TypeError("Invalid arguments has provided to inputNum function!")
    while 1:
        try:
            val = float(input(message))
            if isInt:
                val = int(val)
        except ValueError:
            print("That\'s not a number! Try again!")
        else:
            try:
                upval = val <= upLim
            except TypeError:
                upval = True
            try:
                dnval = val >= downLim
            except TypeError:
                dnval = True
            if (upI or upval) and (dnI or dnval):
                return val
            else:
                print(
                    f"Please enter a number between {downLim} and {upLim}! Try again!")


def inputBool(message, trueMsg="yes", falseMsg="no") -> bool:
    """Takes input message,\n
    and returns a valid boolian value from the user."""
    trueMsg = trueMsg.lower()
    falseMsg = falseMsg.lower()
    while 1:
        val = input(f"{message} Type {trueMsg} or {falseMsg}... ").lower()
        if val in (trueMsg, trueMsg[0]):
            return True
        elif val in (falseMsg, falseMsg[0]):
            return False
        else:
            print("Invalid input! Try again!")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def inputLetter(message: str):
    while 1:
        val = input(message)
        if val in alphabet:
            return val
        else:
            print("Not a letter! Try again!")
