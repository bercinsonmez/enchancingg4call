# Write a piece of python code that accepts a DNA sequence from the user and prints a report. The report should contain
# 1. the sequence with "5'" and "3'" at the beginning and the end,
# 2. the length of the sequence,
# 3. whether the sequence contains the start codon
# example.fasta

sequence = input("Enter the sequence>>> ")

print("===Report===")
print("you have entered the sequence: 5'", sequence, "3'")
print("its length is", len(sequence), "nucleotides")
if "AUG" in sequence:
    print("it contains the start codon.")
else:
    print("it does not contain the start codon.")

print("====END====")
