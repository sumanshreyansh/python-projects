# The task is to create a "Health Management System." Suppose you are a fitness trainer and nutritionist. You have to deal with three clients, i.e., (Harry, Rohan, Hammad). For each client, you have to design their exercise and diet plan.

# Instructions:
# Create a food log file for each client
# Create an exercise log file for each client.
# Ask the user whether they want to log or retrieve client data.
# Write a function that takes the user input of the client's name. After the client's name is entered, it will display a message as "What you want to log- Diet or Exercise".
# Use function

# def getdate():
#            import datetime
#            return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()
aq = int(input("press 1 for harry press 2 for rohan press 3 for hammad\n"))
bq = int(input("press 1 for exercise press 2 for food log\n"))
cq = int(input("press 1 to add data press 2 to retrieve data\n"))

if (aq == 1 and bq == 1 and cq == 1) :
    data = input("type here\n")
    f = open("harry-exe.txt","a")
    f.write(str([str(gettime())])+": "+data+"\n")
    f.close()
    print("sucessfully written")
elif (aq == 2 and bq ==1 and cq == 1):
    data = input("type here\n")
    f = open("rohan-exe.txt","a")
    f.write(str([str(gettime())])+": "+data+"\n")
    f.close()
    print("sucessfully written")
elif (aq == 3 and bq == 1 and cq == 1):
    data = input("type here\n")
    f = open("hammad-exe.txt","a")
    f.write(str([str(gettime())])+": "+data+"\n")
    f.close()
    print("sucessfully written")
elif (aq == 1 and bq == 2 and cq == 1):
    data = input("type here\n")
    f = open("harry-food.txt","a")
    f.write(str([str(gettime())])+": "+data+"\n")
    f.close()
    print("sucessfully written")
elif (aq == 2 and bq == 2 and cq == 1):
    data = input("type here\n")
    f = open("rohan-food.txt","a")
    f.write(str([str(gettime())])+": "+data+"\n")
    f.close()
    print("sucessfully written")
elif (aq == 3 and bq == 2 and cq == 1):
    data = input("type here\n")
    f = open("hammad-food.txt","a")
    f.write(str([str(gettime())])+": "+data+"\n")
    f.close()
    print("sucessfully written")
elif (aq == 1 and bq  == 1 and cq == 2):
    with open("harry-exe.txt") as f:
                for i in f:
                    print(i,end="")
elif (aq == 2 and bq  == 1 and cq == 2):
    with open("rohan-exe.txt") as f:
                for i in f:
                    print(i,end="")
elif (aq == 3 and bq  == 1 and cq == 2):
    with open("hammad-exe.txt") as f:
                for i in f:
                    print(i,end="")
elif (aq == 3 and bq  == 1 and cq == 2):
    with open("rohan-exe.txt") as f:
                for i in f:
                    print(i,end="")
elif (aq == 1 and bq  == 2 and cq == 2):
    with open("harry-food.txt") as f:
                for i in f:
                    print(i,end="")
elif  (aq == 2 and bq  == 2 and cq == 2):
    with open("rohan-food.txt") as f:
                for i in f:
                    print(i,end="")
elif  (aq == 3 and bq  == 2 and cq == 2):
    with open("harry-food.txt") as f:
                for i in f:
                    print(i,end="")
else:
    print("you made mistake try again")