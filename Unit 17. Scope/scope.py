#global scope variable
x = 5
#local scope variable
def func():
    x = 10
    print(x)
func()

#enclosing scope variable
def func():
    x = 10
    def func2():
        x = 20
        print(x)
    func2()
func()


def first():
    color = "olive green"

    def second():
        print(color)

    second()


first()
color = "purple"


def my_func():
    global color
    color = "green"


print(color)
my_func()
print(color)
