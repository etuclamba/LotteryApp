import random

def yourname_password_gen():
    

#Generate a random lottery number
    name = input("Enter Username: ")
    lottery_number = int(input("Enter lottery number: "))
    rand = random.sample(range(0,50), k=1)
    winning_number = 30

    if lottery_number > 50:
        print("syntax error")
    elif lottery_number == winning_number and lottery_number == rand:
        print("congratulations", name, "your lucky number is", winning_number, "you are the lucky winner")
    else:
        print("sorry", name, "your lottery number is", lottery_number, "you got", rand, "you failed, try again next time")

yourname_password_gen()
