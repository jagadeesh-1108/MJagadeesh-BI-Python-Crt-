#Variable shawdowing - Dominance of local variable over global variable 
Greet="Good Morning"
def Display():
    Greet = "Good Afternoon"
    print(Greet)
Display()    
print(Greet)