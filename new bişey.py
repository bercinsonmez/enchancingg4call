import numpy as np
from time import sleep
def S( x,y ):
    if seq[x]==seq[y]:
        return match
    else:
        return mismatch


seq1="AACG"
seq2="AAtCG"
gap=-2
mismatch=-1
match=1

n=len(seq1)+1
m=len(seq2)+1
D= np.zeros( (n,m) )
for i in range(1,n):
    D[i,0]=gap*i
for j in range(1,m):
    D[0,j]=gap*j

for i in range(1,n):
    for j in range(1,m):
        horizontal
        # D[i,j]=3.14
        print(D)
