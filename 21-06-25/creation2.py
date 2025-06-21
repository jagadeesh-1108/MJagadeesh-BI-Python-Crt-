#creation of node
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
    def AddNode(self,data):
        N_Node=Node(data)
        N_Node.next=self.head
        self.head=N_Node
        current=N_Node
N1=Node(25.89)
          
node=Node(10)
print(node.Data)
node1=Node(20)
print(node1.Data)
node2=Node(30)
print(node2.Data)
current=node
current.next=node1
node1.next=node2
while current:
    print(current.Data ,end="-->")
    current=current.next
print("None")    