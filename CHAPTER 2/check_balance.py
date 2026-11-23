class Insufficientbalanace(Exception):
    pass
try:
    balance=5000
    
    amount=int(input("enter withdrawal amount"))
    
    if amount<=0:
        raise ValueError("enter a valid amount")
    
    if amount > balance:
        raise Insufficientbalanace("Insufficient balance")
    
    balance=balance-amount
    
    print("withdrawal successful")
    print("remaining balance",balance)
    
except Insufficientbalanace as e:
    print("Error",e)
    
except ValueError as e:
    print("Error",e)
    