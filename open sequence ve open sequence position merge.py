from Bio import SeqIO
import os
import subprocess

def CallRNAfold(filename):
    directory = 'C:\\Program Files (x86)\\ViennaRNA Package\\'
    """uses the fasta in the file and returns a tuple of level and looping bases"""
    open("output.txt","w").close()
    if os.path.exists("temp_output.fold"):
        os.remove("temp_output.fold") #deletes original file
    print(os.getcwd())
    subprocess.run([directory + "RNAfold.exe", "-i", filename, "--outfile=temp_output.fold"]) #predicts the hairpins
    output=open("temp_output.fold","r").read() #extracts the date
    #print(output)
    o1=output.split("\n")
    # o1[2]=o1[2][:-10]
    open_parenthesis_index = o1[2].rfind(" ")  # find the index of the first open parenthesis
    if open_parenthesis_index != -1:
        o1[2] = o1[2][:open_parenthesis_index]  # slice the string up to the first open parenthesis
    #o1[2] = o1[2].split("(-")[0]  # remove the deltaG value from the end
    [print(x) for x in o1 if x.endswith(")")] #

    o2=[float(x.split(")")[-2].split("(")[-1]) for x in o1 if x.endswith(")")]
    print(o2)
    return o2,o1


if __name__=="__main__":
    o1=CallRNAfold("example2.fasta")[1]
    Seq=o1[1]
    DBN=o1[2]
    splitSequences=[]
    splitSeqPos=[]
    openSequence=dict()
    openSeqPos=dict()
    curlvl=0
    for pos in range(len(DBN)):
        curChar=DBN[pos]
        if (curChar=="("):
            if (openSequence.__contains__(curlvl)):
                openSequence[curlvl]+="/"
                openSeqPos[curlvl] += "/"

            curlvl+=1

        if (curChar=="."):
            if (openSequence.__contains__(curlvl)):
                openSequence[curlvl]+=Seq[pos]
                openSeqPos[curlvl] += [pos]
            else:
                openSequence[curlvl]=Seq[pos]
                openSeqPos[curlvl]=[pos]

        if (curChar==")"):
            curlvl-=1
            for lvl in [x for x in openSequence.keys()]:
                if (lvl>curlvl):
                    # openSeqPos[curlvl+1] += [ f"|{pos}|"] #added later.need checkup
                    openSeqPos[curlvl+1] += [ pos] #adds the next nucleotide pos after the end of current level. It is not in this level but we need to keep it so we can know where the previous loop ends if the loop is the last thing here.
                    splitSequences.append( (lvl, openSequence[lvl]) )
                    splitSeqPos.append( (lvl, openSeqPos[lvl]))
                    del openSequence[lvl]
                    del openSeqPos[lvl]

    for k, v in openSequence.items():
        splitSequences.append((k, v))
        splitSeqPos.append((k, openSeqPos[k]))
    print(splitSequences)
    print(splitSeqPos)




    for i in range(len(splitSequences)):
        if (splitSequences[i][1].__contains__("/")):
            for k in [x for x in range(len(splitSequences[i][1])) if splitSequences[i][1][x] == "/"]:
                # print (k)
                SSrange=splitSeqPos[i][1][k-1:k+2]
                print(k,SSrange)