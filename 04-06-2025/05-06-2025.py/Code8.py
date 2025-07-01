#write a python code 
#input a list of numbers 
#Create two new lists: one for even numbers , one for odd numbers
#Display both lists
Size=int(input("Enter the Size of the list "))
List=[]
for i in range(Size):
    Temp=int(input("Enter the elements "))
    List.append(Temp)
print(List)
Even=[]
Odd=[]
for i in List:
    if i %2==0:
        Even.append(i)
    else:
        Odd.append(i)
print(Even)
print(Odd)
                

