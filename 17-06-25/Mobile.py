# Accessor and mutator methods 
class Mobile:
    def __init__(self,p,c,b):
        self.Price=p
        self.Color=c
        self.Brand=b
        print("Object is Created")
    #Mutator
    def Set_Color(self):
        self.Color='Blue'
    #Accessor
    def Get_Details(self):
        print(f"Color : {self.Color}")
        print(f"Price : {self.Price}")
        print(f"Brand : {self.Brand}")
M1=Mobile(12000,'Black','Samsung')
M1.Get_Details()
print("After Updating....!")
M1.Set_Color()
M1.Get_Details()

