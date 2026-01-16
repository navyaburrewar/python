## position only the arguments

#You can specify that a function can have ONLY positional arguments.
#To specify positional-only arguments, add , / after the arguments:

def my_func(name,/):
    print("hello",name)
my_func("choti")    

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:


def my_func(name,):
    print("hello",name)
my_func(name="choti")    


## here about it is taking the keyword arguments


# def my_func(name,/):
#     print("hello",name)
# my_func(name="choti")

     ## here we will get error for the about code because /,, are the positional arguments but we are using the keyword argumrnts hence it will give the error
     

