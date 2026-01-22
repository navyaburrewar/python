def function(func):
    def inner(name):
        result = func(name)
        return result.upper()
    return inner

@function
def my_function(name):
    return "hello"+name
print(my_function("neha"))





  
        