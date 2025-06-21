#Write a python program to print square numbers from n to 1
N=int(input("Enter the square of a number : "))
def Square(N):
    if N>=1:
        print(N*N)
        Square(N-1)
Square(N)
