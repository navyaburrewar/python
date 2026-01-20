## global scope
##A variable created in the main body of the Python code is a global variable and belongs to the global scope.

#Global variables are available from within any scope, global and local.


x=20
def func():
    print(x)
func()

print()



## ex-2
y=7
def func():
    print(y)
func()
print(y)
    