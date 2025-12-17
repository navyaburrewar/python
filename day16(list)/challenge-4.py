## write a program to flatten aneasted list
## flat which is nothing but convert a list that contain other lists into a single list with all elements at one level


nested =[ [1,2],[3,5],[9,4]]
flat =[]
for sublist in  nested:
    for subelement in sublist:
        flat.append(subelement)
print(flat)   

#### using list comprehension
nested =[[1,2],[5,3],[6,7]]
flat =[ subelement for sublist in nested for subelement in sublist  ]
print(flat)





