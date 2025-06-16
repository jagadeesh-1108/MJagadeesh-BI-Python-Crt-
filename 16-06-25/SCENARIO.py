#Scenario:
#you have attended a skill development training programme for fifteen days on python programming language
#task:
# Write python programme to give the detailed report of 15 days python training which includes
#1)Day
#2)Topics Covered
#3)Efficiency (rae & grip on topics learnt on a scale of 5)
#4)Number of Assignments Solved
#5)Number of Hackerrank Questions Solved
#6)Rating Acheived on Hackerrank fro that particular day
#7)Certifications Completed (including name of Certificate)
# 8)Duration Class
# 9)Rate the session on scale of 5 where
# i)1- being worst
# ii)2-being bad
# 3-being average
# 4-being good
# 5-being best
class report():
    def __init__(self,day,topics,efficiency,No_of_assignments_Solved,No_of_Hackerrank_Solved,Rate_of_Session):
        self.Day=day
        self.Topics=topics
        self.Efficiency=efficiency
        self.NO_OF_Assignments_Solved=No_of_assignments_Solved
        self.NO_OF_HACKERRANK_Solved=No_of_Hackerrank_Solved
        self.RATE_OF_SESSION=Rate_of_Session
def Display_report(self):
    print("Detailed report : ")
    print(f"DAY : {self.Day}")
    print(f"Topics Covered: {self.Topics}")
    print(f"Efficiency : {self.Efficiency}")
    print(f"NO_OF_Assignments_Solved: {self.NO_OF_Assignments_Solved}")
    print(f"NO_OF_HACKERRANK_Solved: {self.NO_OF_HACKERRANK_Solved}")
    print(f"RATE_OF_SESSION:{self.RATE_OF_SESSION}")
    print("------------------------------------------------------")
R1=report(1,"Basics of Python",70,10,6,"")
R2=report(2,"Variables",70,10,7,"Average")
R3=report(3,"Operators",70,10,8,"AVERAGE")
R4=report(4,"Data Types",70,10,6,"good")
R5=report(5,"SEQ DATA TYPES",45,10,7,"good")
R6=report(6,"SETS",50,10,8,"Average")
R7=report(7,"LIST",50,10,6,"good")
R8=report(8,"FUNCTIONS",60,10,7,"good")
R9=report(9,"Function Declerations ",60,10,8,"Average")
R10=report(10,"Function Call",65,10,9,"good")
R11=report(11,"OOPS",70,10,6,"Average")
R12=report(12,"4 Pillars of OOPS",71,10,6,"good")
R13=report(13,"CLASS",80,12,9,"good")
R14=report(14,"OBJECTS",90,15,9,"BEST")
R15=report(15,"REVISION",90,18,10,"BEST")

Display_report(R1)
Display_report(R2) 
Display_report(R3) 
Display_report(R4) 
Display_report(R5) 
Display_report(R6) 
Display_report(R7) 
Display_report(R8) 
Display_report(R9) 
Display_report(R10) 
Display_report(R11) 
Display_report(R12) 
Display_report(R13) 
Display_report(R14)
Display_report(R15)


 
