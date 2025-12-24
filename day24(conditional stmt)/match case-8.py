## match-case

#Similar to switch-case in other languages
#  Used for fixed value matching

# syntax
# #match variable:
#     case value1:
#         statements
#     case value2:
#         statements
#     case _:
#         statements   # default case



## ex-1
# day=int(input())

# match day :
#    case 1:
#       print("monday")
#    case 2:
#       print("tuesday")
#    case 3:
#       print("wednesday")      
#    case 4:
#       print("thurday")
#    case 5:
#       print("friday")
#    case 6:
#       print("saturday")
#    case 7:
#       print("sunday")      



# ## simple calculator
a=10
b=30
op ="*"

match op:
   case "+":
      print(a+b)
   case "-":
      print(a-b)
   case "*":
      print(a*b)
   case "%":
      print(a%b)
   case "/":
      print(a/b)     
# match 1:
#     case 1:
#         print("Match works")
