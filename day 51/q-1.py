def function(func):
    def inner():
        return func().upper()
    return inner()


@function
def my_function():
    return "hello world"

print(my_function)