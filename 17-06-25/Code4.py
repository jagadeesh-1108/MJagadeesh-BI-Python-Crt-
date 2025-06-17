'''
write a py program to create a squareshape class & declare the proprtities as 
length
breadth
height
i) calculate the Area of square using Instance methods 
ii)check whether the sides of square's are equal or not using instance methods 
iii)Calcualte the perimeter of square using instance methods 
iv)Find the Diagonals of square using instance methods 
v)find the side length of square using instance methods 
'''
class Squareshape:
    def __init__(self,l,b,h):
        self.Length=l
        self.Breadth=b
        self.Height=h
    def Area_Square(self):
        A=self.Length*self.Breadth
        print(" Area of Square : ",A)
    def SideEqual(self):
        S = (self.Length ==  self.Breadth)    
        print("Side of Square is Equal or Not : ",S)
    def Perimeter_Square(self):
        P = 4*(self.Length+self.Breadth)
        print("Perimeter of a square : ",P)
    def Diagnoals_Square(self):
        D = 1.414*(self.Length+self.Breadth)
        print("Diagnoal of square : ",D)
    def SideLength(self):
        SL= ( 4*(self.Length+self.Breadth)/4)
        print("SideLength : ",SL)
S1=Squareshape(4,5,13)
S1.Area_Square()
S1.SideEqual()
S1.Perimeter_Square()
S1.Diagnoals_Square()
S1.SideLength()


