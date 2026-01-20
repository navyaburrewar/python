## non local kryword
## The nonlocal keyword is used to work with variables inside nested functions.
##The nonlocal keyword makes the variable belong to the outer function.

def func1():
    x="navya"
    def func2():
        nonlocal x
        x="choti"
    func2()
    return x 
print(func1())
       