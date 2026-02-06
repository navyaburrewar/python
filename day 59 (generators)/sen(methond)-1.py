def func():
    balance=0
    while True: 
       amount= yield balance
       if amount is not None:
           balance+=amount
           
account = func()

print(next(account))      # 0
print(account.send(100))  # 100
print(account.send(50))   # 150
print(account.send(-30))  # 120
