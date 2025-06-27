#write a py program to read the month number as input from the user and print the respective days present in the month 
Month = int(input("Enter the Month Number:"))
if Month in [4,6,9,11]:
    print("30 Days")
elif Month in [1,3,5,7,8,10,12]:
    print("31 Days")
elif Month==2:
    print("28 or 29 Days")
else:
    print("In-Valid Month Number")    

