#pb statement 
#Consideer you are a HR Operations Mangaer in Vignan Softwae Solutions, you will be receieveing Applications from the candidates for multiple roles, 
#you are having a list of Jobroles write a program
# 1) To view the candidates Applications, Shortlisted applications, Jobroles 
# 2)Based on your evaluation on CV's of a candidate, Send a message to the candidate to update  weather his/her cv is shortlisted or not 
# 3) Shedule a interview for the paarticular shortlisted candidates 
# 4) Send a message to the candidate to update the status of their Level=1 interview Feedback and inform whether they are qualified or not for further level interview
# 5) Send an Offer letter to the shortlisted (level-3)candidates
Job_Roles=['Full Stack Developer','Data Engineer','Java Developer','Data Analyst','HR','Data Scientist','Team Lead']
Can_App=[
    #Name,Mailid,contactno,job applied for
    ['Jyothi','jyothi@gmail.com',1234567890,'Data Analyst'],
    ['Niharika','niharika@mail.com',9123458908,'Java Developer'],
    ['Nadeem','nadeem@gmail.com',89453256776,'Data Engineer'],
    ['Sravya','sravya@gmail.com',78462672398,'Full Stack Developer','HR'],
    ['Harshith','harshith@gmail.com',79124867983,]
]
Shortlisted_App=[
    ['Jagadeesh','abc@gmail.com',68251432876,'Tech Support'],
    ['Shraddha','xyz@gmail.com',2635116747,'SQL Admin']
]
Completed=[ ['Jyothi','jyothi@gmail.com',1234567890,'Data Analyst'],
    ['Niharika','niharika@mail.com',9123458908,'Java Developer'],]
#----------------------------------------------------------
def View_Details():
    print(f"Applied Candidates : ")
    print("------------------------")
    for i in Can_App:
        print(i)
    print(f"Shortlisted Candidates : ")
    print("------------------------")
    for i in Shortlisted_App:
        print(i)
    print(f"Finalized  Candidates : {Completed}")
def Shortlist_Profile():
    Name = input("Enter the Candidate Name : ")
    found = False
    for candidate in Can_App:
        if candidate[0] == Name:  # Check if the name matches
            found = True
            Temp = input("Enter Yes If Candidate's Profile Meets the Criteria & Job Requirement else Enter No : ")
            if Temp.lower() == "yes":
                print(f"Congratulations {Name}...! Your Profile is Shortlisted")
                # Move to shortlisted list
                Shortlisted_App.append(candidate)
                Can_App.remove(candidate)
            else:
                print(f"Hello {Name}...! We Regret to inform you that your Profile is not Shortlisted")
            break
    if not found:
        print(f"Candidate {Name} not found in applications")
def Schedule_Call():
    Name=input("Enter the Candidate Name to Schedule the Interview :")
    if Name in Shortlisted_App:
        print(f"Congratulations {Name} your profile is shortlisted & we are proceeding level-1  interview with our SME Please be available for Interview ")
    else:
        print(f"{Name}'s Profile is Rejected at CV Evaluation")
def Update_Status():
    Name=input("Enter the Name of Candidate:")
    Status=input("Enter Yes if qualifed in level-1 interview else enter no :")
    if Status in " Yes YES yes":
        print(f"Congratulations {Name} you have been Qualified in Level-1 Interview")
    else:
        print(F"We are regret to inform you that you have been disqualified in level-1 Interview")
def Send_OfferLetter():
    Name=input("Enter the Name of Candidate:")
    Status=input("Enter Yes if qualifed in all 3 level's of  interview else enter no :")
    if Status in " Yes YES yes":
        print(f"Congratulations {Name} you will recieve offer letter shortly , kindly acknowledge")
    else:
        print(F"Candidate data does not exist in database")

while(True):
    print("------------------------------------------------------")
    print("1.To View the Candidates Applications, ShortListed Applications,Job Roles")
    print("2.To ShortList the Profiles")
    print("3.Schedule an Interview for Shortisted Candidates")
    print("4.To Update the status of their profile ")
    print("5.Send Offer Letters to Particular Candidates")
    print("6.Exit")
    print("------------------------------------------------------")
    Choice=int(input("Enter Your Choice : "))
    if(Choice>=1 and Choice<=6):
        if Choice==1:
            View_Details()
        elif Choice==2:
            Shortlist_Profile()
        elif Choice==3:
            Schedule_Call()
        elif Choice==4:
            Update_Status()
        elif Choice==5:
            Send_OfferLetter() 
        else:
            print("Exit")
            break
    else:
        print("In-valid input") 
        


