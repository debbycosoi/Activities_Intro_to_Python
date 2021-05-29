import random

def game ():
    play = int(input("Choose a number from 1 to 3 so that Rock=1, Paper=2, Scissors=3:"))
    print (f"You played {play}")
    contra = random.randrange(1,4)
    print(f"Computer played {contra}")
    if (play == contra):
        print("Tie")
    elif (play == 1 and contra == 2):
        print("You Win!")
    elif (play == 1 and contra == 3):
        print("You Lose!")
    elif (play == 2 and contra == 1):
        print("You Win!")
    elif (play == 2 and contra == 3):
        print("You Lose!")
    elif (play == 3 and contra == 2):
        print("You Win!")
    elif (play == 3 and contra == 1):
        print("You Lose!")


game()