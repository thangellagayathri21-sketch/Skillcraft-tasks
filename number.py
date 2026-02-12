import random
number = random.randint(1,2)
guessing_Number = int(input("Enter Your Guess: "))
if number == guessing_Number:
    print("You Won the game")
else:
    print("You loss the game")