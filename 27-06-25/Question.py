#write a py program to read the month number input from the user and check whether it is a valid month number or not 
Month = int(input("Enter the Month Number:"))
if (Month>=1 and Month<=12):
    print("Valid Month Number")
else:
    print("In-Valid Month Number")    