'''1.write a py program to calculate factorial of n using recursion
2.write a py program to calculate sum of first n natural numbers using recursion
3.write a py program to print the power of a given number using recursion
4.write a py program to calculate sum of digits of the given number using recursion
5.write a py program to calculate count of digits of the given  number using recursion 
6.write a py program to reverse the string using recursion
7.write a py program to calculate maximum element from the list using recursion
8.write a py program to calculate minimum elements from the list using recursion
'''
N=int(input("Enter the Number: "))
def factorial(N):
    if N==0:
        return 1
    else:
        return  N*factorial(N-1) 
print(factorial(N))    