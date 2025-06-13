#write a py program tp read mail id as input from the user name and organisation name based on mail id (first : name@orgname  org.com )
mail_id=input("Enter the mail_id : ")
List=mail_id.split('@')
print(f"User Name : {List[0]}")
Org=List[1]
List=Org.split('.')
print(f" Org Name : {List[0]}")
