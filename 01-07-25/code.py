#Backtracking - solving the solution in many possiblities with the help of recurssion 
# writa a py program to read the len of the string as input from the user and print all binary of len
def genearte_binary_no_backtrack(n):
    result='0' * n
    print(result)
genearte_binary_no_backtrack(3)    
#with Backtracking
print("With Backtracking")
def generate_binary_backtrack(n,current=""):
    if len(current) == n:
        print(current)
        return
    #choose 0
    generate_binary_backtrack(n, current + '0')
    #choose 1 
    generate_binary_backtrack(n, current + '1')

generate_binary_backtrack(3)    