#creation of node 
#insertion at end 
#count 
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None        
    def AddNode(self,data):
        N_Node=Node(data)
        N_Node.next=self.head
        self.head=N_Node
    def Display_List(self):
        current=self.head
        while current:
            print(current.Data,end="-->")
            current=current.next
        print("None")    
    def insert_end(self,data):
        new = Node(data)
        if not self.head:
            self.head=new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new    
    def count_nodes(self):
        count =0
        temp = self.head 
        while temp:
            count += 1
            temp = temp.next
        return count   
    def delete_front(self):
        if self.head:
            self.head=self.head.next
L1=LinkedList()
L1.AddNode(25.89)
L1.AddNode(99.56)
L1.AddNode(76.54)
L1.AddNode(100)
L1.insert_end(120)
L1.Display_List() 
print(L1.count_nodes())
L1.Display_List()
print(L1.delete_front())
L1.Display_List() 