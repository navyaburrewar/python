def max_number(m):
    if len(m)==1:
        return m[0]
    else:
        max_rest= max_number(m[1:])
        return m[0]if m[0]>max_rest else max_rest
    
print(max_number([2,3,86,1]))    





def max_number(m):
    if len(m)==1:
        return m[0]
    else:
        max_rest= max_number(m[1:])
    if m[0]>max_rest:
          return m[0]
    else:
          return  max_rest
    
print(max_number([2,3,86,1]))    
