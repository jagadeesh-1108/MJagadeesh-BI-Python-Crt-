#write a py program to check whether the user enters 2 string are  anagrams or not
Str1=input("Enter the First String:  ").lower()
Str2=input("Enter the Second String:  ").lower()
print(f"First String: {Str1}")
print(f"Second String : {Str2}")
Str1=Str1.replace(" ",'')
Str2=Str2.replace(" ",'')
if len(Str1) == len(Str2):
    if sorted(Str1)==sorted(Str2):
        print("Anagram")
else:
    print("Not a Anagram")
