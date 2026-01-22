## aruments in the decorated functions
##  Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:


def function(func):
    def inner(name):
        result=func(name)
        return result.upper() 
    return inner


@function
def good(name):
    return "hello"+name
 
print(good("navya"))
        
        