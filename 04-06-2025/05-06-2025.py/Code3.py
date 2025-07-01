#write a python program to remove the duplicate values from the list 
List=[2,5,5,6,6]
print("Original List: ")
print(List)
New_List=[]
for i in List:
    if i not in New_List:
        New_List.append(i)
print(New_List)
        


