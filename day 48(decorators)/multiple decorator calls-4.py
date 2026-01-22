## multiple decorator calls

##   A decorator can be called multiple times. Just place the decorator above the function you want to decorate.

def function(func):
    def inner():
        return func().lower()
    return inner()


@function
def my_function():
    return "nAvya"
print(my_function)


@function
def good():
    return "choti"
print(good)


def bad():
    return "nikki"
bad=function(bad)
print(bad)
