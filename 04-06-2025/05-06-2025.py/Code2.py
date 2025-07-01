'''
write a python program to:
1.Add Confiremed guest to al list.
2.Remove the Guest who can Cancles.
3.Check if a friend is on the list.
4.sort and print the final guest list.

'''
Guest_List=[]
while(True):
    print("*********MENU*********")
    print("1.Add the Guest")
    print("2.Remove the Guest who can Cancles")
    print("3.Check if a Guest is Attending the party or not")
    print("4.Veiw  the Final  Guest List")
    print("5.Exit")
    print("----------------")
    Choice=int(input("Enter Your Choice: "))
    if(Choice >=1 and Choice<=5):
        if(Choice==1):
            GuestName=input("Enter the Guest Name: ")
            Guest_List.append(GuestName)
            print(f"{GuestName} is Added to Guest List....!")
        elif(Choice==2):
            CancelledGuest=input("Enter the Cancelled Guest Name: ")
            if CancelledGuest in Guest_List:
                Guest_List.remove(CancelledGuest)
                print(f"{CancelledGuest} is Removed from the Guest_List...!")
            else:
              print(f"{CancelledGuest} is not in the Guest LIST")
        elif(Choice==3):
            CheckGuest=input("Enter the Guest Name to Check: ")
            if CheckGuest in Guest_List:
                print(f"{CheckGuest} is Attending the party....!")
            else:
                print(f"{CheckGuest} is not Attending the party....!")
        elif(Choice==4):
            if(len(Guest_List)==0):
                print("Guest List is Empty....!")
            else:
                Guest_List.sort()
                print("Hurray Here's Your Final Guest List")
                print("Guest_List")
        else:
            print("Enjoy the party....!")
            break
else:

    print("In-valid Input")        



