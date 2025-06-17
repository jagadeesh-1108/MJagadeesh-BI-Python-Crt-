'''write a py program to create a book class declare the states as Bookname, Authourname, PublisherName,Publisheddate,CategoryofBook
i)Create 5 objects & Initionalize the values using Constructor where out of five 
---create 1 object using one parameterized constructor
---create 2 object using two parameterized constructor
---create 3 object using zero parameterized constructor
----create 4 object using four parameterized constructor
-----create 5 object using five parameterized constructor
ii)Access the values using Accessor Methods 
iii)Update the values using mutator method for name of the book'''
class Book:
    def __init__(self,bookname):
        self.BookName=bookname
    def Get_1(self):
        print(f"BookName: {self.BookName}")    
        print("----------------------------!")

    def __init__(self,bookname,authourname):
        self.BookName=bookname
        self.AuthourName=authourname
    def Get_2(self):
        print(f"BookName: {self.BookName}")
        print(f"AuthourName: {self.AuthourName}")  
        print("-------------------------------------!")  
    def __init__(self):
        pass
    def Get_3(self):
        print("There is No Book 3")
        print("-------------------------------------!")
        
    def __init__(self,bookname,authourname,publishername,publisheddate):
        self.BookName=bookname
        self.AuthourName=authourname
        self.PublisherName=publishername
        self.PublishedDate=publisheddate  
    def Get_4(self):
        print(f"BookName: {self.BookName}")
        print(f"AuthourName: {self.AuthourName}")
        print(f"PublisherName: {self.PublisherName}")
        print(f"Publisheddate: {self.PublishedDate}")
        print("-------------------------------------------------!")
    def __init__(self,bookname,authourname,publishername,publisheddate,categoryofbook):
        self.BookName=bookname
        self.AuthourName=authourname
        self.PublisherName=publishername
        self.PublishedDate=publisheddate
        self.CategoryofBook=categoryofbook
        print("Object is Created") 
    def Get_Details(self):
        print(f"BookName: {self.BookName}")
        print(f"AuthourName: {self.AuthourName}")
        print(f"PublisherName: {self.PublisherName}")
        print(f"Publisheddate: {self.PublishedDate}")
        print(f"CategoryofBook: {self.CategoryofBook}")
        print("-----------------------------------------!")
    def Set_Details(self):
        self.BookName="Java"
B1=Book('PythonJoy of Life','Jagadeesh','Sravya','17-06-25','Coding')
B2=Book('RichDad & PoorDad ','Akhil','Teenu','17-06-25','Personal Finance')
B3=Book('Java of Life','Yogya','Pretty','17-06-25','Coding')
B4=Book('C of Life','Sriram','Lalasa','17-06-25','Coding')        
B5=Book('C++ of Life','Akhil','Maharshi','17-06-25','Coding')
B1.Get_1()
B2.Get_2()
B3.Get_3()
B4.Get_4()
B5.Get_Details()




