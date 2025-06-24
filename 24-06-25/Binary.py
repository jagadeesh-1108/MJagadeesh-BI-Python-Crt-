#Binary Search  here A means  Pivot element
def Binary_search(arr,target,A=0):
    if(len(arr)==0):
        print("Array does not exst")
        return -1 
    
    mid=len(arr)//2
    if target==arr[mid]:
        print(f"Element found at {mid+A} index")
    else:
        if target<arr[mid]:
            return Binary_search(arr[:mid],target,A)
        elif target >arr[mid]:
            return Binary_search(arr[mid+1:],target,A+mid+1) 
        else:
                print("Element does not exist")
output=Binary_search([1,2,3,4,5],4)          
      



