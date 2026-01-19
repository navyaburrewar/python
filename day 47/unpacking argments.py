##  Unpacking Arguments

#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
# If you have values stored in a list, you can use * to unpack them into individual arguments:


def my_func(a,b,c):
    return a+b+c

numbers =[1,2,3]
result = my_func(*numbers)
print(result)