word = "Saruf"
chances = 10 
addguess = []
done = False

while not done:
    for letter in word:
        if letter.lower() in addguess:
            print(letter,end =" ")
        else:
            print("_",end = " ")

    Myguess = input(f"Your chances is {chances},Guess the number :")
    addguess.append(Myguess.lower())
    if Myguess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in addguess:
            done = False