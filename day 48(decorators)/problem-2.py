def marks(func):
    def sub(name):
        result=func(name)
        return result.upper()    
    return sub



@marks
def school(name):
    return("20 marks "+name)
print(school("akhi"))
