#multi level inheritence - method overriding 
class GrandFather:
    def _init_(self):
        pass
    #method overriding
    @staticmethod  
    def Properties():
        print("100 acres of land")
class Father(GrandFather):
    def _init_(self):
        super()._init_()
    @staticmethod 
    def Properties():
        print("50 acres of land")
class You(Father):
    def Properties():
        print("A Btech degree")
GrandFather.Properties()
Father.Properties()
You.Properties()                                  