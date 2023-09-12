# from Bio import SeqIO
import os
import subprocess
import re

def CallRNAfold(filename, temp=37):
    directory = 'C:\\Program Files (x86)\\ViennaRNA Package\\'
    open("output.txt","w").close()
    if os.path.exists("temp_output.fold"):
        os.remove("temp_output.fold") #deletes original file
    print(os.getcwd())

    temp = float(input("Please enter the temp: "))
    subprocess.run([directory + "RNAfold.exe","--noconv", "-i" , filename,"--temp=" +str(temp), "--outfile=temp_output.fold"]) #predicts the hairpins
    output=open("temp_output.fold","r").read() #extracts the date
    #print(output)

    rows=output.split("\n")
    description=rows[2]
    score=float(re.findall("\([ ]?[+-]?[0-9]+\.?[0-9]*\)",rows[2])[-1][1:-1])
    print(score)
    DBN=re.sub("\([ ]?[+-]?[0-9]+\.?[0-9]*\)","",rows[2])
    rows[2]=DBN.strip()
    [print (x) for x in rows]
    # print(rows)
    return score,rows



if __name__ == "__main__":
    scr,o1 = CallRNAfold("../thesis/example.fasta")
    Seq = o1[1]
    DBN = o1[2]
    splitSequences = []
    splitSeqPos = []
    openSequence = dict()
    openSeqPos = dict()
    curlvl = 0
    for pos in range(len(DBN)):
        curChar = DBN[pos]
        if curChar == "(":
            if openSequence.__contains__(curlvl):
                openSequence[curlvl] += "e"

            curlvl += 1

        if curChar == ".":
            if openSequence.__contains__(curlvl):
                openSequence[curlvl] += Seq[pos]
                openSeqPos[curlvl] += [pos]
            else:
                openSequence[curlvl] = Seq[pos]
                openSeqPos[curlvl] = [pos]

        if curChar == ")":
            curlvl -= 1
            for lvl in [x for x in openSequence.keys()]:
                if lvl > curlvl:
                    splitSequences.append((lvl, openSequence[lvl]))
                    splitSeqPos.append((lvl, openSeqPos[lvl]))
                    del openSequence[lvl]
                    del openSeqPos[lvl]

    for k, v in openSequence.items():
        splitSequences.append((k, v))
    for k, v in openSeqPos.items():
        splitSeqPos.append((k, v))
    print(splitSequences)
    print(splitSeqPos)


    temp_value = 37  # Change this value to the desired temperature
    output_filename = "output.fasta"  # Change this to your desired output file name

    # Generate the output FASTA file
    with open(output_filename, "w") as output_file:
        for i, (level, sequence) in enumerate(splitSequences):
            positions = splitSeqPos[i][1]
            description = "Level: {} | Temp: {} | Score: {}".format(level, temp_value,scr)
            output_file.write(">" + description + "\n" + sequence + "\n")


