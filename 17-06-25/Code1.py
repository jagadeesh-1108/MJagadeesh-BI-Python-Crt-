#Write a py program student class  declare the properties as student name , student id , branch , percentage, age, year of passing , No.of.certifications , create 10 objects and initialize the values using mutator method and access the values using accessor  (Note:- initialize the values without using constructor)
class Student:
    pass
    def Set_Details(S):
        S.Name=input("Enter the Student Name : ")
        S.ID=input("Enter the Student ID : ")
        S.Branch=input("Enter the Student Branch : ")
        S.Percentage=int(input("Enter the Student Percentage : "))
        S.Age=int(input("Enter the Student Age : "))
        S.Passout=input("Enter the Student Passed out year : ")
        S.No_of_certifications=int(input("Enter the Student No_oF_certifications  : "))
    def Get_Details(S):
        print(f"Student name : {S.Name}")
        print(f"Student branch : {S.ID}")
        print(f"branch : {S.Branch}")
        print(f"percentage : {S.Percentage}")
        print(f"age : {S.Age}")
        print(f"Passout : {S.Passout}")
        print(f"No_of_certifications : {S.No_of_certifications}")
S=Student()
S.Set_Details()
S.Get_Details()
S1=Student()
S1.Set_Details()
S1.Get_Details()
S2=Student()
S2.Set_Details()
S2.Get_Details()
S3=Student()
S3.Set_Details()
S3.Get_Details()
S4=Student()
S4.Set_Details()
S4.Get_Details()
S5=Student()
S5.Set_Details()
S5.Get_Details()
S6=Student()
S6.Set_Details()
S6.Get_Details()
S7=Student()
S7.Set_Details()
S7.Get_Details()
S8=Student()
S8.Set_Details()
S8.Get_Details()
S9=Student()
S9.Set_Details()
S9.Get_Details()







