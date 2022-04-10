from random import randint
from validInput import inputNum
from mangeConsole import clearConsole
asciiArt = [
    '',
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
    """
     )                                 
  ( /(                                 
  )\())       (    (  (                
 ((_)\  (    ))\   )\))(    (    (     
__ ((_) )\  /((_) ((_)()\   )\   )\ )  
\ \ / /((_)(_))(  _(()((_) ((_) _(_/(  
 \ V // _ \| || | \ V  V // _ \| ' \)) 
  |_| \___/ \_,_|  \_/\_/ \___/|_||_|  
                                       
""", """
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                                                                  
"""]
user_score = 0
com_score = 0


def user_wins():
    global user_score
    user_score += 1
    print(
        f"You have won this round!\nYou: {user_score} vs Computer: {com_score}")


def com_wins():
    global com_score
    com_score += 1
    print(
        f"You lost this round!\nYou: {user_score} vs Computer: {com_score}")


clearConsole()
count = inputNum("How many rounds do you want to play? ", downLim=2)
clearConsole()
while 1:
    if user_score >= count or com_score >= count:
        break
    user_choice = inputNum(
        "Which one do you choose? Enter\n1 for rock\n2 for paper\n3 for scissors... ", downLim=1, upLim=3)
    com_choice = randint(1, 3)
    clearConsole()
    print(
        f"You chose:\n{asciiArt[user_choice]}\nComputer chose:\n{asciiArt[com_choice]}")
    if user_choice == 3 and com_choice == 1:
        com_wins()
    elif user_choice == 1 and com_choice == 3:
        user_wins()
    elif user_choice > com_choice:
        user_wins()
    elif user_choice < com_choice:
        com_wins()
    else:
        print(
            f"Draw!\nYou: {user_score} vs Computer: {com_score}")

if user_score > com_score:
    print(
        f"{asciiArt[4]}\nCongradulations!!!\nYou: {user_score} vs Computer: {com_score}")
else:
    print(
        f"{asciiArt[5]}\nYou lost!!!\nYou: {user_score} vs Computer: {com_score}")
