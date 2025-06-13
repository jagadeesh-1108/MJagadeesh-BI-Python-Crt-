#real time GC content calculator
seq=input("enter the seq: ")
dna=seq
GC=dna.count('G')+dna.count('C')/len(dna)*100
if GC >60:
    print("High GC")
elif GC>=40 and GC<=60:
    print("Moderate GC")
elif GC<=40:
    print("Low GC")         

print(GC)

