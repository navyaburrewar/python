###  A function that calculates the sum of any number of values:
def func(*nums):
    total=0
    for num in nums:
      total+=num
    return total
print(func(23,4,9,2,2))    



def func(*alphabet):
    total=""
    for char in alphabet:
      total+=char
    return total  
print(func("n","a","v","y","a"))
    
