#Time complexity - The Amount of time is required to exceute a programm 
#Space complexity - The memory occupied during the exceution of a program 
#Recursion - A finction call by it's own
'''
def function_name(parameters):
    if base_condition:
        return result
    return function_name(modified_parameters)
print(function_name)'''

def Add_List(n,sum):
    if bool(n):
        sum=sum+n
        return Add_List(n-1,sum)
    return sum
print(Add_List(5,0))

