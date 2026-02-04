## normal function vs generator


# normal function

def numbers():
    return (1,7,9)
print(numbers())
 

 ## output ==1,7,9

def number():
    yield 1
    yield 2
    yield 3

print(number())    
for num in number():
    print(num) 


# 🎬 Generator = TV Series
# 🎮 for loop = Remote control
# ▶ next() = Pressing “Next Episode

