# # # ## problems on the continue
# # # #Write a while loop that prints numbers from 1 to 10, but skips 5 using continue.

# # # i=1
# # # while i<=10:
    
# # #     if i==5:
# # #         i+=1
# # #         continue
# # #     print(i)
# # #     i+=1


# # # ## 2
# # # # ## Write a program that prints numbers from 1 to 20, but skips all even numbers using continue.    

# # # i=1
# # # while i<=20:
# # #    if i%2==0:
# # #     i+=1
# # #     continue
# # #    print(i)
# # #    i+=1 


# # ## 3
# # # Write a while loop that prints numbers from 10 to 1, but skips 7 using continue.
# # i=10
# # while i<0:
# #     if i==7:
# #       i-=1
# #       continue 
# #     print(i)
# #     i-=1


# ## 4
# # Use a while loop and continue to print only positive numbers.
# nums = [3, -1, 4, -2, 0, 6]
# i = 0

# while i < len(nums):
#     if nums[i] <= 0:
#         i += 1
#         continue
#     print(nums[i])
#     i += 1


# ## 5
# ## Write a while loop that prints numbers from 1 to 15, but skips multiples of 4 using continue.
# i=1
# while i<=15:
#     if i%4==0:
#         i+=1
#         continue
#     print(i)
#     i+=1



# ## 6
# # Write a program that prints all numbers from 1 to 10 except those divisible by 3 using continue.
# i=1
# while i<=10:
#     if i%3==0:
#         i+=1
#         continue
#     print(i)
#     i+=1


# 7
##Use a while loop and continue to print all characters except spaces.
text="i am a good girl"
i=0
while  i<len(text):
    if text[i]==" ":
        i+=1
        continue
    print(text[i])
    i+=1
       
