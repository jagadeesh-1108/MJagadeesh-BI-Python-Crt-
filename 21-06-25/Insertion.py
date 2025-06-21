#insertion at end
class Node:
    def __init__(self,data):
        self.Data=data
        self.next=None
    def insert_end(self,data):
        new = Node(data)
        if not self.head:
            self.head=new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
LL=Node(10)
LL.insert_end(20)
