def func1():
    x = 1    # here x is in the enclosed scope

    def func2():
        print(x)
    func2()

func1()