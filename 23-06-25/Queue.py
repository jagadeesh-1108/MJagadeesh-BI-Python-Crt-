#Queue
class Queue:
    def __init__(self,items):
        self.items=[]
    #Enqueue - adds an elements at the end (rear)
    def Enqueue(self,item):
        self.items.append(item)
    #check queue is empty 
    def is_empty(self):
        return len(self.items)==0    
    #Dequeue - deletes or removes items from front
    def Dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    #Look at the front item without reemoving
    def peek_front(self):
        if self.is_empty():
            return None
        return self.items[0]
    #Look at rear item without removing
    def peek_rear(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def size(self):
        return len(self.items)
queue = Queue(1)
print(queue.Enqueue(2))
print(queue.is_empty())
print("Queue size :",queue.size()) 