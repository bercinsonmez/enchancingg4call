filename1="G4C_raw_out.txt"
filename2="G4out.txt"
# filename=r"C:\Users\brcns\PycharmProjects\HelloWorld\analysis1110\G4out.txt"

def Count(filename):

    uniqueIdentifiers = set()
    with open(filename, "r") as f:
        line = f.readline()
        while (line != ""):
            uniqueIdentifiers.add(line.split()[0])
            line = f.readline()
    return uniqueIdentifiers

res1=Count(filename1)
res2=Count(filename2)
