import os
import subprocess
import re


def CallRNAfold(filename, temp=37):
    directory = 'C:\\Program Files (x86)\\ViennaRNA Package\\'
    open("output.txt", "w").close()
    if os.path.exists("temp_output.fold"):
        os.remove("temp_output.fold")  # deletes the original file
    print(os.getcwd())

    #temp = float(input("Please enter the temp: "))
    subprocess.run([directory + "RNAfold.exe", "--noconv", "-i", filename, "--temp=" + str(temp),
                    "--outfile=temp_output.fold"])  # predicts the hairpins
    output = open("temp_output.fold", "r").read()  # extracts the data
    # print(output)

    rows = output.split("\n")
    description = rows[2]
    score = float(re.findall("\([ ]*[+-]?[0-9]+\.?[0-9]*\)", rows[2])[-1][1:-1])
    print(score)
    DBN = re.sub("\([ ]*[+-]?[0-9]+\.?[0-9]*\)", "", rows[2])
    rows[2] = DBN.strip()
    [print(x) for x in rows]
    # print(rows)
    return score, rows


def write_split_seq_pos_to_file(definition,temperature, split_seq_pos, score, output_filename):
    with open(output_filename, "a") as output_file:
        for level, positions in split_seq_pos:
            output_file.write(f">{definition} | Level: {level} | Temp: {temperature} | Score: {score:.2f}\n")
            output_file.write(f"{group_numbers(positions)}\n")
            # Pozisyonları ve karşılık gelen karakterleri birlikte yaz
        output_file.write("\n")

def generate_temperature_ranges(start, end, step):
    # Belirtilen başlangıçtan sona kadar olan sıcaklık aralıklarını oluşturur.
    # start: Başlangıç sıcaklığı
    # end: Bitiş sıcaklığı (dahil değil)
    # step: Adım değeri
    temp=start
    ranges=[]
    while (temp<end):
        ranges.append(temp)
        temp+=step

    return ranges

def group_numbers(lst):
    groups = []
    start = lst[0]
    end = lst[0]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            end = lst[i]
        else:
            if start == end:
                groups.append(str(start))
            else:
                groups.append(f"{start}-{end}")
            start = end = lst[i]

    if start == end:
        groups.append(str(start))
    else:
        groups.append(f"{start}-{end}")

    return ','.join(groups)

def merge_output_files(temperature_range, output_filename):
    with open(output_filename, "w") as output_file:
        for temp_value in temperature_range:
            temp_filename = f"output_{temp_value}.fasta"
            with open(temp_filename, "r") as temp_file:
                #output_file.write(f"Temperature: {temp_value}\n")
                output_file.write(temp_file.read())
            os.remove(temp_filename)  # Geçici dosyayı sil




if __name__ == "__main__":
    input_str = input(
        "Please enter the starting temperature, ending temperature (exclusive), and temperature step (comma-separated): ")
    start_temp, end_temp, temp_step = map(float, input_str.split(","))

    # RNAfold için çalıştırılacak sıcaklık aralıklarını oluştur
    temperature_range = generate_temperature_ranges(start_temp, end_temp, temp_step)

    split_output_filename = "split_seq_pos_output.txt"
    open(split_output_filename,"w").close()



    # Her bir sıcaklık değerini kullanarak işlem yapabilirsiniz
    for temp_value in temperature_range:
        scr, o1 = CallRNAfold("example.fasta", temp_value)
        definition=open("example.fasta","r").readline()[1:-1]

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

        # splitSeqPos verilerini dosyaya yaz

        write_split_seq_pos_to_file(definition, temp_value, splitSeqPos, scr, split_output_filename)

        output_filename = f"output_{temp_value}.fasta"  # Çıktı dosyasının adını sıcaklık aralığına göre belirle

        # Generate the output FASTA file
        with open(output_filename, "w") as output_file:
            for i, (level, sequence) in enumerate(splitSequences):
                positions = splitSeqPos[i][1]

                description = "{} Level: {} | Temp: {} | Score: {}".format(definition, level, temp_value, scr)
                output_file.write(">" + description + "\n" + sequence + "\n")
                print(">" + description + "\n" + sequence + "\n")

    # Çıktı dosyalarını birleştir ve tek bir dosyada sakla
    merge_output_files(temperature_range, "merged_output.fasta")

    subprocess.run("python.exe g4catchall.py --fasta merged_output.fasta >> G4out.txt",shell=True)
    with open("G4out.txt", "a") as g4out_file:
        g4out_file.write("\n")


    # output_filename = "g4catchall_output.txt"
    # with open("g4catchall_output.txt", "w") as output_file:
    # subprocess.run("python.exe g4catchall.py --fasta merged_output.fasta")


