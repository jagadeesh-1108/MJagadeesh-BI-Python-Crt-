'''
problem statement: given DNA sequences ,  calculate the GC content of each and plot it as a histogram
'''
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "GeneID": [f"G{i}" for i in range(1, 16)],
    "Sequence": [
        "ATGCGTAA", "GGGCGCGT", "ATATATAT", "CGCGATAT",
        "GCGTGCAT", "TTATTATA", "CCGGCCGG", "GATCGATC",
        "TATATATA", "GCGCGCGC", "ATGCATGC", "GGATCCGG",
        "CATCATGG", "TGCATGCA", "GGTACCGA"
    ]
}
df = pd.DataFrame(data)
def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100
df["GC_Content"] = df["Sequence"].apply(gc_content)
print(df)
plt.figure(figsize=(8, 5))
plt.hist(df["GC_Content"], bins=10, color="skyblue", edgecolor="black")
plt.title("GC Content Histogram")
plt.xlabel("GC Content (%)")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()