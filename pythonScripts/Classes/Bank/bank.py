class InsufficientFundsException(Exception):
    pass

def withdraw(balance : float , amount : float ):
    if (amount>balance):
        raise InsufficientFundsException(f"Current Balance : {balance} is less than requested amount : {amount}")
    else:
        return balance-amount
    

try:
    x = withdraw(100,200)
except InsufficientFundsException as error:
    print(error)