#SETS
Set={10,20,30,40}
Set2={0,70,80}
print(Set)
print(type(Set))
print(10 in Set)#Membership operator 
Set.add(50)#addition
print(Set)
Set1 ={60}
Set.update(Set1)#updating
print(Set)
Set.remove(10)#removing
print(Set)
Set.discard(100)#discarding without raising error 
print(Set)
Set.clear#clear
print(Set)
print(Set | Set2)#Union
print(Set & Set2)#intersection
print(Set ^ Set2)#symmetric difference 
print(Set - Set2)#Difference
Set.union(Set2)
Set.difference(Set2)
Set.issubset(Set2)
Set.issuperset(Set2)
print(Set) 

