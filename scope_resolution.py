# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# local scope
def func1():
    x = 1
    def func2():
        print(x)
    func2()

# func1()

# global scope
def func3():
    y = 1
    print(y)

def func4():
    y = 2
    print(y)

y = 3

# func3()
# func4()

# built-in
from math import e

def func5():
    print(e)

e = 3

func5()