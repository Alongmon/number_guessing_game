# number guessing game

import random
# loops the entire game

while True:
    print("Guess The Number")
    while True:
        try:
            # used for setting up the range for the final number
            lower_limit = int(input("Lower limit: "))
            upper_limit = int(input("Upper limit: "))
            break
        except ValueError:
            print("Please type a number")

    secret_number = random.randrange(lower_limit, upper_limit)
    request = "ans?"

    while True:
        guess = input(f"Guess a number between {lower_limit} and {upper_limit}: ")

        # used for checking whether the number is a string or a digit (the .isdigit returns a boolean value)
        parameter = guess.isdigit()

        # this exception part is the whole game
        if parameter is True:
            guess = int(guess)
            if guess != secret_number and request:
                print("That was incorrect try again.")
            elif guess == secret_number:
                print(f"Correct! The answer is {secret_number}")
                break

        elif guess == request:
            print(f"The correct answer is {secret_number}")
            break

    # prompting the user if they want to continue playing the game or end
    while True:
        end_input = input("Would you like to play again? (y/n): ")
        if end_input == "n":
            print("Thank you for playing.")
            break
        elif end_input == "y":
            break
        elif end_input != "y" or "n":
            print("Please press either \"y\" for yes or \"n\" for no.")

    # to break the while loop
    if end_input == "n":
        break
