## Lambda with filter()
# filter() selects items based on condition.
num= [1,2,4,56,7,8,0]
even =list(filter(lambda x:x%2==0,num))
print(even)