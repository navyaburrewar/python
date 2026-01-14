## You can send arguments with the key = value syntax.
def my_function(name,age):
    print("my name is",name +"  and age is", age )

my_function(name="navya",age="21")    

## here name and age are key arguments





###   positional arguments

#When you call a function with arguments without using keywords, they are called positional arguments.
#Positional arguments must be in the correct order:


def my_func(name, age):
    print(name,age) 
my_func("navya" , 21)    
my_func(21,"navya")
