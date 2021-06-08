# fibonacci series
number = int(input("enter the number "))
def fibonacc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacc(n-1) + fibonacc(n-2)
print("the fibonacci number is",fibonacc(number))
    