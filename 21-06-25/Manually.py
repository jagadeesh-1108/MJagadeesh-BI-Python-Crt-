#manually create a linkedlist with 3 elements
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
    def AddNode(self,data):
        Node=Node(data)
        Node.next=self.head
        self.head=Node
a=Node(10)
b=Node(20)
c=Node(30)
a.next=b
b.next=c
temp=a
while temp:
    print(temp.Data, end="-->")
    temp=temp.next
print('None')    
