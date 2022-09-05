#function example
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
hello()

#funnction with input
def helloWithInput(name):
    name = input('What is your name? ')
    print('Hello ' + name)
helloWithInput('')

#function with multiple parameters
def helloWithMultipleParameters(name, age):
    print('Hello ' + name + ' you are ' + str(age))
helloWithMultipleParameters('Alice', 25)

#function with return
def helloWithReturn(name):
    return 'Hello ' + name
helloWithReturn('Alice')

#function with return and multiple parameters
def helloWithReturnAndMultipleParameters(name, age):
    return 'Hello ' + name + ' you are ' + str(age)
helloWithReturnAndMultipleParameters('Alice', 25)

#divide function
def divide(dividend, divisor):
    if divisor == 0:
        return
    return dividend / divisor
print(divide(15, 3))
print(divide(15, 0))
print(divide(15, 5))

#is even function
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(isEven(20))
print(isEven(21))

#is odd function
def isOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False
print(isOdd(20))
print(isOdd(21))

#function with default parameter
def helloWithDefaultParameter(name = 'Alice'):
    print('Hello ' + name)
helloWithDefaultParameter()
helloWithDefaultParameter('Bob')






