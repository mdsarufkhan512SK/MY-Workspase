import random 
Ludu = True

while Ludu:
    print(random.randint(1,6))
    Playagain = input("You want play again [y/n]:")
    if Playagain == "y":
        continue
    else:
        print("Game over..!")
        break
