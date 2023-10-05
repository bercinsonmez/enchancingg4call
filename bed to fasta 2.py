bed_file = r"C:\Users\brcns\Downloads\Na_PDS_plus_hits_intersect.bed"
hg19_file=r"C:\Users\brcns\Downloads\HG19 (3).fasta"

# Kullanıcıdan hg19 FASTA dosyasının yolunu alın
#hg19_file = input("hg19 FASTA dosyasının yolunu girin: ")

# Kullanıcıdan BED dosyasının yolunu alın
#bed_file = input("BED dosyasının yolunu girin: ")

output_file = "third_output_chr21.fasta"  # Çıktı dosyasının adını belirtin

output_fasta=open(output_file, "w")

# hg19 FASTA dosyasını okuyun
with open(hg19_file, "r") as hg19_fasta:
    hg19_data = hg19_fasta.read()

# BED dosyasını okuyun
with open(bed_file, "r") as bed:
    for line in bed:
        parts = line.strip().split("\t")
        chromosome = parts[0]
        start = int(parts[1])
        end = int(parts[2])

        # Sadece kromozom 21 için işlem yapın
        if chromosome == "chr21":
            # Kromozom 21 sekansını alın
            chromosome21_seq = ""
            in_sequence = False
            lines = hg19_data.split("\n")
            for fasta_line in lines:
                if fasta_line.startswith(">"):
                    if in_sequence:
                        break
                    continue
                else:
                    chromosome21_seq += fasta_line.strip()
                    in_sequence = True

            # Verilen başlangıç ve bitiş pozisyonlarına göre sekansı alın
            chromosome21_seq = chromosome21_seq[start - 1:end]

            # Yeni bir FASTA dosyasına yazın
            #output_file = "output_chr21.fasta"  # Çıktı dosyasının adını belirtin
            #with open(output_file, "a") as output_fasta:
            header = f">{chromosome}:{start}-{end}"
            output_fasta.write(header + "\n")
            output_fasta.write(chromosome21_seq + "\n")
            output_fasta.flush()

print("İşlem tamamlandı. Çıktı FASTA dosyası oluşturuldu.")
