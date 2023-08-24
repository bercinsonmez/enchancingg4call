f= open("sequence.fasta")
seq=""

for line in f:
    if line[0]== ">":  # ya da if line.startswith(">"): de diyebiliriz
        continue
    seq += line      # ya da seq+=line.strip("\n") ya da seq+=line.replace(" ","").strip("\n")

print(seq)
