## using yield function

def count_1(n):
    count =1
    while count <=n:
        yield count
        count+=1

for num in count_1(10):
    print(num)        