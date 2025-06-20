#1.write a py program to calculate factorial of n using recursion
n=int(input("enter a number: "))
def factorial(n):
    if n==0:
        return 1
    else :
        return n*factorial(n-1)
print(factorial(n))    

