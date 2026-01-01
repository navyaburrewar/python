# ##  Print a square of stars (size 4×4).


# for i in range(5):
#    print("*"*4)


# ## 2
# ## another way of the  printing the stars
# for i in range(5):
#  for j in range(5): 
#      print("*", end="") 
#  print()


### 3
## Rectangle pattern (3 rows, 6 columns)
for i in range(3):
   for j in range(6):
      print("*",end="")
   print()



### 4
#   Right-angled triangle (5 rows)
for i in range(6):
   print("*"*i)


   ## another way
##    Using i and j (nested loops)
for i in range(6):
   for j in range(i+1):
      print("*",end="")
   print()  
   

    