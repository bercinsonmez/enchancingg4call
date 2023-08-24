# f=open(subject.fasta)
# # sequence=input("Please enter the sequence")
# # sequence=sequence.strip("\n 53'")
# #
# # for line in f:
# #
# # Tm=round(64.9 +41*(G+C-16.4)/(A+T+G+C))
# # print(report)
# # if ( Tm < 65):
# #     print( Tm is below 65)
# # elif ( Tm > 55):
# #     print("Tm is above 55")

#quiz2_erokay_gürz
seq = input("enter a sequence\n").upper().strip(" 53'-")

f = open("subject.fasta")
sub = ""

for line in f:
    if line[0] == ">": # skips the first line of definition
        continue
    sub += line.replace(" ","").strip("\n") # removes the indents and gaps while typing

if seq in sub:
    print("\nEntered sequence is in the subject.fasta\n")
else:
    print("\nEntered sequence could not be found in subject.fasta\n")

# Tm= 64.9 +41*(#G+#C-16.4)/(#A+#T+#G+#C)

tot = len(seq)
a = seq.count("A")
g = seq.count("G")
c = seq.count("C")
t = seq.count("T")

tm = 64.9 +(41*(g+c-16.4)/(a+t+g+c))
print("Sequence Tm is",tm)
if tm > 65:
    print("and above 65 oC\n")
elif tm < 55:
    print("and below 55 oC\n")
else:
    print("and between 55 and 65 oC\n")

gc = (g+c)/tot*100
print("Sequence GC concent is",gc)
if gc > 60:
    print("and above 60%\n")
elif tm < 50:
    print("and below 50%\n")
else:
    print("and between 50% and 60%\n")


