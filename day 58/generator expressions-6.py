## list comprehension vs generator expression


list_comp =[x*x for x in range(10)]
print(list_comp)

## generator expression -creates a generator

gen_exp =(x*x for x in range(5))
print(gen_exp)
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))