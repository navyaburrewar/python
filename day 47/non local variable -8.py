##

def func1():
    x="burrewar"
    def func2():
        nonlocal x
        x="choti"
    func2()
    return(x)
print(func1())    