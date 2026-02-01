## closure :
#3 A function that “remembers” values from its surrounding (outer) function, even after the outer function has finished executing.


def myfunc(n):
    return lambda a:a*n

func = myfunc(3)
print(func(11))




def func(m):
    return lambda a:a+m
myfunc=func(6)
print(myfunc(4))