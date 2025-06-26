arr = list((input("Enter the list of elements (space-separated): ").split()))
print(f'Original arr: {arr}')
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(f'Sorted arr: {arr}')
