import random
lst1=[0, 45, 76, 98, 123, 458, 89, 287, 1004, 22]
x=random.choice(lst1)

print("Judges have picked a number from the list:", lst1)

y = int(input("Please guess the number: "))
if y>x:
    print("The number you guessed is too high. Sorry, you lost!")
    print("The number was", random.choice(lst1))
elif y<x:
    print("The number you picked is too low. Sorry, you lost!")
    print("The number was", random.choice(lst1))
else:
    print("Great Job! You guessed the number correctly!")