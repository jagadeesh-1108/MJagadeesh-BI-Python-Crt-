#write a py program to read the year as input from the user and check whether it is a leap year or not 
n= int(input(" Enter the year: "))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("It is a Leap Year") 
else:
    print("It is not a Leap Year")    
   
