# write a Python (3+) script that,
#
# 1. asks the user for a sequence
#
# 2. asks the user for a value of k
#
# 3. finds all k-mers in the sequence and prints on the screen

import random
from itertools import product

nucleotides=["A","T","G","C"]
seq=input("please enter the sequence")
k=int(input("enter the value of k"))

random_sequence= "".join([nucleotides[random.randint(0,3)] for x in range(len(seq))])

combs= ["".join(x) for x in product(nucleotides, repeat=k)]

kmers= dict()
for x in combs:
    kmers[x] = seq.count(x)

print(kmers.keys())





