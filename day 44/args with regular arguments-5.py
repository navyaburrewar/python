def func(greeting,*names):
  for name in names:
    print(greeting,name)
func("hello","choti","neha","nandhini")    

## In this example, "Hello" is assigned to greeting, and the rest are collected in names.


def func(greeting,*names):
  for name in names:
    print(greeting,name)
func("nice to meet you","nandhini","neha","choti")    


