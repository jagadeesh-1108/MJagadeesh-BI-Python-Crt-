#generate report 
def generate_report(dna,db):
    Count_G=0
    Count_C=0
    if dna in db:
        ID = db[dna]
    for i in dna:
        Count_G = dna.count(i)
        Count_C = dna.count(i)
    GC_Count = (Count_G+Count_C)/len(dna)*100
    if(GC_Count )
#git changes