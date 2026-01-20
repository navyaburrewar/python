## global keyword

## If you need to create a global variable, but are stuck in the local scope, you can use the global keyword

## The global keyword makes the variable global.


def func():
    global x
    x=100
    print(x)

func() 


##ex-2   ## here we converting local to global
x=100
def func():
    global x
    x=200
func()    
print(x)    