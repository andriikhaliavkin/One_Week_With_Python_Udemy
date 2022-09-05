#loop with break and continue
#break - exits the loop
#continue - skips the rest of the loop and goes back to the top

#break
for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("Done with loop")

#continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print("Done with loop")

#nested loops
for i in range(1, 4):
    for letter in ["a", "b", "c"]:
        print(i, letter)

#dice roll
from random import randint
for i in range(10):
    print(randint(1, 6))

#2 dice roll
for i in range(10):
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print(dice1, dice2)

#toothpick game
from random import randint
for i in range(10):
    player = randint(1, 2)
    print("Player", player, "wins!")


