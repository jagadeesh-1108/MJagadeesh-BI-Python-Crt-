#college level codding fest
'''
you have participated in your college level coding fest which was there for 6 days
write a py prog to give the final report which includes
1) Activities for the day including timeline
2) Number of teams/participants of the day
3) Project name
4) technologies used
5) PPT demonstration given
6) Winner of day
7) Runner up of the day
8) Best Performer of the day
9) Host of the program for that day
'''
class Final_Report():
    def __init__(self,Activities,No_of_teams_participated,project_names,technologies_used,ppt_demo_given,winner_of_the_day,runner_of_the_day,best_performer_of_the_day,host_of_program):
        self.ACTIVITIES_FOR_THE_DAY=Activities
        self.NO_OF_TEAMS_PARTICIPATED=No_of_teams_participated
        self.PROJECT_NAMES=project_names
        self.TECHNOLOGIES_USED=technologies_used
        self.PPT_DEMO_GIVEN=ppt_demo_given
        self.WINNER_OF_THE_DAY=winner_of_the_day
        self.RUNNER_OF_THE_DAY=runner_of_the_day
        self.BEST_PERFORMER_OF_THE_DAY=best_performer_of_the_day
        self.HOST_OF_THE_PROGRAM=host_of_program
def Display_report(self):
    print("COLLEGE LEVEL CODING FEST : ")
    print(f"Activities : {self.ACTIVITIES_FOR_THE_DAY}")
    print(f"NO.of.teams : {self.NO_OF_TEAMS_PARTICIPATED}")
    print(f"project names : {self.PROJECT_NAMES}")
    print(f"TECHNOLOGIES USED : {self.TECHNOLOGIES_USED}")
    print(f"PPT demo given : {self.PPT_DEMO_GIVEN}")
    print(f"Winner of the day  : {self.WINNER_OF_THE_DAY}")
    print(f"Runner of the day : {self.RUNNER_OF_THE_DAY}")
    print(f"Best performer of the day: {self.BEST_PERFORMER_OF_THE_DAY}")
    print(f"Host of the day: {self.HOST_OF_THE_PROGRAM}")
    print("-----------------------------------------------------------------")
r1=Final_Report("Welcome Ceremony",5,"Project_AI,Project_DS","Python",'YES','Team_A','Team_C','Nani','Akhil')    
r2=Final_Report("Workshop on Python_WEB_DEV",7,"Project_Python,Project_DS","Python,Django",'YES','Team_B','Team_E','Krishna','Jagadeesh')   
r3=Final_Report("Coding_Challenge,Teams_Interactions",10,"Project_AI,Project_DS","Python,HTML",'YES','Team_Z','Team_Y','Bhargavi','Teenu')   
r4=Final_Report("Team_Presentations,Transition_Stage",12,"Project_B,Project_D","Python,Flask",'YES','Team_X','Team_W','Samhitha','Pretty')   
r5=Final_Report("Final_Challenge,Rectifying",15,"Project_I,Project_S","Python,JS",'YES','Team_L','Team_M','Ganesh','Maharshi')   
r6=Final_Report("Closing_Ceremony,Prizes_Distributions",15,"Project_C,Project_F","Python,Pyramid",'YES','Team_D','Team_F','Rehaman','Yogya')   
Display_report(r1)
Display_report(r2)
Display_report(r3)
Display_report(r4)
Display_report(r5)
Display_report(r6)
