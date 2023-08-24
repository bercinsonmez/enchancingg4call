# The Align function currently performs pairwise alignment using Needleman-Wunsch algorithm.
# You are asked to change this algorithm so it will be using Smith-Waterman algorithm instead.
# The Needleman-Wunsch and Smith-Waterman algorithms are very close in the way they work.
# Both are designed to calculate the pairwise alignment between two sequences

#difference in SmithWaterman vs NeedlmanWunsch,
# 1. the matrix in SmithWaterman  does not contain any value below zero. Any number below zero is replaced with zero in Smithwaterman Alignment during construction of the matrix.
# 2. the final score is calcualted from the maximum value in the matrix in Smithwaterman Alignment method, instead of the value at the bottom right of the matrix.


import numpy as np

def Align(seq1,seq2,match=1,mismatch=-1,gap=-2):

    n=len(seq1)+1
    m=len(seq2)+1
    D=np.zeros((n,m))

    def s_Function(x,y):
        if seq1[x]==seq2[y]:
            return match
        else:
            return mismatch

    def Recursion_Function(x, y):
        horizontal = D[x, y - 1] + gap
        vertical = D[x - 1, y] + gap
        diagonal = D[x - 1, y - 1] + s_Function(x - 1, y - 1)
        return max(horizontal,vertical,diagonal)

    for i in range(1,n):
        D[i,0]=gap*i
    for j in range(1,m):
        D[0,j]=gap*j

    for i in range(1,n):
        for j in range(1,m):
            D[i,j]=Recursion_Function(i,j)
    print("alignment matrix:\n",D)
    print("alignment score:",np.max(D))


sequence1="GCTAGCTAGATCG" #example.fasta
sequence2="GCTAGCTATCG" #example.fasta
Align(sequence1,sequence2) #example.fasta

