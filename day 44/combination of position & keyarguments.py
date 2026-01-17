## combination of key and position arguments

## You can combine both argument types in the same function.
#Arguments before / are positional-only, and arguments after * are keyword-only:

def func(a,b,/,*,c,d):
    return a+b+c+d

result = func(5,6,c=8,d=9)
print(result)