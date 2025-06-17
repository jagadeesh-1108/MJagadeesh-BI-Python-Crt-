class Ob:
    def __init__(self,p_Name,p_Price,p_ID,p_GST,p_manufdata,p_exppirydate):
        self.P_Name=p_Name
        self.P_Price=p_Price
        self.P_ID=p_ID
        self.P_GST=p_GST
        self.P_Manufdata=p_manufdata
        self.P_Exppirydate=p_exppirydate
        print("Object is Created")
    def Set_Modify(self):
        self.P_Name='Rare beatuty'
        self.P_Price=15038
        self.P_ID='pd_12'
        self.P_GST=324
        self.P_Manufdata='12/2/2024'
        self.P_Exppirydate='13/4/2025'
    def Get_Modifi(self):
        print(f"product name {self.P_Name}")
        print(f"product price{self.P_Price}")
        print(f"product ID{self.P_ID}")
        print(f"product GST{self.P_Price}")
        print(f"product Manufacturing date{self.P_Manufdata}")
        print(f"product Expiry Date{self.P_Exppirydate}")
    
M1=Ob("Rhode beauty",7623776,"pd_123",768,'12/4/2024','13/4/2026')
M1.Get_Modifi()
print("After Modification.......................!")
M1.Set_Modify()
M1.Get_Modifi()
M2=Ob("Fenty beauty",776,"pd_1234",7268,'1/4/2020','3/4/2026')
M2.Get_Modifi()
print("After Modification.......................!")
M2.Set_Modify()
M2.Get_Modifi()