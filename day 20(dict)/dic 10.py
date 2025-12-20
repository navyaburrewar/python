## dictionary comprehension
squares={x :x*x for x in range(1,9)}
print(squares)

squares=[x*x for x in range(1,9)]
print(squares)

print(tuple(squares))
