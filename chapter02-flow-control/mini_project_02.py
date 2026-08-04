#Number Guessing Game

secret_number = 14
attempts = 0

print("Welcome to the Number Guessing Game!!")
print("I am thinking of a number between 1 to 20.")

while True: #using True because we want to keep asking the user to guess
    num = int(input("Guess the Number: "))
    attempts += 1
    if num == secret_number:
        print("You guessed it correctly!!!")
        if attempts == 1:
            print("You guessed it in", attempts, "attempt!!")
        else:
            print("You guessed it in", attempts, "attempts!!")
        break #runs and stops the loop when the user guesses the correct answer so the loop eventually ends
    elif num == 13 or num == 15:
        print("Closeeee")
    elif num > secret_number:
        print("Too High")
    else:
        print("Too low")