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

