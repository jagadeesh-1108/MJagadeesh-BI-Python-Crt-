#write a python program to create a product class delcare the states of class as product name, product id , price , gst, Manufacture date, Expire Date
#Create 5 objects initialized using parameterized constructor and access the elements using instance method and declare mutator methods as set product name, set product id ...... and change the values of the properties using mutator methods and print it 
class product:
    def __init__(self,product_name,product_ID,p,gst,manufacture_date,expire_date):
        self.Product_Name=product_name
        self.Product_ID=product_ID
        self.Price = p
        self.GST=gst
        self.Manufacture_Date=manufacture_date
        self.Expire_Date=expire_date
        print("Object is Created")
    #Mutator
    def Set_Product_Name(self):
        self.Product_Name = 'Sunsrceen'
    def Set_Product_ID(self):
        self.Product_ID = 'SUN101'
    def Set_Price(self):
        self.Price = '250'     
    def Set_GST(self):    
        self.GST = '50'
    def Set_Manufacture_Date(self):    
        self.Manufacture_Date = '17-06-2025'
    def Set_Expire_Date(self):
        self.Expire_Date='17-06-26'
    #Accessor
    def Get_Details(self):
        print(f"Product Name : {self.Product_Name}")
        print(f"Product ID : {self.Product_ID}")
        print(f"Price : {self.Price}") 
        print(f"GST : {self.GST}")  
        print(f"Manufacture Date : {self.Manufacture_Date}")
        print(f"Expiery Date : {self.Expire_Date}")
P1=product('Body_Lotion','LOC101','200','25','16-06-25','16-06-26')
P2=product('Hair_Oil','HO102','200','25','16-06-25','16-06-26')
P3=product('Shampoo','SH101','200','10','16-06-25','16-06-26')
P4=product('Tooth_Paste','TH101','200','15','16-06-25','16-06-26')
P5=product('Brush','BH101','200','25','16-06-25','16-06-26')
P1.Get_Details()
print("After Updation.....................!")
P1.Set_Product_Name()
P1.Set_Product_ID()
P1.Set_Price()
P1.Set_GST()
P1.Set_Manufacture_Date()
P1.Set_Expire_Date()
P1.Get_Details()
P2.Get_Details()
print("After Updation.....................!")
P2.Set_Product_Name()
P2.Set_Product_ID()
P2.Set_Price()
P2.Set_GST()
P2.Set_Manufacture_Date()
P2.Set_Expire_Date()
P2.Get_Details()
P3.Get_Details()
print("After Updation.....................!")
P3.Set_Product_Name()
P3.Set_Product_ID()
P3.Set_Price()
P3.Set_GST()
P3.Set_Manufacture_Date()
P3.Set_Expire_Date()
P3.Get_Details()
P4.Get_Details()
print("After Updation.....................!")
P4.Set_Product_Name()
P4.Set_Product_ID()
P4.Set_Price()
P4.Set_GST()
P4.Set_Manufacture_Date()
P4.Set_Expire_Date()
P4.Get_Details()
P5.Get_Details()
print("After Updation.....................!")
P5.Set_Product_Name()
P5.Set_Product_ID()
P5.Set_Price()
P5.Set_GST()
P5.Set_Manufacture_Date()
P5.Set_Expire_Date()
P5.Get_Details()
      
      
      
      
      
