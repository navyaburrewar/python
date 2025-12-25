# ## break 
# #if you can always write a perfect stopping condition, then break is NOT necessary.

# # But in real programs, we often cannot predict everything in advance.
# # That’s exactly why break exists

# #Case 1: When condition is known (NO break needed)

# # i=1
# # while i<5:
# #     print(i)
# #     i+=1

#     #We know exactly when to stop → no break needed.




# # Case 2: When stop condition happens during execution (break needed)

# # while True:
# #     password= input("enter password ")
# #     if password =="123":
# #         print("access granted")
# #         break
# #     print("wrong password")

# #it will break after you enterd the correct ans




# ## Case 3: Searching something/element
# ## it breakes after only  you found correct ans
# ## in this situation you dont know can you will found correct ans
# ## break is used
# num =[1,3,5,8,6]
# i=0
# while i<len(num):
#     if num[i]==10:
#         print("found")
#         break
#     i=i+1          #output :nothing will be printed





# num =[1,3,5,8,6]
# i=0
# while i<len(num):
#     if num[i]==5:
#         print("found")
#         break
#     i=i+1    # which will saves the time  if ans found it will be break





# ## continue statment in while loop
# ##continue skips the current iteration and moves to the next one.

# i=0
# while i<10:
#     i=i+1
#     if  i==5:
#       continue      # it will skip 5
#     print(i)




    ## ex-2
# i=5
# while i<20 :
#       i=i+1
#       if i==15 :
#            continue
#       print(i)





##  removing more than one element in .....

i=0
while i<10:
    if i==3:
        i=i+3
        continue
    print(i)
    i=i+1


  