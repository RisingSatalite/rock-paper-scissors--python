from random import randint
while 1 == 1:
    player = input("rock, paper, scissor")

    com = randint(1, 3)
    if com == 1:
        comp = "rock"
    elif com ==2:
        comp = "paper"
    else:
        comp = "scissors"
    if player == "rock":
        if comp == "rock":
            print("You though rocks can beat rocks, draw")
        elif comp == "paper":
            print("The computer tossed you aside, defeat")
        else:
             print("You crush metal, victory")
    elif player == "paper":
        if comp == "rock":
            print("You tossed the computer aside, victory")
        elif comp == "paper":
            print("You and the computer collasps, draw")
        else:
            print("You got sliced to piece, defeat")
    elif player == "scissor":
        if comp == "rock":
            print("You are pinned, stuck between a rock and a hard place, defeat")
        elif comp == "paper":
            print("With your awsome sword skills, the computer has fallen, victory")
        else:
            print("You and the computer and evenly matched, draw")
    else:
        print("You did not give a proper respond")