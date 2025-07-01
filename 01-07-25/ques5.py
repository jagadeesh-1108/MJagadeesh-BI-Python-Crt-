#write a py program to check whether the user entered string is a panagram or not 
Str=input("Enter the String:").upper()
Str=Str.replace(" ",'')
print(f"User Entered String: {Str}")
Str=sorted(set(Str))
Str=''.join(Str)
if Str == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
         print("Panagram")
else:
    print("Not a Pangaram")