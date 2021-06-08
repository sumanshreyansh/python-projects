#You have to build a "Number Guessing Game," in which a winning number is set to some integer value. The Program should take input from the user, and if the entered number is less than the winning number, a message should display that the number is smaller and vice versa.
#Instructions:
#1. You are free to use anything we've studied till now.
#2. The number of guesses should be limited, i.e (5 or 9).
#3. Print the number of guesses left.
#4. Print the number of guesses he took to win the game.
#5. “Game Over” message should display if the number of guesses becomes equal to 0.


secret_no = 21
strtn_no = 1
end_no = 9
while strtn_no<=end_no:
    qw = int(input("guess the number:\n "))
    strtn_no+=1
    zx = end_no-1
    cv = strtn_no
    if qw == secret_no:
        print("congratulation you guessed it correct")
        print(f"you guessed correctly in {cv} attempt")
        break
    elif(qw > secret_no):
        print("the number is large")
        print(f"chances left {zx}" )
        continue
    elif(qw < secret_no):
        print("the number is smaller")
        print(f"chances left {zx}" )
        continue
else:
    print("guess limit is reached \ngame over")  