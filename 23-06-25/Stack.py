#LIFO-Last in First Out
#if stack is  empty- element added at bottom
#  undo , redo 
#Stack - An Array or a List
class Stack:
    def __init__(self):
        self.Stack=[]
    def push(self,data):
        self.Stack.append(data)
        print(f"{data} Element is Appended")
    def isempty(self):
        if len(self.Stack)==0:
            return True
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.Stack.pop()
            print(f"Element is Removed")
    def peek(self):
        length=len(self.Stack)
        print(f"Peek element is {self.Stack[length-1]}")
    def Size(self):
        return len(self.Stack)    

    def Display(self):
        self.Stack.reverse()
        Str=[]
        for i in self.Stack:
            Str.append(i)
            Rev_Str="".join(Str)
        print(Rev_Str)
    #def Check_Balnce(self):
        #if '([{' ==  self.Stack[:3]:




stack = Stack()
stack.push('([{}])')
stack.push('A')
stack.push('N')
stack.push('I')
stack.Display()
stack.peek()
print("Stack size :",stack.Size())
stack.Display()

 