## naming variables


##  If you operate with the same variable name inside and outside of a
## function, Python will treat them as two separate variables, one available in
## the global scope (outside the function) and one available in the local scope (inside the function):


x=3
def my_func():
    x=4
    print(x)
my_func()
print(x)    



#ex-2
z=100
def func():
    x=200
    print(x)
func()
print(z)    





