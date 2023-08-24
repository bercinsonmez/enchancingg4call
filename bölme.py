from Bio import SeqIO
window_size=30
filename = "example2.fasta"

with open("temp_segmented.txt", "w") as output_file:
    for record in SeqIO.parse(filename, "fasta"):
        sequence = str(record.seq)
        segments = []
        for i in range(len(sequence) - window_size):
            segment = sequence[i:i+window_size+1]
            segments.append(segment)
    #print(segments)
#with open("output.txt", "w") as output_file:
    #for i in range(len(sequence)):
        #output_file.write(sequence[i] + "\n")
        for segment in segments:
            output_file.write(f'{segment}\n')
