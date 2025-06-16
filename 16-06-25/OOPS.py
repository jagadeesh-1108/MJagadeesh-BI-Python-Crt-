#OOP'S - Object Oriented Programming System
#4 pillars of oops are - Inheritence, Polymorphism, Encapsulation, Abstraction
#Entity- Anything which exists or existance  in real world
#class- Logical Entity  or BluePrint or Plan to create a multiple objects 
# Multiple Objects Created using same class is known as Identical Objects or Similar Objects 
#Object- instance of class  or , It is a real world physical entity. It is also known as Instance 
#Instance - Specific object created from class. 
#syn for object creation:- Object_name = Class_name()
#Object_name = Class_name(arg)
#eg:-Mobile = Apple()
#source code is .py , byte code is  .pyc
#constructor are of 2 types - parameterized- other than self arguments , Non - parameterized - single parameter, default constructor  
class Student():
    def __init__(self):
        print("Hey..! I'm a Constructor of Student class")
        print(" I Will be Automatically invoked when the object is created")
s1=Student()#__init__(self)
s2=Student()
s3=Student()
s4=Student()
#__init__()method - magic method or dunder method  




