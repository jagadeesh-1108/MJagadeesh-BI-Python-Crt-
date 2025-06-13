#Write a py program to read the list of chars from the user converted it in to a word and print it 
Size=int(input("Enter the length of list: "))
Char_List=[]
for i in range(Size):
    ch=input("Enter the characters : ")
    Char_List.append(ch)
print(Char_List)
str="".join(Char_List)
print(str)   