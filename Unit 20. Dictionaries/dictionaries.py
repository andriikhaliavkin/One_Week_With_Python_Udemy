#create dictionary
d = {'name': 'Bob', 'age': 25, 'job': 'dev'}
print(d)
print(d['name'])
print(d['age'])
print(d['job'])
#add new key
d['salary'] = 80000
print(d)
#change value
d['salary'] = 90000
print(d)
#delete key
del d['job']
print(d)
#check if key exists
print('name' in d)
print('job' in d)
#iterate over keys
for key in d:
    print(key, d[key])
#iterate over keys and values
for key, value in d.items():
    print(key, value)
#iterate over values
for value in d.values():
    print(value)
#clear dictionary
d.clear()
print(d)
#delete dictionary
del d
# print(d)

#invalid dictionary key
#d = {[1, 2, 3]: 'list'}

#get dictionary value
d = {'name': 'Bob', 'age': 25, 'job': 'dev'}
print(d.get('name'))
print(d.get('salary'))
print(d.get('salary', 0))

#list and dictionary combination
d = {'name': 'Bob', 'age': 25, 'job': 'dev'}
l = ['name', 'age', 'job']
print(d[l[0]])
print(d[l[1]])
print(d[l[2]])

#dictionary comprehension
d = {x: x**2 for x in range(7)}
print(d)

#dictionary comprehension with if
d = {x: x**2 for x in range(7) if x % 2 == 0}
print(d)

#dictionary comprehension with if else
d = {x: 'even' if x % 2 == 0 else 'odd' for x in range(7)}
print(d)

ski_runs = {"easy": "green", "intermediate": "blue", "advanced": "black"}





