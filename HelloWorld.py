



seq=input("Enter the sequence").upper()
DNAbases={"A","T","C","G"}
RNAbases={"A","U","C","G"}
seq_set=set(seq)
if seq_set.issubset(DNAbases):
    print("Your sequence is a DNA sequence")
elif seq_set.issubset(RNAbases):
    print("Your sequence is a RNAbases")
else:
    print("Sequence cannot be defined")

