#write a py program to create a customer service by adding the customer into the queue and once the customer served he has to be removed from the queue
from collections import deque
class CustomerService:
    def __init__(self):
        self.queue=[]
    def Enqueue(self,customername):
        self.queue.append(customername)
    def is_empty(self):
        return len(self.queue)==0     
    def Deueue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)    
customer = CustomerService(1)
print(CustomerService.queue.append())
print(CustomerService.Enqueue('Chicken_Biryani'))
print(print(CustomerService.is_empty()))
print(CustomerService.Deueue())
