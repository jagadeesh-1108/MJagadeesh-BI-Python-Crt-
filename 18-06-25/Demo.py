#class father 
class father:
    def __init__(self):
        pass
    @staticmethod
    def Work():
        print("Hardworking Father")
class Son(father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Work():
        print("Enjoying son")     
father.Work()
Son.Work()               
