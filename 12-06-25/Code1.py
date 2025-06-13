#Real Time scenario based questions Bioinformatics Domain - DNA 
str=input("Enter the input: ")
count_a=count_T=count_G=count_C=0
for i in str:
    if i in "A":
        count_a+=1
    elif i in "T":
        count_T+=1
    elif i in "G":
        count_G+=1
    elif i in "C":
        count_C+=1
dict={"A":count_a,"T":count_T,"G":count_G,"C":count_C}
print(dict)                




