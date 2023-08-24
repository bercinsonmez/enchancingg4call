# import random
#
# nucleotides=["A","G","C","T"]
#
# ecoli_seq=""
# f=open("e.coli.fasta","r")
# for line in f.readlines():
#     if line.startswith(">"):
#         continue
#     ecoli_seq+=line.strip("\n")
#
#
#
# seq=  "".join( [ nucleotides[ random.randint(0,3) ] for x in range(100) ] )

# burçinin yaptığı

# K-mer / (motif search) tries to find repetitive sequences in DNA or protein sequences
# Pairwise Alignment Algorithm / (comparison) try yo compare 2 sequences to see how close or how different they are

# How many times any combination of 8 nucleotides has repeated in a given sequence? K-mer
import random
from itertools import product

import random
nucleotides=["A","G","C","T"]

ecoli_seq = ""
f=open("ecoli.fasta","r")
for line in f.readlines():
    if line.startswith(">"):
        continue
    ecoli_seq += line.strip("\n")

ecoli_seq = ecoli_seq[ :10000]

random_seq = "".join([nucleotides[random.randint(0,3)] for x in range(4641652)])

# def eightmer_permutations():
#     results = []
#     kmer = ""
#     for base in nucleotides:
#         kmer += base
#         for base2 in nucleotides:
#             kmer += base2
#             results.append(kmer)
#             kmer = kmer [ :-1]
#         kmer =""
#     return results

combs = ["".join(x) for x in product(nucleotides, repeat=8)]

ecoli_kmers = dict()
for x in combs:
    print("\b\b\b\b\b\b\b\b"+x,end="")
    ecoli_kmers[x] = ecoli_seq.count(x)

mylist = list(ecoli_kmers.items())
mylist.sort(key = lambda x:x[1])

import matplotlib.pyplot as plt
plt.hist(ecoli_kmers.values())

