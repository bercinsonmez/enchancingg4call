seq=" 5' GCT AGT CGA TGC -3' "
# I want an output of a list of bases ie. [ "GCT...GC"]
DNAbases=["G","C","A","T"]
output=[ base for base in seq if base in DNAbases ]
output= "".join(output)
#############

sentence="this is a mad world"
words=sentence.split()
output= [ len(x) for x in words ]



# #  ya da tek basamakta yazmak istersek böyle yazabiliriz
# sentence="this is a mad world"
# output= [ len(x) for x in sentence.split()]

# desired output= [4, 2, 1, 3, 5]

# sentence="this is a mad world"  # desired output= [4, 2, 1, 3, 5]
# words = sentence.split()
# output = [len(x) for x in words]