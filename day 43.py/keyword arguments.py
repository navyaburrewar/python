## keyword only argument

#  To specify that a function can have only keyword arguments, add *, before the arguments:

def my_func(*,name):
    print("hello",name)
my_func(name="navya")   

## the about is an keyword only aruments
# there we are giving  key and value



#Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:

def my_func(name):
    print("hi",name)
my_func("navya")     ## this also gives output same as the about

### so becuse  we are not giving the * it is  also taking the positional arguments


# def my_func(*,name):
#     print(name)

# my_func("navya")    


  # the about codes gives error because that we are given * and we are giving the positional arguments hence it will give the the error
  