number = int(input("enter any number\n"))
a = number
reverse = 0 

while(number>0):
    b = number%10
    reverse = reverse*10 + b
    number = number//10
if a == reverse:
    print("it's a palindrome")
else:
    print("it's not a palimdrome")