#Real time problem on gene expression analyser
size=int(input("Enter the size: "))
List=[]
for i in range(size):
    temp = float(input())
    List.append(temp)
for i in List:    
    if i < 5:
        print("Underexpressed")
    elif i>=5 and i<=15:
        print("Normal")
    elif i>15:
        print("Overexpressed")
print(List)   
