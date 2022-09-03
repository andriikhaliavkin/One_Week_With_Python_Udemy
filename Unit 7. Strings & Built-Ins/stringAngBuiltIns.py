
# Function definition
def func_name():
    pass

# Main function
def main():
    pass


help(len)
help(str)
help(str.lower)
help(str.upper)
help(str.title)
help(str.capitalize)
help(str.swapcase)
help(str.casefold)
help(str.islower)
help(str.isupper)

color = "red"
print(len(color))
# print(len(55)) # TypeError: object of type 'int' has no len()

color = input("Enter a color: ")
print(color)

age = "25"
int_age = int(age)
age = int(age)

print(type(age))

age = float(input("Enter your age: "))
print(f'You are {age*365} days old.')
