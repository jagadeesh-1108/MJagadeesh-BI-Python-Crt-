#write a py program to take len of queue as input from the user and add the elements by using enque method and print the elements present in the queue and remove the elements from the queue one by one and check whether the queue is empty or not and print the front peek and rear peek  
class custom:
    def __init__(self):
        self.queue=[]
    def add_c(self,cus):
        self.queue.append(cus)
    def serv(self,ser):
        n = int(input("Enter 1 if customer recieved service or Enter 0: "))
        if(bool(n)):
            temp = self.queue.pop(ser)
            print(f"{ser} is serviced successfully")
        else:
            print("The customer is not satisfied with the service")
    
    def mt(self):
        if not self.queue:
            print("Not empty")
        else:
            print("Empty")

qu = custom()
num = int(input("Enter the number of customers: "))
for i in range(num):
    temp = input("Enter customer name: ")
    qu.add_c(temp)
print("**Customer service access**")
for i in range(num):
    qu.serv(i)

qu.mt()














'''
from collections import deque
queue =  deque()

num = int(input("num of customers at cs "))
for i in range (num):
    temp = input("enter the customer name: ")
    queue.append(temp)
print("first elemnent in queue is: ",queue[0])
print("last elemnent in queue is: ",queue[len(queue)-1])
print(" *dequeuing* ")
for i in range(num):
    t = queue.popleft()
    print(f"element {i+1} is popped")
print("not empty") if bool(queue) else print("empty")'''

