# # BEN 519 Homework2 / Burcin Dersu Acikgoz / Student Number: 20203512003
# sequence = input("Enter the sequence>>> ")
# complements ={"A":"T","T":"A", "G":"C", "C":"G"," ":" "}
# complement_sequence = ""
# for base in sequence:
#     if base in complements:
#         complement_sequence+=complements.get(base)
#     else:
#         print(base, "is not recognized")
# print(complement_sequence)

# 1.satır -- input alıyosun
# 2.satır -- dict tanımlıyorsun, entryler key value şeklinde tutuluyor. Sol key, sağ value
# 3.satır -- boş variable oluşturuyoruz, complement yazıcağımız için, boş string
# 4.satır -- for içinde string sequence, her harf bir baza denk geliyor. For içinde her karakter için bazın complement
# dict içinde olup olmadığına bakıyor, varsa dictten alıyor, ucuna ekliyor

sequence= input("enter the sequence")
complements ={"A":"T","T":"A", "G":"C", "C":"G"}
complement_sequence = ""
for base in sequence:
    complement_sequence+=complements.get(base)
    print(complement_sequence)

