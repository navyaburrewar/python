# # # boolean

# # #1
# # print(5>2)
# # print(4==4)
# # print(5>=0)
# # print(0>9)
# # print(6==1)



# # ## 2
# # bool(0)           ## python consider the 0 as the empty hence false


# # ## 3
# # print(4>0 & 4>1)      # t & t       ### & hs higher precedence then the ">" comparision
# # print(4>0 & 3>0)      # t & f       ### here logic is that  
# # print(2<0 & 4>0)      #  f & t      ### first step (4>0 & 4>1)
# # print(2<0 & 3<0)       #  f & f      0 & 4 ==0  , 4>0 =T,0>1=f  ,T&F =F

# # ## all outputs are false

# # ### 4
# # print(4>0 | 4>1)      # t & t       ### & hs higher precedence then the ">" comparision
# # print(4>0 | 3>0)      # t & f       ### here logic is that  
# # print(2<0 | 4>0)      #  f & t      ### first step (4>0 & 4>1)
# # print(2<0 | 3<0)       #  f & f      0 & 4 ==0  , 4>0 =T,0>1=f  ,T&F =F

# #   ## 5
# #   ## converting values to the boolean
# #   ## 10. " ","python"
# # print(bool(10) )
# # print(bool(""))
# # print(bool("python"))
# # print(bool("python"))

# # ## 6
# # print(7==7)

# # ## 7
# # print(4!=4)


# ## 8
# print(bool([]))  ## empty list which is false here


# ### 9
# print(3<=3)

# ## 10
# print(not(4 ==4)) ### first inside the brackets 4==4 =T
#                   ## !T ==f

# ## 11
# ##Boolean expression to check if a number is between 10 and 20.
# num =int(input())
# print(bool(10 <=num<=20))



## 12
print(bool("0"))
## non empty string hence true

## 13
#print(true or false and false)
print(20>3 |  30<0 & 20>30)
# > and < are comparison operators
# & and | are bitwise operators, not logical operators (and, or)
# Operator precedence (high to low):
# Comparison (>, <)
# Bitwise AND (&)
# Bitwise OR (|)

##comparison > bitwise > logical.