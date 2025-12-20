## removing elements


## 1 pop(key) = removing specific key
## 2popitem() =remove last item
## 3 del =deletes key
## 4 clear() =remove all items


## 1
## pop()
results={
    "nandhu":"good",                
    "bindhu":"bad",        
    "neha":"not bad",
    "akhi": "worst",
    "navya": "best"

}
results.pop("nandhu")    ### removes by index
print(results)
results.popitem()        ## removing last element
print(results)
results.clear()           ## removes all element
print(results)


## del -remove by index or slice 
num=[11,2,22,33,44,55]
del num[3]
print(num)



