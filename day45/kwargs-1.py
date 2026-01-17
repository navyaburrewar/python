## arbitrary keyword arguments -** kwargs

##If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
#This way, the function will receive a dictionary of arguments and can access the items accordingly:


def my_func(**kids):
    print("first name is"+kids["fname"]+" last name is"+kids["flast"])
my_func(fname=" navya",flast=" burrewar")    
