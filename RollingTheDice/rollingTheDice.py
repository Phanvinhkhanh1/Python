import random

min_val = 1
max_val = 6

rolling_again = "yes"

while rolling_again == "yes" or rolling_again == "y":
    print("Rolling The Dices ...")
    print("Values are : ")

    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))

    rolling_again = input("Do you want to Rolling The Dices again? ")
