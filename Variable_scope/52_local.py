# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local --> Enclosed --> Global --> Built-in

def func1():  #functions can't see inside of other functions
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()