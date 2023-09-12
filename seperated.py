from Bio import SeqIO

filename = "../thesis/example.fasta"

with open("output.txt", "w") as output_file:
    for record in SeqIO.parse(filename, "fasta"):
        sequence = str(record.seq)
        segments = []
        for i in range(len(sequence) - 15):
            segment = sequence[i:i+16]
            segments.append(segment)
        for segment in segments:
            output_file.write(f'"{segment}"\n')
