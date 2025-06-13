#Write a py program to read a string as input from the user and 
# 1) print count of upper case letters 
#2)print count of lower case letters 
#3)print the count of numeric values 
#4)print the count of special characters 
str=input("enter the string : ")
Uppercase_Alpha=0
Lowercase_Alpha=0
Numeric=0
special_char=0
for ch in str:
    if ch.isupper():
        Uppercase_Alpha+=1
    elif ch.islower():
        Lowercase_Alpha+=1
    elif ch.isdigit():   
        Numeric+=1
    else:
        special_char+=1
print(f"Count of Upper case letters : {Uppercase_Alpha}")
print(f"Count of Lower case letters : {Lowercase_Alpha}")
print(f"Count of Numeric values : {Numeric}")
print(f"Count of Special characters : {special_char}")                 
