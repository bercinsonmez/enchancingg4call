RNAseq="CGUAGUGCAUGACGUACCC"

RNAtoDNAdict={"A":"A","G":"G","C":"C","U":"T"}

DNAseq=""

for x in RNAseq:
    temp=RNAtoDNAdict[x]
    print( DNAseq )
    DNAseq+=temp

print(DNAseq)



print("bitti")
