#Exception
class InsufficientFundError(Exception): pass
balance = 10000
try:
    amount=int(input("Enter amount to Withdraw: "))
    if amount <=0:  
        raise ValueError("Withdrawal amount must be greater ")
    if amount > balance:
        raise InsufficientFundError("Insufficient balance for ")
    balance -=amount
    print(f"Withdrawal successful! Remaining balance: {balance}")
except ValueError as ve:
    print()    