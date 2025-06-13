#write a python program a string input from theuser and print the count of 
#1)Uppercase_Vowels
#2)Lowercase_Vowels
#3)Uppercase_Consonants
#4)lowercase_consonants
str=input("Enter the input : ")
Uppercase_Vowels=0
Lowercase_Vowels=0
Uppercase_Consonants=0
Lowercase_Consonants=0
for ch in str:
    if(ch>='A' and ch<='Z'):
        if ch in 'AEIOU':
            Uppercase_Vowels+=1
        else:
            Uppercase_Consonants+=1
    elif(ch>='a' and ch<='z'):
        if ch in 'aeiou':
            Lowercase_Vowels+=1
        else:
            Lowercase_Consonants+=1
print(f"Count of Upper case  Vowels : {Uppercase_Vowels}")
print(f"Count of Lower case Vowels : {Lowercase_Vowels}")
print(f"Count of Upper case Consonants : {Uppercase_Consonants}")
print(f"Count of Lower case Consonants : {Lowercase_Consonants}")



