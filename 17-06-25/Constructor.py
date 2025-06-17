#Constructor without parameters
#constructor
class Mobile:
    def __init__(self):
        print("Mobile Constructor Called")
realme = Mobile()
#constructor without paramter - direct initialization
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'
        self.Battery_Capacity = '5500'
    def show_model(self):
        print("Model:", self.model)   
    def show_Battery_Capacity(self):
        print("Battery_Capacity:",self.Battery_Capacity)
realme = Mobile()
realme.show_model()
realme.show_Battery_Capacity()
 