#Destructor - used to destroyed the object 
#__del__ is used 
class Mobile:
    def __init__(self):
        print("Object is created")
    @classmethod
    def Display(Class):
            print("I'm a Class Method")
            print("I Will Work Irrespective of Object creation")
Mobile.Display()
M1=Mobile()
M1.Display()



