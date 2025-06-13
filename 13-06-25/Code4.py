#multiplication table of 1 to  n
def table(num):
    for i in range(1,num):
        for j in range(1,11):
            print(f"{i}*{j}={i*j}")
num=int(input("Enter the num: "))
table(num)            

