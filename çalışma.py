#BEN 519 Homework1 / Burçin Dersu Açıkgöz
seq=input("Please enter the sequence: ").upper()
DNAbases={"A","G","T","C"}
RNAbases={"A","G","U","C"}
seq_set=set(seq) #önce userdan sekansı alıyoruz, ama setlerde birer tane aynı seyden olabilceği için set yapıyoruz
if seq_set.issubset(DNAbases):
    print("That is a DNA sequence")
elif seq_set.issubset(RNAbases):
    print("That is a RNA sequence")
else:
    print("Sequence cannot be recognized")