#to make a program which keeps adding number till the user doesn't press q.
sum = 0
while(True):
    a = input("Enter the price \n")
    if a != "q":
        sum = sum + int(a)
        print(f"order so far {sum}")
        
    else:
        print("The total price is ",sum)
        break