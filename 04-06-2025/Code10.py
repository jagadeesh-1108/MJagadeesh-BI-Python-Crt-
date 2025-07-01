#write a python program to read 2 integers values as an input from the user 
a=int(input("Enter 1st element  "))
b=int(input("Enter 2nd element"))
#a,b=b,a
#print(a,b)
'''
Temp=a
a=b
b=Temp
print(a,b)'''
a=a+b
b=a-b
a=a-b
print(a,b)
