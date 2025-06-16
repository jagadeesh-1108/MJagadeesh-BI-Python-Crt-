#write a py program to create a mobile class and declare the staes of mobile as color , price, brand , series , version , features, storage, Battery capacity,Ram, Processor
#cretae 10 objects and initialize using constructor print the details of the individual objects using functions
class Mobile():
    def __init__(self,color,price,brand, series,version,features,storage,battery_capacity,ram, processor):
        self.Color=color
        self.Price=price
        self.Brand=brand
        self.Series=series
        self.Version=version
        self.Features=features
        self.Storage=storage
        self.Battery_capacity=battery_capacity
        self.Ram=ram
        self.Processor=processor
def Display_Details(self):
    print("Details of Mobiles: ")
    print(f" Mobile Color: {self.Color}")
    print(f" Mobile Price: {self.Price}")
    print(f" Mobile Brand: {self.Brand}")
    print(f" Mobile Series: {self.Series}")
    print(f" Mobile Version: {self.Version}")
    print(f" Mobile Features: {self.Features}")
    print(f" Mobile Storage: {self.Storage}")
    print(f" Mobile Battery_capacity: {self.Battery_capacity}")
    print(f" Mobile Ram: {self.Ram}")
    print(f" Mobile Processor: {self.Processor}")
    print("----------------------------------------")
M1=Mobile("BLUE",20000,"Samsung","A35",15,"Good Quality for Camera_Storage_Speed",'128GB',6000,'8GB','Spandragon')    
M2=Mobile("BLUE",20000,"Samsung","A55",15,"Good Quality for Camera_Storage_Speed",'512GB',6500,'12GB','Spandragon')
M3=Mobile("RED",25000,"IQOO","Z9S",16,"Good Quality for Camera_Storage_Speed",'128GB',6000,'8GB','Spandragon')
M4=Mobile("RED",15000,"OPPO","X6",16,"Good Quality for Camera_Storage_Speed",'128GB',6000,'4GB','Spandragon')
M5=Mobile("RED",25000,"POCO","M",16,"Good Quality for Camera_Storage_Speed",'128GB',6000,'8GB','Spandragon')
M6=Mobile("RED",120000,"IPhone","14",16,"Good Quality for Camera_Storage_Speed",'128GB',6000,'12GB','Spandragon')
M7=Mobile("RED",18000,"IQOO","Z9x",16,"Good Quality for Camera_Storage_Speed",'128GB',6000,'4GB','Spandragon')
M8=Mobile("RED",20000,"GOGGLE PIXELS","A",16,"Good Quality for Camera_Storage_Speed",'128GB',6000,'8GB','Spandragon')
M9=Mobile("RED",20000,"IQOO","Z7Lite",16,"Good Quality for Camera_Storage_Speed",'128GB',6000,'4GB','Spandragon')
M10=Mobile("RED",20000,"IQOO","Z6Lite",16,"Good Quality for Camera_Storage_Speed",'128GB',6000,'4GB','Spandragon')
Display_Details(M1)
Display_Details(M2)
Display_Details(M3)
Display_Details(M4)
Display_Details(M5)
Display_Details(M6)
Display_Details(M7)
Display_Details(M8)
Display_Details(M9)
Display_Details(M10)
