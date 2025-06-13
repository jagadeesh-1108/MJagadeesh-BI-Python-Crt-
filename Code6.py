#DNA to RNA conversion
dna=input("Enter dna seq: ")
for i in dna:
    rna=dna.replace('T','U') 
print(rna)