#functions decleration within a function
def Eat():
    def Washhash():
        print("Wash hands...!")
    def ServeFood():
        print("ServeFood...!")
    Washhash()
    ServeFood()
    print("Enjoy Your meal...!")
    Washhash()
Eat()    
