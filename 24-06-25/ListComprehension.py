'''list comprehension - cretae a new list from an iterable object that statsify given condition 
syn:- 
new_list =[expression for item in iterable_object if_statement]
there can be zero or more if statements
there can be one or more for loops
EX:-
list1=[i+1 for i in range(20)]
list2=[i for i in range(20) if i%2==0]
list3=[i for i in range(11) if i%2==0 if i%3==0](nested if statement i%3==0)'''

Num=[]
for i in range(1,11):
    Num.append(i)
print(Num)
#Implementing Same using List Comprehenssion
# New_List=[expression for item in Iteration_object if_statement]
New=[i for i in range(1,11)]
print(New)    