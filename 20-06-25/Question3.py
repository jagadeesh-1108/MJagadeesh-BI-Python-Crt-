#write a py program to print the natural numbers from n to 1
N=int(input("Natural Numbers from N to 1: "))
def NaturalNum(N):
    if 0==N:
        return
    print(N)
    NaturalNum(N-1)
NaturalNum(N)    