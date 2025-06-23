#Sorting - bubble sort
'''
arr=[10,20,30,40,50,60,55]
print(f"Original array:{arr}")
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(f"Sorted array:{arr}")     
'''
arr=[10,20,30,40,50,60,55]
print(f"Original array:{arr}")
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            Flag=True
    if Flag == False:
        break
print(arr)    