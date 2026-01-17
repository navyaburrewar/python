## arbitrary arguments - *args

## If you do not know how many arguments will be passed into your function, add a * before the parameter name.
##This way, the function will receive a tuple of arguments and can access the items accordingly:


def my_function(*kids):
    print("the youngest child is " + kids[2])
my_function("choti","navya","neha")    



def my_func(*villages):
    print("my village name is " + villages[0])
my_func("bkd","nzb","hyd")   

##What is *args?
#The *args parameter allows a function to accept any number of positional arguments.
#Inside the function, args becomes a tuple containing all the passed arguments: