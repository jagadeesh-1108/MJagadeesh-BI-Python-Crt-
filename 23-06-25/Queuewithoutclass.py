#queue without class
from collections import deque
queue= deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueuing :",queue)
first = queue.popleft()
print("Dequed elements:",first)
print("Queue after dequeuing:",queue)
if not queue:
    print("Queue is empty")
else:
    print("queue is not empty")
print("front element:", queue[0])
