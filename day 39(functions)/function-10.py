### some problems using default parameters
 

## default   two numbers 
def add(a,b=4):
    print(a,b)
add(3,9)
add(5)
add(7)       ## default parameter must come last


## using multiple default parameter

def information(name="navya",age=20):
    print(name,age)
information()
information("choti")
information("neha",50)    