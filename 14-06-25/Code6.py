#pb statement 
#Consideer you are a HR Operations Mangaer in Vignan Softwae Solutions, you will be receieveing Applications from the candidates for multiple roles, 
#you are having a list of Jobroles write a program
# 1) To view the candidates Applications, Shortlisted applications, Jobroles 
# 2)Based on your evaluation on CV's of a candidate, Send a message to the candidate to update  weather his/her cv is shortlisted or not 
# 3) Shedule a interview for the paarticular shortlisted candidates 
# 4) Send a message to the candidate to update the status of their Level=1 interview Feedback and inform whether they are qualified or not for further level interview
# 5) Send an Offer letter to the shortlisted (level-3)candidates
Job_Roles=['Full Stack Developer','Data Engineer','Java developer','Data analyst','Data Scientist','Team Lead']
Can_APP=[
    #Namae,mailid , Contactno,job,applied for
    ['Jyothi','jyothi@gmail.com',1234567890,'Data Analyst'],
    ['nani','nani@gmail.com',2131131230,'Java developer'],
    ['jagadeesh','jagadeesh@gmail.com',545454504,'Data enginner'],
    ['Harshith','harshith@gmail.com',7894561230,'HR']
]
Sortlisted_APP=[
    ['mani','mani@gmail.com',54353216780,'Tech supportt'],
    ['Akhil','akhil@gmail.com',4564656790,'Sql Admin']
]
Completed=[]
#------------------------------------------------------------------------
def Veiw_Details():
    print(f"")
def Update_Status():
    Name=input("Enter ty=he name ")    
while(True):
    print("1.To view the candidates Applications, Shortlisted applications, Jobroles")
    print("2.To shortlist the profiles")
    print("3.Shedule a interview for the paarticular shortlisted candidates")
    print("4.To update the status of their profile")
    print("5.Send an Offer letter to the shortlisted ")
    print("6.Exit")
    print("--------------------------------------------------------------")
    choice=input("enter the choice : ")
    if(Choice>=1 and Choice<=6):
        if Choice==1:
            Veiw_Details()
        elif choice==2:
            Shortlist_Profile()
        elif Choice==3:
            Schedule_()
        elif Choice==4:
            Update_Status()
        elif choice==5:
            Send_OfferLetter()
        elif Choice==6:
            Exit()             
        


