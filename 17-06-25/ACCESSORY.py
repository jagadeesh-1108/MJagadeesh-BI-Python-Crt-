#Accessorymethod - to acces only
class Employee():
    def __init__(self,empname,empID,designation,salary,deptname):
        self.EmpName=empname
        self.EmpID=empID
        self.Designation=designation
        self.Salary=salary
        self.DeptName=deptname
    def Get_Details(self):
        print(self.EmpName)
        print(self.EmpID)
        print(self.Designation)
        print(self.Salary)
        print(self.DeptName)
E1=Employee("Scott",'EMP101','Data Analyst',25000,'DeploymentTeam')
E1.Get_Details()
