import os
import subprocess
import re


def CallRNAfold(filename):
    directory = 'C:\\Program Files (x86)\\ViennaRNA Package\\'
    open("output.txt", "w").close()
    if os.path.exists("temp_output.fold"):
        os.remove("temp_output.fold")  # deletes original file
    print(os.getcwd())

    # Run RNAfold and capture output
    subprocess.run([os.path.join(directory, "RNAfold.exe"), "--noconv", "-i", filename, "--outfile=temp_output.fold"])

    # Read and process output
    output = open("temp_output.fold", "r").read()
    rows = output.split("\n")
    description = rows[2]
    print(description)

    # Print lines that end with ")"
    [print(x) for x in rows if x.endswith(")")]

    # Uncomment and modify lines as needed
    # rows[2] = rows[2][:-10]
    # o1[2] = o1[2].split("(-")[0]

    # Initialize an empty list for scores
    score = []
    # Extract scores from lines ending with ")"
    for x in rows:
        if x.endswith(")"):
            score_part = x.split(")")[-2].split("(")[-1]
            score.append(float(score_part))

    print("Scores:", score)

    return score, rows


if __name__ == "__main__":
    # Capture both score and rows from CallRNAfold
    scores, o1 = CallRNAfold("example.fasta")
    Seq = o1[1]
    DBN = o1[2]

    # Rest of your code (splitSequences, splitSeqPos, etc.)
    # ...
