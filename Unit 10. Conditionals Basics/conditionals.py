import random
# Create a random number between 1 and 10
secret = random.randint(1, 10)
# Ask the user to guess the number
guess = int(input("Guess the secret number between 1 and 10: "))
# Compare the user's guess to our number
if guess == secret:
    print("You guessed it - congratulations! It's number " + str(secret))
else:
    print("Sorry, your guess is not correct... The secret number is not " + str(guess))
print("Game over!")


if_example = 1
if if_example == 1:
    print("if_example is 1")
elif if_example == 2:
    print("if_example is 2")
else:
    print("if_example is not 1 or 2")

