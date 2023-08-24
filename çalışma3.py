sequence = input("Please enter the RNA sequence: ")
RNAtoDNA={"A":"A", "U":"T", "G":"G", "C": "C"," ":" "}
DNA = ""   #ekrana yazması yetmez, belki tekrar kullanıcam, boş stringde kaydediyoruz, her loop sonunda cıkan diğeri DNA ya eklicek
for base in sequence:
    DNA+=RNAtoDNA.get(base)
print(DNA)