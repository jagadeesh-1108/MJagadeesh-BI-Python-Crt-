#write a py program to declare a list of words and declare a tuple of words and map it to print the combined words
n=int(input("Enter the no.of words that you would like to find: "))
list=['Marker','Water','Bread','Black','Class']
tuple=('Pen','Bottle','Jam','Board','Room')
i=1
while(i<=n):

    Word=input("Enter the Word: ")
    index=list.index(Word)
    print(f"{Word}-{tuple[index]}")
    i+=1
    
