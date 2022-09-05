#create list
myList = [1, 2, 3, 4, 5]
print(myList)
#add to list
myList.append(6)
print(myList)
#remove from list
myList.remove(6)
print(myList)
#insert into list
myList.insert(0, 0)
print(myList)
#sort list
myList.sort()
print(myList)
#reverse list
myList.reverse()
print(myList)
#count list
print(myList.count(1))
#length of list
print(len(myList))
#access list
print(myList[0])

#create task list
taskList = []
#add tasks
taskList.append("Wash the car")
taskList.append("Clean the house")
taskList.append("Do the dishes")
taskList.append("Mow the lawn")
taskList.append("Take out the trash")
#display tasks
print(taskList)

#convert string hello to a list
helloList = list("Hello")
print(helloList)

#list of a lists
listOfLists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listOfLists)
#loop through list of lists
for i in listOfLists:
    print(i)
    for j in i:
        print(j)

