class InsufficientFundsError(Exception):
    pass

def withdraw(balance : float , amount : float ) -> float:
    if amount>balance:
        raise InsufficientFundsError(f"Current Balance : {balance} is less than requested amount : {amount}")
    else:
        return balance-amount
    

try:
    x = withdraw(100,200)
except InsufficientFundsError as error:
    print(error)