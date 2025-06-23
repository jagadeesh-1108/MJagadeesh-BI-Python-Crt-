#str patterns 
#normal order
'''
str=input("enter the str: ")
for i in range(len(str)):
    for j in range(len(str)):
        print(f"{str[j]} ",end="")
    print()
    
#reverse order 
str=input("enter the str: ")
Length=len(str)
for i in range(Length):
    for j in range(i+1):
        print(f"{str[Length-j-1]} ",end="")
    print()
#print the following pattern 
#n
#aa
#nnn
#iiii
str=input("enter the str: ")
Length=len(str)
for i in range(Length):
    for j in range(i+1):
        print(f"{str[i]} ",end="")
    print()

#hallow str
str=input("enter the str: ")
length=len(str)
for i in range(length):
  for j in range(length):
    if(i==0 or i==length-1 or j==0 or j==length-1):
      #print('*',end=' ') 
      print(f"{str[j]}",end=" ")
    else:
       print(' ',end=' ')
  print()
   
# + str 
st = input("Enter the name: ")
for i in range(len(st)):
    for j in range(len(st)):
        if(j==(len(st)-1)//2):
            print(st[i],end=" ")
        elif(i==(len(st)-1)//2):
            print(st[j],end=" ")
        else:
            print(" ",end=" ")
    print()
num = int(input("Enter the number: "))
k=1
for i in range(num):
    for j in range(i+1):
        print(k*k,end=" ")
        k+=1
    print()'''
n=int(input("Enter the value: "))
for i in range(n):
   print(" "*(n-i-1)+'*'*(2*i+1))
for i in range(n-1,0,-1):
    print(" "*(n-i)+'*'*(2*i-1)) 
