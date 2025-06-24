#write a py program to print even numbers from 1 to n using list comprehenssion
n=int(input("enter the element: "))
n=[i for i in range(n+1) if i%2==0]
print(n) 