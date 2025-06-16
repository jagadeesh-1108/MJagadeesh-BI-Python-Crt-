#employee class & objects creation
class Employee():
    def __init__(self,empname,empId,designation,empsalary,deptname):
        self.EmpName=empname
        self.EmpID=empId
        self.Designation=designation
        self.Salary=empsalary
        self.DeptName=deptname
def Diaplay_Details(self):
    print(f"Employee Name : {self.EmpName}")
    print(f"Employee ID : {self.EmpID}")
    print(f"Employee's Designation : {self.Designation}")
    print(f"Employee's Salary : {self.Salary}")
    print(f"Employee's DeptName : {self.DeptName}") 
    print("-------------------------------------")       
E1=Employee("Nani","EMP10",'Data Scientist',25000,'DeploymentTeam') 
print("---------------------------------------------------")
E2=Employee("jagadeesh","EMP102",'AI Spealist',50000,'AI Team')
E3=Employee("akhil",'EMP011','Data Enginner',30000,'DeploymentTeam')
E4=Employee("maharshi",'EMP011','Data Enginner',30000,'DeploymentTeam')
Diaplay_Details(E1)
Diaplay_Details(E2)
Diaplay_Details(E3)
Diaplay_Details(E4)
