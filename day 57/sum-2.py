##   sum of list elements

def sum_list(m):
    if len(m)==0:
        return 0
    else :
        return m[0] + sum_list(m[1:])
print(sum_list([10,20,30,40]))    