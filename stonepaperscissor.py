
import random

strtn_no = 1
end_no = 10
while strtn_no<=end_no:
    a = input(" press s for stone\n press p for paper\n press k for scissor\n your input: ")
    strtn_no+=1
    mylist = ["s","p","k"]
    q = random.choice(mylist)
    if q == "s" and a == "p":
        print("YOU WIN !")
        continue
    elif q == "p" and a == "s":
        print("YOU LOSE !")
        continue
    elif q == "p" and a == "k":
        print("YOU WIN !")
        continue
    elif q == "k" and a == "p":
        print("YOU LOSE !")
        continue
    elif q == "s" and a == "k":
        print("YOU LOSE !")
        continue
    elif q == "k" and a == "s":
        print("YOU WON !")
        continue
    elif q == "s" and a == "s":
        print("try again")
        continue
    elif q == "p" and a == "p":
        print("try again")
        continue
    elif q == "k" and a == "k":
        print("try again")
        continue
else:
    print("try again")     