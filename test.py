# test


number = 1
while True:
    user_input = int(input("Type a number: "))
    if user_input == number:
        print("Correct.")
        break
    elif user_input != number:
        print("Incorrect. Try again.")
