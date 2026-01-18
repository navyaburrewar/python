## combination of  *args and **kwargs

# You can use both *args and **kwargs in the same function.

# The order must be:

# regular parameters
# *args
# **kwargs

def func(*args,**kwargs):
    print("positional arguments" , args)
    print("keyword arguments",kwargs)
func("navya","choti","neha",age=20,rank=1)    