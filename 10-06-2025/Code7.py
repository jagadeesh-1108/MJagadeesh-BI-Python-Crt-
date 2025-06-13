#write a python program to take name as input from the user including prefix(Mr/Ms)
#print the gender classification of the name on basics of prefix
str=input("Enter the name: ")
if str.startswith('Mr.')==True:
    print("Male")
elif str.startswith("Ms.")==True:
    print("Female")     