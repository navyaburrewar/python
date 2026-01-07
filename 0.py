# list=[2,3,6,6,5,]
# b=set(list)

# print(b[-2])


nums =list(map(int,input("enter numbers: " ).split()))
runnerup =list(set(nums))
runnerup.sort()
if len(runnerup)<2:
    print("no second large")
else:
    print("second largest number",runnerup[-2])    

