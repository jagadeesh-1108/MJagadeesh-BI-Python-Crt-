'''
 Write a python program to print square numbers from 1 to n
 Write a python program to print square numbers from n to 1
 Write a python program to print prime numbers from 1 to n
 Write a python program to print prime numbers from n to 1
'''
N=int(input("Enter the square of a number : "))
def Square(N):
    if N==0:
        return 
    Square(N-1)
    print(N*N)
    
print(Square(N))
print("---------------------")