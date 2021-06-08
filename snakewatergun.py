# Water will win from gun , gun will win from snake, snake will win from water.
import random

strtn_no = 1
end_no = 10
while strtn_no<=end_no:
    a = int(input(" press 1 for snake\n press 2 for water\n press 3 for gun\n your input: "))
    mylist = ["s","w","g"]
    q = random.choice(mylist)
    if q == "w" and a == 3:
        print("YOU LOSE !")
        continue
    elif q == "g" and a == 2:
        print("YOU WON !")
        continue
    elif q == "g" and a == 1:
        print("YOU LOSE !")
        continue
    elif q == "s" and a == 3:
        print("YOU WON !")
        continue
    elif q == "s" and a == 2:
        print("YOU LOSE !")
        continue
    elif q == "w" and a == 1:
        print("YOU WON !")
        continue
    elif q == "s" and a == 1:
        print("try again")
        continue
    elif q == "w" and a == 2:
        print("try again")
        continue
    elif q == "g" and a == 3:
        print("try again")
        continue
else:
    print("try again")     