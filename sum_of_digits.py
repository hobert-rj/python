from typing import Union
from validInput import inputNum


def sumOfDigits(number: Union[float, int, str]):
    result = 0
    number = int(str(number).replace('-', '').replace('.', ''))
    while number:
        result += number % 10
        number //= 10
    return result


sum = sumOfDigits(inputNum("Enter the number... ", False))
print(f"result: {sum}")
