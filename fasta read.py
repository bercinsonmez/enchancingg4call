from Bio import SeqIO

# Replace "example.fasta.fasta" with the path to your FASTA file
fasta_file = "../thesis/example.fasta"

try:
    # Use SeqIO.parse to read the file and return a generator of SeqRecord objects
    records = SeqIO.parse(fasta_file, "fasta")

    # Loop through each record in the generator and print the header and sequence
    for record in records:
        print("Header:", record.id)
        print("Sequence:", record.seq)

except Exception as e:
    print("Error:", e)


