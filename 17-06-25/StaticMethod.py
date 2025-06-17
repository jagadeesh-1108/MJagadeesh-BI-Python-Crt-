class Mobile:
    def __init__(self):
        print("Object is created")
    @staticmethod
    def Display(Class):
            print("I'm a Class Method")
            print("I Will Work Irrespective of Object creation")
            print("value is  : ",Class)
Mobile.Display(10)


'''global variable - A variable which is declared within the class but outside of a method, function,constructor or block is known as Global variable
 Global variable has global scope where you can acess the variable through out the program 
It has a global access
Local Variable : A variable which is declared within the class but inside of a method ,  function, constructor or block is known as local Variable 
Local variable has limited scope where you can access the variable within the given scope(either function or method or constructor)
it has a limited acces'''

