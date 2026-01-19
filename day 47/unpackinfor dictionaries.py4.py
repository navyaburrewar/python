### unpackin with dictionaries with**
#If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

def func(fname,lname):
    print( "hello",fname,lname)

greeting = {"fname":"navya","lname":"burrewar"}
func(**greeting)
