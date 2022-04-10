from validInput import inputNum, inputBool
logo = """
   _____                                  _____  _         _                 
  / ____|                                / ____|(_)       | |                
 | |      __ _   ___  ___   __ _  _ __  | (___   _  _ __  | |__    ___  _ __ 
 | |     / _` | / _ \/ __| / _` || '__|  \___ \ | || '_ \ | '_ \  / _ \| '__|
 | |____| (_| ||  __/\__ \| (_| || |     ____) || || |_) || | | ||  __/| |   
  \_____|\__,_| \___||___/ \__,_||_|    |_____/ |_|| .__/ |_| |_| \___||_|   
                                                   | |                       
                                                   |_|                       
"""
dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dic += dic


def encrypt(msg: str, offset: int, decrypt=False):
    new: str = ""
    do = -1 if decrypt == True else 1
    offset = int(offset % (len(dic)/2-1))
    for i in msg.lower():
        if i in dic:
            new += dic[dic.index(i) + offset*do]
        else:
            new += i
    return new


print(logo)
while 1:
    msg = input("Enter the text... ").strip()
    offset = inputNum("Enter the offset... ", downLim=1,
                      upLim=int(len(dic)/2-2))
    decrypt = inputBool("What you want to do?", "decrypt", "encrypt")
    print(f"result: {encrypt(msg, offset, decrypt)}")
    if not inputBool("Do you want to continue?", falseMsg="Exit"):
        break
