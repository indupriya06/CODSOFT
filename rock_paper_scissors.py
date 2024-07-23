import random
options=("rock","paper","scissors")
running=True
while running:
    player=None
    computer=random.choice(options)

    while player not in options:
        player=input("Enter a choice(rock,paper,scissors):")

    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player==computer:
        print("It's a tie!")
    elif player=="rock":
        if computer=="scissors":
            print("You win!",player, "smashes",computer)
        else:
            print("You lose!",computer, "covers",player)
    elif player=="paper":
        if computer=="rock":
            print("You win! ",player,"covers ",computer)
        else:
            print ("You lose!",computer, "cuts",player)
    elif player=="scissors":
        if computer=="paper":
            print("You win!",player, "cuts", computer)
        else:
            print("You lose!",computer, "smashes",player)      
    else:
        print("You lose!")
    if not input("Play again?(y/n):").lower()=="y":
        running=False
print("Thanks for playing!")
    
    
