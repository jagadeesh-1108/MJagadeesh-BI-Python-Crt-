#parameters - Function decleration a,b  and arguments - actual values when we are giving to print
##formal arguments- function definition parameters are called as formal arrguments
#actual arguments - function call arguments are actual arguments
def Display(a,b):
    print(a,b)
Display(10,20)    
#add-x,y are formal arguments, 10,20 are actual arguments
def add(x,y):
    c=x+y
    print(c)
add(10,20)
#types of actual arguments
#positional arguments, key arguments, default arguments, variable arguments, keyword variable length arguments
#positional 
def pw(x,y):
    z = x**y
    print(z)
pw(5,2)   
#keyword arguments
def show(name,age):
    print(name,age)
show(name="nani",age=21)  
#default 
def show(name,age=27):
    print(name,age)
show(name="jagadeesh",age=32)       
