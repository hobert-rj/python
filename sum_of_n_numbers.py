from validInput import inputNum


def sumOfnNumbers(number: int):
    sum = 0
    for num in range(1, number+1):
        sum += num
    return sum


sum = sumOfnNumbers(inputNum("Enter the number... ", downLim=0))
print(f"result: {sum}")
