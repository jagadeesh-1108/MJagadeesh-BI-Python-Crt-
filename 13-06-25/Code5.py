#multilplication of a table 
def table(num):
    for i in range(10):
        print(f"{num}*{i+1}=",num*(i+1))
num=int(input("Enter the num: "))
table(num)           
