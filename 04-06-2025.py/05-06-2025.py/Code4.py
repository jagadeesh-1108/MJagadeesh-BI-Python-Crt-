#write a python program to read the list elements as a input from the user and print the new list of numbers which are multiplies of 5 
List=[]
New_List=[]
len=int(input("Enter the size of the list "))
for i in range(len):
    Temp=int(input(f"Enter the integer value at {i} index "))
    List.append(Temp)
print("Given List: ")    
print(List)
for i in List:
    if i%5==0:
        New_List.append(i)        
print(New_List)
