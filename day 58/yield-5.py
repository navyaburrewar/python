##  using the yield

def function():
    yield "navya"
    yield "choti"
    yield "neha"

name=function()
print(next(name))
print(next(name))    
print(next(name))   