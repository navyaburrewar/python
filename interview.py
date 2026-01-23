# ##Write a program to solve a classic ancient Chinese puzzle: 
# # We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# #  How many rabbits and how many chickens do we have?

# #Hint: Use for loop to iterate all possible solutions.

# # heads=35
# # legs=94
# # ## chiken =1 head + 2 legs
# # ## rabit = 1 head +4 legs
# # rabit=[0]
# # chiken=[0]
# # i="head"
# # j="leg"
# # for i in range(35+1):   ## i = head
# #     for j in range(94+1):   ## j = leg
# #         if i==1 & j==2:
# #             chiken = chiken+1
# #             print(count(chiken))

# #         elif i==1 & j==4:
# #             rabit= rabit+1
# #             print(count(rabit))
           
# ## Write a python code to accept a string and count the number of vowels and consonants.
# # 
# i = "navya"
# vowels= "a" or "e" or "i"or "o" or "u"

# print("vowels", i.count(vowels))
# print("consonants"i.count())    

#     ##Write a program to find the number of occurrences of elements from list1 to list2



heads = 35
legs = 94

for chickens in range(heads + 1):
    rabbits = heads - chickens
    if 2*chickens + 4*rabbits == legs:
        print("Chickens:", chickens)
        print("Rabbits:", rabbits)

        


                  


