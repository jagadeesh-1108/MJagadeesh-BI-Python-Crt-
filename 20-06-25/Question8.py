#to create a linkedlist of size n user input and data as input from the user 
class Node():
    def __init__(self,data):
        self.Data=data
        self.Next=None
class LinkedList(Node):
    n=int(input(" Enter the value: "))
    Head=int(input("Enter the Head Value: "))
    Tail=int(input("Enter the Tail Value: "))
    for i in (Node,n):
        print(f"Enter the value at {i} index position ")

head=Node(int(input("Enter the value: ")))
head.Next=Node(int(input("Enter the value:"))) 
Current=head
while Current:
    print(Current.Data,end="-->")
    Current=Current.Next
print("None")    

