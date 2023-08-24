from Bio import SeqIO
import os
import subprocess

def CallRNAfold(filename):
    directory = 'C:\\Program Files (x86)\\ViennaRNA Package\\'
    open("output.txt","w").close()
    if os.path.exists("temp_output.fold"):
        os.remove("temp_output.fold") #deletes original file
    print(os.getcwd())
    subprocess.run([directory + "RNAfold.exe", "-i", filename, "--outfile=temp_output.fold"]) #predicts the hairpins
    output=open("temp_output.fold","r").read() #extracts the date
    #print(output)
    o1=output.split("\n")
    o1[2]=o1[2][:-10]
    #o1[2] = o1[2].split("(-")[0]  # remove the deltaG value from the end
    [print(x) for x in o1 if x.endswith(")")]

    o2=[float(x.split(")")[-2].split("(")[-1]) for x in o1 if x.endswith(")")]
    print(o2)
    return o2,o1




if __name__=="__main__":
    o1=CallRNAfold("example2.fasta")[1]
    Seq=o1[1]
    DBN=o1[2]
    splitSequences=[]
    openSequence=dict()
    curlvl=0
    for pos in range(len(DBN)):
        curChar=DBN[pos]
        if (curChar=="("):
            if (openSequence.__contains__(curlvl)):
                openSequence[curlvl]+="/"
            curlvl+=1

        if (curChar=="."):
            if (openSequence.__contains__(curlvl)):
                openSequence[curlvl]+=Seq[pos]
            else: openSequence[curlvl]=Seq[pos]

        if (curChar==")"):
            curlvl-=1
            for lvl in [x for x in openSequence.keys()]:
                if (lvl>curlvl):
                    splitSequences.append( (lvl, openSequence[lvl]) )
                    del openSequence[lvl]
    for k, v in openSequence.items():
        splitSequences.append((k, v))
    print(splitSequences)
