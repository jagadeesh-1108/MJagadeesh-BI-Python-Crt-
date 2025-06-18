#Heraricheal level inheretance 
class Graduation():
    def __init__(self):
        pass
    @staticmethod
    def Graduation():
        print("Congraculations you are a graduate now")
#first sub class
class CSE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduation():
        print("Cobgratulations you are a computer Science graduate")
#second class        
class BI(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduation():
        print("Cobgratulations you are a Bioinformatics graduate")  
#third sub class
class ECE(Graduation):
    def __init__(self):
        pass
    @staticmethod
    def Graduation():
        print("Cobgratulations you are a ECE graduate")      
Graduation.Graduation()
CSE.Graduation()
BI.Graduation()
ECE.Graduation()


