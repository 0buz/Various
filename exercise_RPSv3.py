from random import randint


def rockPaperScissors(x, y):
    goes = [x, y]
    if ("r" in goes) & ("p" in goes):
        return "Player " + str(goes.index("p") + 1) + " wins!"
    elif ("r" in goes) & ("s" in goes):
        return "Player " + str(goes.index("r") + 1) + " wins!"
    elif ("p" in goes) & ("s" in goes):
        return "Player " + str(goes.index("s") + 1) + " wins!"
    elif x == y:
        return "It's a tie"
    else:
        return "Invalid input! You must enter 'r', 'p' or 's'."


def mapping(player):
    if player == 0:
        return 'r'
    elif player == 1:
        return 'p'
    else:
        return 's'


player1 = input("Player 1, go! ")
go = randint(0, 2)
computer = mapping(go)

print(rockPaperScissors(player1, computer))
print("Computer chose " + computer + ".")

while True:
    rest = input("Would you like to play again? y/n \n")
    if rest == "y":
        player1 = input("Player 1, go! ")
        go = randint(0, 2)
        computer = mapping(go)
        print(rockPaperScissors(player1, computer))
        print("Computer chose " + computer + ".")
    elif rest == "n":
        print("Game Over.")
        break
    else:
        print("Valid options are 'y', 'n'.")
