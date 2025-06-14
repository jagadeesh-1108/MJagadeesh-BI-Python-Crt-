#keyword variable length argument
def add(**num):
    z= num['a']+num['b']+num['c']
    print(z)
add(a=5,b=2,c=4)    