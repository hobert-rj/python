from random import randint
from validInput import inputNum, inputBool
Lletters = 'qwertyuiopasdfghjklzxcvbnm'
Uletters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
number = '1234567890'
symbols = '~`!@#$%^&*()_-+={[}]|\:;"\',<>.?/'
while 1:
    pool = ""
    password = ""
    count = inputNum("How long do you want your key to be? ", downLim=1)
    if inputBool("Do you want lowercase letters to be used? "):
        pool += Lletters
    if inputBool("Do you want uppercase letters to be used? "):
        pool += Uletters
    if inputBool("Do you want numbers to be used? "):
        pool += number
    if inputBool("Do you want symbols to be used? "):
        pool += symbols
    if pool == '':
        print("You should at least have one answer! Try again!")
        continue
    for _ in range(0, count):
        password += pool[randint(0, len(pool)-1)]
    print(f"********\nYour password is:\n{password}\n********")
    if inputBool("Do you want to exit?", "exit"):
        break
