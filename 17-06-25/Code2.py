#Write a python program to create a rectangle class and initialize the variables length and breadth using constructor and access the values using mutator methods 
class rectangle:
    def __init__(self,l,b):
        self.Lenght=l
        self.Breadth=b
        print("Object creation called")
    def Set_Details(self):
        self.Length = self.Lenght
        print(f"Length : {self.Lenght}")
        self.Breadth = self.Breadth
        print(f"Breadth : {self.Breadth}")
R=rectangle(20,19)
R.Set_Details()
