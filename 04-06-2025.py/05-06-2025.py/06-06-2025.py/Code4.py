#write a py program to create a tuple of programming languages beging length of 15 and find the maximum element , min element  and prnt the sorted tuple and print the reversed tuple 
#write a py program to create a tuple of names and print the original tuple and print the names which has length of 5 from the tuple 
#1)ans
Tuple=('HTML','CSS','JS','C++','PYTHON','JAVA','A','B','C','D','PERL','R','RUBY','GO-LANG','ANGULAR JS')
print("Max of Tuple: ",max(Tuple))
print("Min of Tuple: ",min(Tuple))
print("Sorted of Tuple : ", sorted(Tuple))

print("Reversed of Tuple : ",tuple(reversed(Tuple)))
#2)ans
Tuple=('ABC','BCA','BBA','BCADEFGH','ABCDEF','JAGADEESH')
print(Tuple)
for i in range(len(Tuple)):
    if (len(Tuple[i])>=5):
        print(
            (Tuple[i]))


