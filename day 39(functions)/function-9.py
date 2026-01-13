## default parameter

## A default parameter is a parameter that already has a value given to it when the function is created.
#So if the user does not give a value, Python will use the default one.
## “If no value is given, use this value automatically.”



## ex-1
def greet(name="choti"):    ## here choti is the default  value
    print("hello",name)     ## when greer("navya")--> replaces the "choti"

greet()                   ### greet() is calles --> no value given --> choti is used
greet("navya")           



##3 Why do we need default parameters?
# without default parameters

#### code ###

# def greet(name):
#     print("Hello", name)

# greet()   # ❌ Error


## here which gives the error


def greet(name="Guest"):
    print("Hello", name)

greet()   # Works fine


