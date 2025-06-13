#write a py program to read the str as input from the user
#1) Reverse the string
#2)convert the stn into lowercse
#3) str into uppercase
#4)convert the char of str to lowercase if it is in upper case
#5) convert the char of str to upper case if it is in lowercase
#6)check if the str is starting with the letter a
# 7)print the count of the char a from the give string  and replace all letter p's to letter j 
str=input("Enter the sequence: ")
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.startswith('A'))
print(str.count('P'))
str=str.lower()
print(str.replace('p','j'))
