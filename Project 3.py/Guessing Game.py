import random
randomnumber = random.randrange(1,100)
userinput = int(input("Guessing the number:"))

if userinput < randomnumber:
    print(randomnumber)
    print("That number is too high")
elif userinput > randomnumber:
    print(randomnumber)
    print("That number is too low")

else:
    print(randomnumber)
    print("You guess the correct number ")