def function(m):
    for i in range(m):
        yield i

    gen =function(20)
    print(next(gen))
    print(next(gen))
    print(next(gen))    



# def large_sequence(n):
#   for i in range(n):
#     yield i

# # This doesn't create a million numbers in memory
# gen = large_sequence(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))