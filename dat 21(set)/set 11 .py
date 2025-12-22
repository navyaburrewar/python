## enumerate()
#With enumerate(), Python adds a counter automatically:


## without enumerate
fruits = {'apple', 'banana', 'cherry'}
for fruit in fruits:
    print(fruit)                    ## no indexing here

## with enumarete
fruits = {'apple', 'banana', 'cherry'}
for fruit in enumerate( fruits):
    print(fruit)                  ## index is added in the 
    
    #Use enumerate() whenever you need both the index and value in a loop
    #Works with lists, tuples, strings, sets