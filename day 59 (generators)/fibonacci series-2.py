def function(m):
    a=0
    b=1
    count=0
    while count < m:
        yield a
        a,b=b,a+b
        count+=1


for num in function(10):
    print(num)        


    