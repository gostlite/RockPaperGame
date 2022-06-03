import random



game = ["R", "P", "S"]
gameStart = True
while gameStart:
    player_choice = input("Enter a choice (R for rock, p for paper, s for scissors): ").upper()
    computer_choice = random.choice(game)
    print(f"\nYou chose {player_choice}, computer chose {computer_choice}.\n")

    if player_choice in game:
        if player_choice == computer_choice:
            print(f"Both players selected {player_choice}. It's a tie!")
        elif player_choice == "R":
            if computer_choice == "S":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif player_choice == "P":
            if computer_choice == "R":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif player_choice == "S":
            if computer_choice == "P":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
    else:
        print("Wrong selection, make sure you type R, S, P. Try again")


