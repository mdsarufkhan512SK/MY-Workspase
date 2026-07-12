Answer = input("Are you want to play this game ? [Yes/No]")
if Answer == "Yes":
    print("welcome to the game..!")
    Answer = input("Where you want to go..?[Forst/Cave]")
    if Answer == "Forst":
        print("You can see a Tiger And The Tiger killed you.. You loss the game")
    else:
        print("You can see a bear in font of the cave")
    Answer = input("What do you want at this moment [Fight/Run]")
    if Answer == "Fight":
        print("The bear is so strong.")
        print('The bear killed you and you loss the game!')
    else:
        print("You run...!")
        print("You win the game")
else:
    print("The game is closed..!")