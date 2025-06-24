#linear search - searching occurs linearly   and It works on both sorted and unsorted data.
# Time- O(n) , Space - O(1)
def LinearSearch(key,arr,len):
    count=0
    for i in range(len):
        count+=1
        print(f"{count} Iteration")
        if arr[i]==key:
            print(f"Element Found at index {i}")
            break
    else:
        print(f"Elemnet Not Found")
res=LinearSearch(8,[5,6,2,3,4,1,0,7,8,9],10)            
