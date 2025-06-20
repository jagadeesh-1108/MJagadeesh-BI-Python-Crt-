N=int(input("Enter the square of a number : "))
def Square(N):
    if N==0:
        return 
    print(N*N)
    Square(N-1)
print(Square(N))
