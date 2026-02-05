def count_1(m):
    count=1
    while count <=m:
        yield count
        count+=1
    return count

for num in count_1(3):
    print(num)