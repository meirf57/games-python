from random import randint

options = ["Rock", "Paper","Scissors"]

player = input("Rock / Paper / Scissors? ").capitalize()

computer = options[randint(0,2)]

if player in options:
    if computer == player:
        game = "Tie"
    elif computer == options[0]:
        if player == options[1]:
            game = "WIN!"
        else:
            game = "Lost"
    elif computer == options[1]:
        if player == options[2]:
            game = "WIN!"
        else:
            game = "Lost"
    else:
        if player == options[0]:
            game = "WIN!"
        else:
            game = "Lost"
    print(f"{game}\nP - {player} / C - {computer}")
else:
    print(f"Please check spelling. (your input: {player.casefold()})")


