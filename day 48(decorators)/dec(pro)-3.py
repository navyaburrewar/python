def function(func):
    def inner():
        return func().lower()
    return inner

def my_function():
    return "HELLO WORLD"

my_function = function(my_function)
print(my_function())
