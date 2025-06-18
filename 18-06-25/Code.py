#method/ Function overloading and over riding using mobile unlocking 
class Mobile:
    def __init__(self):
        print("Object is Created ")
def UnlockMobile():
    print("Swipe up to unlock your Mobile....!")
UnlockMobile()
def UnlockMobile(Password):
    print("Enter Password to unlock Your Mobile.....!")
UnlockMobile("XYZ123")
def UnlockMobile(Num,pattern):
    print("Enter the Pin to unlock Your Mobile..................!")
UnlockMobile(4,'AAAA ')                    