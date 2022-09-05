#join lists example
#create two lists
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
#join the lists
list3 = list1 + list2
print(list3)
#split lists example
#split the list into two lists
list4 = list3[:5]
list5 = list3[5:]
print(list4)
print(list5)
#copy lists example
#copy the list
list6 = list3[:]
print(list6)

#todo list example
#make a list of things to do
todo = ["call mom", "pay bills", "make dentist appt"]
#add an item to the list
todo.append("go to the gym")
#remove an item from the list
todo.remove("pay bills")
#sort the list
todo.sort()
#reverse the list
todo.reverse()
#print the list
print(todo)

colors = ['r', 'g', 'b']
letters = colors
letters.append('z')
print(colors)
print(letters)

