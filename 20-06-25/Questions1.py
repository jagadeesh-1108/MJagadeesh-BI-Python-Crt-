#2.write a py program to calculate sum of first n natural numbers using recursion
n1=int(input("Enter a number: "))
def sum(n1):
    if n1==0:
        return 0 
    else:
        return n1+sum(n1-1) 
      
print(sum(n1))   