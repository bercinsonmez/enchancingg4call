# Write a code that asks the user for a sequence and returns sub-sequence
# between the first “ATG” (start codon) until
# the first “TAA” (stop codon) in a sequence given by the user.
# input = TCGTAGGCATCG ATGCGATGCTAA CGCGCAGCTTAA
# output= ATGCGATGCTAA

raw_sequence=input("Please enter the sequence>>> ")
raw_sequence=raw_sequence.strip("\n 53'") #So I can have only the main sequence
print("Your sequence is", raw_sequence)
pos_1st_ATG=raw_sequence.find("ATG")

if pos_1st_ATG == -1:
    print("There is no open reading frame")
    exit()
print("First ATG is at", pos_1st_ATG)
pro_seq=raw_sequence[pos_1st_ATG: ]
print("Processed sequence:", pro_seq)

pos_1st_TAA_after_ATG=pro_seq.find("TAA")
if pos_1st_TAA_after_ATG == -1:
    print("Cannot find the TAA after the first ATG. There is no full open reading frame.")
    exit()
print("Position of the first TAA in the processed sequence is", pos_1st_TAA_after_ATG)
pro_seq=pro_seq[ :pos_1st_TAA_after_ATG]
print("The sequence between the first ATG and the first TAA is")

