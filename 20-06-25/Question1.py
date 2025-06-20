#write a py program to print natural numbers count
N=int(input("Enter the Value of n :"))
i=0
def NaturalNum(N,i):
    i=i+1
    if N==0:
        return
    NaturalNum(N-1,i)
    print(f"{i} Method Call")
NaturalNum(N,i)