import sys, subprocess, os
from Bio import SeqIO
import matplotlib.pyplot as plt
windowSize=90
inputFile = "example2.fasta"


def SegmentFile(filename, window_size):
    with open("temp_segmented.txt", "w") as output_file:
        for record in SeqIO.parse(filename, "fasta"):
            sequence = str(record.seq)
            segments = []
            for i in range(len(sequence) - window_size):
                segment = sequence[i:i + window_size + 1]
                segments.append(segment)
            # print(segments)
            # with open("output.txt", "w") as output_file:
            # for i in range(len(sequence)):
            # output_file.write(sequence[i] + "\n")
            for segment in segments:
                output_file.write(f'{segment}\n')

def CallRNAfold():
    directory = 'C:\\Program Files (x86)\\ViennaRNA Package\\'
    open("output.txt","w").close()
    if os.path.exists("temp_output.fold"):
        os.remove("temp_output.fold") #deletes original file
    print(os.getcwd())
    subprocess.run([directory + "RNAfold.exe", "-i", "temp_segmented.txt", "--outfile=temp_output.fold"]) #predicts the hairpins
    output=open("temp_output.fold","r").read() #extracts the date
    #print(output)
    o1=output.split("\n")
    [print(x) for x in o1 if x.endswith(")")]
    o2=[float(x.split(")")[-2].split("(")[-1]) for x in o1 if x.endswith(")")]
    print(o2)
    return o2

if __name__=="__main__":
    pass
    SegmentFile(inputFile,windowSize)
    print("calling RNAfold...")
    profile=CallRNAfold()
    profile=[x/windowSize for x in profile]
    print("RNAfold complete.")
    plt.plot(profile)
    plt.show()