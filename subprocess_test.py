import sys, subprocess, os
directory='C:\\Program Files (x86)\\ViennaRNA Package\\'

if __name__=="__main__":
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