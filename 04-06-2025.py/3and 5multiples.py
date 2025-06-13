#write a python program to read the list elements as a input from the user and check whether the list elements are the multiples of 3 and 5 or not and print the list of elements which are multipleies of 3 and 5

List=[]
New_List=[]
len=int(input("Enter the size of the list "))
for i in range(len):
    Temp=int(input(f"Enter the integer value at {i} index "))
    List.append(Temp)
print("Given List: ")    
print(List)
for i in List:
    if i%5==0 and i%3==0:
        New_List.append(i)        
print(New_List)
