def function():
    yield "navya"
    yield "choti"
    yield "neha"
names =  function() 
print(next(names))  

names.close()



def func():
    for m in range(10):
        yield m
num=func()
print(next(num))
print(next(num))
print(next(num))
num.close()