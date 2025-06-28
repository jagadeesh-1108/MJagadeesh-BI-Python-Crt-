#exceptions
'''
try:
    statements
ecept:
    statements    
'''
num=int(input("ENter the number:" ))
print("Program Exceution Begins")
print(num)
try:
    print(num/0)
except ZeroDivisionError:
    print("Dividing with Zero Gives an infinite Value")
print("Program Exceution Ends")