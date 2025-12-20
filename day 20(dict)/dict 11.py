# ##challenge -1
# #1.
# # Create a dictionary with 5 country names as keys and their capitals as values.

# countries ={
#     "india ": "delhi",
#     "pakistan":"islamabad",
#     "bangladesh":"dhaka"
# }
# print(countries)


# ## 2
# capitals = {
#     "india": "New Delhi",
#     "usa": "Washington, D.C.",
#     "france": "Paris",
#     "japan": "Tokyo",
#     "germany": "Berlin"
# }

# country = input("Enter a country name: ").lower()   ## .lower helps in match keys correctly

# if country in capitals:
#     print("Capital:", capitals[country])
# else:
#     print("Sorry, capital not found.")



##3
# Change the price of an item in a dictionary.

prices ={
    "tomato" :10,
    "potato":20,        
    "mango":40
}
prices.update({"tomato" : 100})
print(prices) 


## 4
## Add a new subject and marks to a student dictionary.
prices ={
    "tomato" :10,
    "potato":20,        
    "mango":40
}
prices["apple"]=60
print(prices)


## differace between adding and updating adding in which new key and value pair
## updating which is updating values to keys


## 5
## delet a key
students ={
    "name" : "navya",
    "age":20,
    "class":3
}
del students["age"]
print(students)
