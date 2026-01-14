#Mixing Positional and Keyword Arguments


#You can mix positional and keyword arguments in a function call.
#However, positional arguments must come before keyword arguments:


def my_func(name ,age,area):
    print(name,age,area)
my_func("navya",age=21 ,area="bkd")    
# my_func(name="navya",age=21,bkd)   --> this line gives error beacuse of that  key argumenta are first then positional arguments

