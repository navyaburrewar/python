## function inside the function that 

def func():
    x=20
    def my_func():
        y=90
        print(y)
    my_func()  
    print(x)
func()      