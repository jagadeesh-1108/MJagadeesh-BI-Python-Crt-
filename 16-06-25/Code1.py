#write a python program to check weather the number is positive or negative using lambda functions
res=lambda num:print('+Ve')if(num>0) else (print ('ZERO') if(num==0) else print('-VE'))
res(2)
#---------------------------
def Positive(Num):
    if(Num>0):
        print("+Ve")
    else:
        if(Num==0):
            print("Zero")
        else:
            print("-Ve") 
Positive(0)                   