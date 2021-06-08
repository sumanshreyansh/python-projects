#faulty calculator
#45*3=124 79+24=46 21-5=02 45/6=4

frst = int(input("enter first number\n"))
scnd = int(input("enter the second number\n"))
print("press-\n 1 for add\n 2 for sub\n 3 for mul\n 4 for div ")
oprtn = int(input("choose the operation\n"))
if (frst == 45 and scnd == 3 and oprtn == 3 ):
    print("124")
elif(frst == 79 and scnd == 24 and oprtn == 1 ):
    print("46")
elif(frst == 21 and scnd == 5 and oprtn == 2):
    print("02")
elif(frst == 49 and scnd == 6 and oprtn == 4):
    print("4")
elif oprtn == 1:
    print(frst + scnd)
elif oprtn == 2:
    print(frst - scnd)
elif oprtn == 3:
    print(frst * scnd)
elif oprtn == 4:
    print(frst / scnd)
else:
    print("thank you")
