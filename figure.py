import sys
import subprocess
import os
from Bio import SeqIO
import matplotlib.pyplot as plt

def SegmentFile(filename, window_size):
    with open("temp_segmented.txt", "w") as output_file:
        for record in SeqIO.parse(filename, "fasta"):
            sequence = str(record.seq)
            segments = []
            for i in range(len(sequence) - window_size):
                segment = sequence[i:i + window_size + 1]
                segments.append(segment)
            for segment in segments:
                output_file.write(f'{segment}\n')

def CallRNAfold():
    directory = 'C:\\Program Files (x86)\\ViennaRNA Package\\'
    open("output.txt", "w").close()
    if os.path.exists("temp_output.fold"):
        os.remove("temp_output.fold")  # deletes original file
    subprocess.run([directory + "RNAfold.exe", "-i", "temp_segmented.txt", "--outfile=temp_output.fold"])  # predicts the hairpins
    output = open("temp_output.fold", "r").read()  # extracts the date
    o1 = output.split("\n")
    o2 = [float(x.split(")")[-2].split("(")[-1]) for x in o1 if x.endswith(")")]
    return o2

def plot_profile(window_sizes):
    inputFile = "example2.fasta"
    plt.figure()
    for window_size in window_sizes:
        SegmentFile(inputFile, window_size)
        profile = CallRNAfold()
        profile = [x / window_size for x in profile]
        plt.plot(profile, label=f'Window size: {window_size}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    window_sizes = [30, 50, 90]  # List of window sizes to plot
    plot_profile(window_sizes)
