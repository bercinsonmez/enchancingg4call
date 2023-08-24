
#
# D     A	A	C	 G
#    0  -2	-4	-6	-8
# A	-2	 1	-1	-3	-5
# A	-4	-1	 2	 0	-2
# T	-6	-3	 0	 1	-1
# C	-8	-5	-2	 1	 0
# G	-10	-7	-4	-1	 2



import numpy as np
from time import sleep

seq1 = "AATCG"
seq2 = "AACG"

def S(x, y):
    if seq1[x] == seq2[y]:
        return match
    else:
        return mismatch

gap = -2
mismatch = -1
match = 1

n = len(seq1)+1
m = len(seq2)+1

D = np.zeros((n, m))

for i in range(1, n):
    D[i, 0] = gap*i
for j in range(1, m):
    D[0, j] = gap*j

for i in range(1, n):
    for j in range(1, m):
        horizontal = D[i, j-1]+gap
        vertical = D[i-1, j]+gap
        diagonal = D[i-1, j-1] + S(i-1, j-1)
        D[i, j] = max(horizontal, vertical,diagonal)
        # print(D)
        # sleep(1)

print(seq1, "and", seq2, "has a similarity of", D[i, j] )

# Biopython;
# from Bio import pairwise2
# pairwise2.align.globalms(seq1, seq2, match = 1, mismatch = -1, open = -2, extend = -2 )