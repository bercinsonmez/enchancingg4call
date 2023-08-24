seq=input("enter the sequence\n").upper().strip("53'-")
f= open ("finalsequence.fasta")
sub= ""

for line in f:
    if line[0] == ">" :
        continue
        sub+=line.replace(" ","").strip("\n")

if seq in sub:
    print("\nentered sequence is in the finalsequence.fasta\n")
else:
    print("\nentered sequence could not be found in finalsequence.fasta\n")
