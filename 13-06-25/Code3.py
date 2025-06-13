#to check weather the user given num is a prime num or not using functions(return)
def Is_prime(Num):
    count = 0
    for i in range(1,Num+1):
        if (Num % i==0):
            count+=1
    if count==2:
        return "prime"
    else:
        return "Not a prime"
Num=int(input("Enter the num: "))
print(Is_prime(Num))