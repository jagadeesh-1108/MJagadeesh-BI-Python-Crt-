#prime 1 to n using recurrsion
'''
n=int(input("Enter the number: "))
def primes(n,i=2):
    if i<=n:
        if is_prime(i):
            print(i)
    primes(n,i+1)

n = int(input("Enter N: "))
primes(n) '''