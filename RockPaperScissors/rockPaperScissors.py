import random
choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)

player_score = 0
computer_score = 0

print("Computer choice is :", computer_choice)

while True:
    player_choice = input("Please choose any in Rock,Paper,Scissors: ")
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("Player : ", player_choice, "beat ",
                  "Computer : ", computer_choice)
            player_score += 1
        else:
            print("Computer :", computer_choice,
                  "beat ", "Player :", player_choice)
            computer_score += 1

    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("Computer :", computer_choice,
                  "beat ", "Player :", player_choice)
            computer_score += 1
        else:
            print("Player : ", player_choice, "beat ",
                  "Computer : ", computer_choice)
            player_score += 1

    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("Player : ", player_choice, "beat ",
                  "Computer : ", computer_choice)
            player_score += 1
        else:
            print("Computer :", computer_choice,
                  "beat ", "Player :", player_choice)
            computer_score += 1

    elif player_choice == "End":
        print("Final Score: ")
        print(f"Computer_score: {computer_score}")
        print(f"Player_score: {player_score}")
        break
