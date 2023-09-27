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
    score = float(re.findall("\([ ]?[+-]?[0-9]+\.?[0-9]*\)", rows[2])[-1][1:-1])
    print(score)
    DBN = re.sub("\([ ]?[+-]?[0-9]+\.?[0-9]*\)", "", rows[2])
    rows[2] = DBN.strip()
    [print(x) for x in rows]
    # print(rows)
    return score, rows


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


def write_temperature_ranges_to_file(temperature_ranges, filename):
    # Sıcaklık aralıklarını belirtilen dosyaya yazar.
    # temperature_ranges: (min, max) sıcaklık aralıklarını içeren bir liste
    # filename: Verilerin yazılacağı dosyanın adı

    with open(filename, "w") as file:
        for temp_range in temperature_ranges:
            file.write(f"{temp_range[0]},{temp_range[1]}\n")


if __name__ == "__main__":
    input_str = input(
        "Please enter the starting temperature, ending temperature (exclusive), and temperature step (comma-separated): ")
    start_temp, end_temp, temp_step = map(float, input_str.split(","))

    # RNAfold için çalıştırılacak sıcaklık aralıklarını oluştur
    temperature_range = generate_temperature_ranges(start_temp, end_temp, temp_step)

    # Her sıcaklık aralığının alt sınırlarını al


    # Her bir sıcaklık değerini kullanarak işlem yapabilirsiniz
    for temp_value in temperature_range:
        #temp_value = temp_value[0]
        scr, o1 = CallRNAfold("../thesis/example.fasta", temp_value)

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
                    openSequence[curlvl] += "/"

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

        output_filename = f"output_{temp_value}.fasta"  # Çıktı dosyasının adını sıcaklık aralığına göre belirle

        # Generate the output FASTA file
        with open(output_filename, "w") as output_file:
            for i, (level, sequence) in enumerate(splitSequences):
                positions = splitSeqPos[i][1]
                description = "Level: {} | Temp: {} | Score: {}".format(level, temp_value, scr)
                output_file.write(">" + description + "\n" + sequence + "\n")
                print(">" + description + "\n" + sequence + "\n")

    # output_lines = []

    # with open("output.fasta", "r") as output_file:
    #     for line in output_file:
    #         if line.startswith(">Level"):
    #             description = line.strip()
    #             sequence = output_file.readline().strip()
    #             # score_line = output_file.readline().strip()
    #             print("score_line:", line)
    #             score = float(line.split(" ")[-1])
    #             print(score)
    #             # G4Catchall formatına uygun çıktı oluştur
    #             g4catchall_output = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
    #                 description,  # Açıklama
    #                 0,  # Başlangıç konumu (burada 0 olarak varsayıldı)
    #                 len(sequence),  # Bitiş konumu (dizinin uzunluğu)
    #                 len(sequence),  # Eşleşme boyutu (dizinin uzunluğu)
    #                 "+",  # Strand
    #                 sequence,  # Pozitif stranddaki eşleşen dizisi
    #                 sequence,  # Eşleşen G4-quadruplex dizisi
    #                 score  # Skor
    #             )
    #
    #             output_lines.append(g4catchall_output)
    #
    #         # Çıktıları dosyaya yaz
    #     with open("g4catchall_input.txt", "w") as g4catchall_input_file:
    #         for line in output_lines:
    #             g4catchall_input_file.write(line + "\n")

import re

# Örnek çıktıları temsil eden bir liste
output_lines = [
    "Level: 8 | Temp: 50.0 | Score: -7.01 0 16 16 + ATGCATGACTCAGTAC ATGCATGACTCAGTAC -7.01",
    "Level: 4 | Temp: 50.0 | Score: -7.01 0 16 16 + ATGCATGACTCAGTAC ATGCATGACTCAGTAC -7.01",
    "Level: 0 | Temp: 50.0 | Score: -7.01 0 16 16 + ATGCATGACTCAGTAC ATGCATGACTCAGTAC -7.01",
    ">Level: 8 | Temp: 50.0 | Score: -7.01 0 16 16 + ATGCATGACTCAGTAC ATGCATGACTCAGTAC -7.01",
    ">Level: 4 | Temp: 60.0 | Score: -6.02 0 16 16 + ATGCATGACTCAGTAC ATGCATGACTCAGTAC -6.02",
    ">Level: 0 | Temp: 50.0 | Score: -5.03 0 16 16 + ATGCATGACTCAGTAC ATGCATGACTCAGTAC -5.03"
]

# Boş bir G4 sözlüğü oluştur
g4_dict = {}

# Her satırı işle
for line in output_lines:
    # Satırı düzenli bir desene göre analiz et
    match = re.match(
        r"Level: (\d+) \| Temp: ([\d.]+) \| Score: ([\-\d.]+) (\d+) (\d+) (\d+) ([\+\-]) (\w+) (\w+) ([\-\d.]+)", line)

    # Eğer uygunsa, gerekli bilgileri al
    if match:
        level = int(match.group(1))
        temperature = float(match.group(2))
        score = float(match.group(3))
        start = int(match.group(4))
        end = int(match.group(5))
        size = int(match.group(6))
        strand = match.group(7)
        seq = match.group(8)
        g4_seq = match.group(9)

        # Her G4 yapısını bir sözlük olarak temsil et
        g4 = {
            "level": level,
            "temperature": temperature,
            "score": score,
            "start": start,
            "end": end,
            "size": size,
            "strand": strand,
            "seq": seq,
            "g4_seq": g4_seq
        }

        # Aynı sıcaklık seviyesine sahip G4 yapılarını kontrol etmek için bir anahtar oluştur
        temperature_key = (level, temperature)

        # Anahtar varsa, o sıcaklık seviyesine sahip G4 yapıları üzerinde işlem yap
        if temperature_key in g4_dict:
            existing_g4_list = g4_dict[temperature_key]
            combined = False
            for existing_g4 in existing_g4_list:
                # İki G4 yapısı örtüşüyorsa
                if g4["strand"] == existing_g4["strand"] and g4["start"] <= existing_g4["end"] and g4["end"] >= \
                        existing_g4["start"]:
                    # G4 yapılarını birleştir
                    existing_g4["start"] = min(existing_g4["start"], g4["start"])
                    existing_g4["end"] = max(existing_g4["end"], g4["end"])
                    existing_g4["size"] += g4["size"]
                    existing_g4["g4_seq"] += g4["g4_seq"]
                    existing_g4["score"] += g4["score"]
                    combined = True
                    break
            # Eğer birleştirilmediyse, G4 yapısını bu sıcaklık seviyesindeki listeye ekle
            if not combined:
                existing_g4_list.append(g4)
        # Anahtar yoksa, bu sıcaklık seviyesine sahip ilk G4 yapısını eklemek için yeni bir liste oluştur
        else:
            g4_dict[temperature_key] = [g4]

# Sonuçları yazdır
for (level, temperature), g4s in g4_dict.items():
    for g4 in g4s:
        print(
            f"mychr {g4['start']} {g4['end']} {g4['size']} {g4['strand']} {g4['seq']} {g4['g4_seq']} {g4['score']}"
        )
