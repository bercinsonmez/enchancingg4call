#
# coll= [ 2,5,2,7,4,1,7,34,7,12,5,5 ]
#
#
# for x in coll:
#     print(x)
# print(coll)

# coll2=[]
#
# for x in coll:
#     print(x)
#     coll2.append(x + 1)
#
# print(coll2)


# f=open("example.fasta","r")
# for l in f:
#     print(l)
#
# # ya da print(l, end="")

# d={ "M":"Met","G":"Gly","I":"Iso" }

# for k in d.keys():
#     # print(k)     #burda m g ı diye sıralar
#     print(d[k])    #burda met gly iso diye sıralar

# for v in d.values():
#     print( v, end="-")    # met-gly-iso yanyana sıraladı

# for v in d.items():
#     print(v, end="-")  #('m', 'met') şeklinde

# for k,v in d.items():
#     print(k,":",v)     #M : Met G : Gly I : Iso

# for k in d.keys():
#     print(k)

# d={ "M":"Methionine","G":"Glycine","I":"Isoleucine" }

#code to change d so each value is only three letters:
# print("dictionary to change:")
# print(d)
#
# for k in d.keys():
#     d[k] = d[k][:3]
# print("change complete.")
# print(d)

# d={ "M":"Methionine","G":"Glycine","I":"Isoleucine" }
#
# coll=["e",33,(1,2),8.0,[1,2,3]]
#
# for i in enumerate(coll):
#     print(i)

d={ "M":"Methionine","G":"Glycine","I":"Isoleucine" }
coll=["e",33,(1,2),8.0,[1,2,3]]

for i in range(10):
    print(i)