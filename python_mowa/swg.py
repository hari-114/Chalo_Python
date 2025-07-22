import random
computer = random.choice([2, 0, 1]) 
youstr = input("enter ur choice (s for snake, w for water, g for gun): ")

youDict = {"s": 1, "w": 2, "g": 0}  
reverseDict = {1: "snake", 2: "water", 0: "gun"}

# Validate user input
if youstr not in youDict:
    print("Invalid input")
else:
    you = youDict[youstr]
    print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

    if computer == you:
        print("draw")
    else:
        if ((computer - you) == -1 or (computer - you) == 2):
            print("you lose")
        else:
            print("you win")