class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # fixed: changed 'Next' to 'next'

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new = Node(data)
        new.next = self.head  # fixed: use 'next' not 'Next'
        self.head = new

    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next  # fixed: use 'next' not 'Next'
        print("None")

# Example usage
ll = LinkedList()  # fixed: Capitalized class name
ll.insert_front(5)
ll.insert_front(10)
ll.insert_front(15)
ll.show()