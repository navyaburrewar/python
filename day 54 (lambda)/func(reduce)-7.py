## reduce

from functools import reduce
num=[1,2,3,5,4]
reduce_1=reduce(lambda a,b:a+b,num )
print(reduce_1)