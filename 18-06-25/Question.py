#write a py program to create a employee class and declare the states and cretae 5 objects using diferent constructors 
class Employee:
    def __init__(self,empname,empid,Job,Salary,Location,Dept):
        self.EMPName=empname
        self.EMPID=empid
        self.JOB=Job
        self.SALARY=Salary
        self.LOCATION=Location
        self.DEPT=Dept
        print("Hey...! I'm a Six Parameterized Constructor")
        
    def __init__(self,empname,empid,Job,Salary,Location):
        self.EMPName=empname
        self.EMPID=empid
        self.JOB=Job
        self.SALARY=Salary
        self.LOCATION=Location    
        print("Hey...! I'm a Five Parameterized Constructor")
    def __init__(self,empname,empid,Job,Salary):
        self.EMPName=empname
        self.EMPID=empid
        self.JOB=Job
        self.SALARY=Salary   
        print("Hey...! I'm a Four Parameterized Constructor")
    def __init__(self,empname,empid,Job):
        self.EMPName=empname
        self.EMPID=empid
        self.JOB=Job
        print("Hey...! I'm a Three Parameterized Constructor")  
    def __init__(self,empname,empid):
        self.EMPName=empname
        self.EMPID=empid 
        print("Hey...! I'm a Two Parameterized Constructor")
    def __init__(self,empname):
        self.EMPName=empname
        print("Hey...! I'm a One Parameterized Constructor")
    def __init__(self):
        print("Hey...! I'm a No Parameterized Constructor")  
Emp1=Employee()
Emp2=Employee("Scott")
Emp3=Employee("Scott",'SC101')
Emp4=Employee("Scott",'SC101','Data Enginner')
Emp5=Employee("Scott",'SC101','Data Enginner',45000)
Emp6=Employee("Scott",'SC101','Data Enginner',45000,'Hybderabad')              
               


