#palindrome
dna=input("Enter the seq: ")
print(True if dna.replace('A','T') and dna.replace('C','G')else False)
