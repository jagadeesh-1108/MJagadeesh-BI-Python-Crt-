#write a python program to read the list elements as input from the user & display the list element using for loop
size=int(input("Enter the size of the list: "))
prog_Lang=[]
#reading the list elements as input
for i in range(size):
    Temp=input()
    prog_Lang.append(Temp)
print("Elements of a List : ")
print(prog_Lang)