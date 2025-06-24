'''Quick Sort - pivot element along with divide and conqure rule 
comprehensions - It conatains very compact code usually a single statement that perform a task 
list comprehension - cretae a new list from an iterable object that statsify given condition 
syn:- 
new_list =[expression for item in iterable_object if_statementy]
there can be zero or more if statements
there can be one or more for loops
EX:-
list1=[i+1 for i in range(20)]
list2=[i for i in range(20) if i%2==0]
list3=[i for i in range(11) if i%2==0 if i%3==0](nested if statement i%3==0)
set comprehension
dictionary comprehension 
'''
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x == pivot]
    right= [x for x in arr if x>pivot]
    return quick_sort(left)+ middle +quick_sort(right)
print(quick_sort([5,3,8,6,2]))

