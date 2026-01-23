i="heads"
j="legs"
chiken_count=0
rabbit_count=0


for i in range(36):
    for j in range(95):
     if i==1 and j==2:
      chiken_count+=1
     elif i==1 and j==4:
      rabbit_count+=1

print("vowels",chiken_count)
print("consonats",rabbit_count)       
 