import random

comp_num = random.randint(0,100)
count = 0
while(True):
    user_num = int(input("What is your number"))
    count = count+1
    if comp_num > user_num:
        print("Bigger")