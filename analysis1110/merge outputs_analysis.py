
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

# def write_split_seq_pos_to_file(temperature, split_seq_pos, score, output_filename):
#     with open(output_filename, "a") as output_file:
#         for level, positions in split_seq_pos:
#             output_file.write(f">Level: {level} | Temp: {temperature} | Score: {score:.2f}\n")
#             output_file.write(f"{', '.join(map(str, positions))}\n")
#             # Pozisyonları ve karşılık gelen karakterleri birlikte yaz
#         output_file.write("\n")
""" 
def write_split_seq_pos_to_file(temperature, split_seq_pos, score, output_filename):
    with open(output_filename, "w") as output_file:
        for level, positions in split_seq_pos:
            description = f">Level: {level} | Temp: {temperature} | Score: {score:.2f}\n"
            output_file.write(description)

            start_pos = positions[0]  # Get the start position for the level
            sequence = Seq[start_pos:]
            before_e_pos = sequence.find("e")
            after_e_pos = sequence.rfind("e") if before_e_pos != -1 else None

            output_file.write(f"Start Position: {start_pos}\n")
            if before_e_pos != -1:
                before_e_pos += start_pos
                output_file.write(f"Before 'e' Position: {before_e_pos}\n")
            if after_e_pos is not None:
                after_e_pos += start_pos
                output_file.write(f"After 'e' Position: {after_e_pos}\n")

            output_file.write("\n")
            
"""


# def write_split_seq_pos_to_file(temperature, split_seq_pos, score, output_filename):
#     with open(output_filename, "w") as output_file:
#         for level, positions in split_seq_pos:
#             description = f">Level: {level} | Temp: {temperature} | Score: {score:.2f}\n"
#             output_file.write(description)
#
#             start_pos = positions[0]  # Seviyenin başlangıç pozisyonunu al
#             sequence = Seq[start_pos:]
#
#             # "e" harfinin pozisyonlarını bul
#             e_positions = [i for i, char in enumerate(sequence) if char == "e"]
#
#             output_file.write(f"Start Position: {start_pos}\n")
#
#             # Eğer "e" harfi bulunursa, pozisyonlarını yaz
#             if e_positions:
#                 e_positions_str = ', '.join(map(str, [pos + start_pos for pos in e_positions]))
#                 output_file.write(f"'e' Positions: {e_positions_str}\n")
#
#                 # "e" harfi pozisyonları için, önceki ve sonraki pozisyonları yaz
#                 for e_pos in e_positions:
#                     before_e_pos = e_pos - 1
#                     after_e_pos = e_pos + 1
#
#                     # Önceki pozisyonu yaz
#                     if before_e_pos >= start_pos:
#                         output_file.write(f"Before 'e' Position: {before_e_pos}\n")
#
#                     # Sonraki pozisyonu yaz
#                     if after_e_pos < start_pos + len(sequence):
#                         output_file.write(f"After 'e' Position: {after_e_pos}\n")
#
#             output_file.write("\n")


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
        #CREATES:
        #   1 ps file for each entry in input fasta file,
        #   output.txt: empty
        #   split_seq_pos.output.txt: empty
        #   temp_output.fold: contains the DBN for each entry. inclluding the deltaG


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
        #POPULATES: split_seq_output.txt is populated

        output_filename = f"output_{temp_value}.fasta"  # Çıktı dosyasının adını sıcaklık aralığına göre belirle

        # Generate the output FASTA file
        with open(output_filename, "w") as output_file:
            for i, (level, sequence) in enumerate(splitSequences):
                positions = splitSeqPos[i][1]

                description = "{} Level: {} | Temp: {} | Score: {}".format(definition, level, temp_value, scr)
                output_file.write(">" + description + "\n" + sequence + "\n")
                print(">" + description + "\n" + sequence + "\n")
        #CREATES: output_{temp}.fasta is created and populated


    # Çıktı dosyalarını birleştir ve tek bir dosyada sakla
    merge_output_files(temperature_range, "merged_output.fasta")
    # REMOVES: output_{temp}.fasta
    # CREATES: merged_output.fasta

    subprocess.run("python.exe g4catchall.py --fasta merged_output.fasta >> G4out.txt",shell=True)


    # output_filename = "g4catchall_output.txt"
    # with open("g4catchall_output.txt", "w") as output_file:
    # subprocess.run("python.exe g4catchall.py --fasta merged_output.fasta")


