#Write a python programme to read the size of the list as input from the user and take the list elements also as a input from the user and find the length of the list the maximum number or element present in the list and similarly the maximun number , minimum number and summation of the element and print the sorted list in ascending order 
Size=int(input("Enter the Size of the list: "))
Num=[]
for i in range(Size):
    Temp=int(input(f"Enter the Element at {i} index: "))
    Num.append(Temp)
print(f"Given List: {Num}")
print("Maximum Element:",max(Num))
print("Minimun Element:",min(Num))
print("Summation of a  Element:",sum(Num))
print("Sorted Element:",sorted(Num))