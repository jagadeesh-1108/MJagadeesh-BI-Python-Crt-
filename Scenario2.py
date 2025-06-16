#college level codding fest
class Final_Report():
    def __init__(self,Activities,No_of_teams_participated,project_names,technologies_used,ppt_demo_given,winner_of_the_day,runner_of_the_day,best_performer_of_the_day,host_of_program):
        self.ACTIVITIES_FOR_THE_DAY=Activities
        self.NO_OF_TEAMS_PARTICIPATED=No_of_teams_participated
        self.PROJECT_NAMES=project_names
        self.TECHNOLOGIES_USED=technologies_used
        self.PPT_DEMO_GIVEN=ppt_demo_given
        self.WINNER_OF_THE_DAY=winner_of_the_day
        self.RUNNER_OF_THE_DAY=runner_of_the_day
        self.BEST_PERFROMER_OF_THE_DAY=best_performer_of_the_day
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
    print(f"Host of the day: {self.HOST_OF_THE_DAY}")
F1=Final_Report("TECHNICAL_ROUNDS",5,"")    
