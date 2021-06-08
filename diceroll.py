#roll of a dice
import random
number = int(input("press 1 to roll a dice "))
while(True):
    if number == 1:
        qw = random.randint(1,6)
        print("the random number you get\n ",qw)
        break
    else:
        print("wrong input")
    

