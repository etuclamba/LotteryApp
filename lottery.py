import random


def lottery_number():
# Generate a random lottery number
    name = input("Enter user's name: ")
    lottery_number = int(input("Enter lottery number: "))
    rand = random.sample(range(0,50), k=1)
    winning_number = 30
    if (lottery_number == winning_number):
        print("congratulation,", name, "your lottery number is", winning_number, "you won!")
    else:
        print("sorry,", name, "your lottery number is", lottery_number, "you failed!")
    if (lottery_number > 50):
        print("the lottery number must be within the range of 0-50")     
    if (lottery_number < 0):
        print("the lottery number must be within the range of 0-50")
        

        


lottery_number()