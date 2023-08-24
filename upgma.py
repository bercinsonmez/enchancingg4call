# Clustering Algorithm
# unweighted pair group method with arithmetic mean
# how can we express similarities between DNA sequences?

import numpy as np
#   a   b   c   d   e
#a  0   5   7   9  25
#b  5   0   9  12  22
#c  7   9   0   8  23
#d  9  12   8   0  43
#e 25  22  23  43   0

# convert to (((a,b),e),(c,d))


D_current=np.zeros(shape=(5, 5))

def assign(matrix, value, n,m):
    matrix[m,n]=value
    matrix[n,m]=value

assign(D_current, 5, 0, 1)
assign(D_current, 7, 0, 2)
assign(D_current, 9, 0, 3)
assign(D_current, 25, 0, 4)
assign(D_current, 9, 1, 2)
assign(D_current, 12, 1, 3)
assign(D_current, 22, 1, 4)
assign(D_current, 8, 2, 3)
assign(D_current, 23, 2, 4)
assign(D_current, 43, 3, 4)

Items_current=["a", "b", "c", "d", "e"]

def where_is_min(matrix,items):
    known_min=np.inf
    m=0
    n=0
    for i in range(matrix.shape[0]):
        for j in range(i+1,matrix.shape[1]):
            if matrix [i,j] < known_min:
                known_min=matrix [i,j]
                m,n=i,j
    return known_min,items[m],items[n]

def combine(matrix, items, item1, item2):
    # example.fasta combine(D_current,Items_current,"a","b")
    Dnext=np.zeros(shape=( matrix.shape[0]-1,matrix.shape[1]-1 ) )
    ItemsNext= [x for x in items if x not in (item1, item2)]
    ItemsNext.append( "("+item1+","+item2+")" )
    # ItemsNext=["c","d","e","(a,b)"]

    for i in range(Dnext.shape[0]): #ex i=0
        for j in range(i+1,Dnext.shape[1]):#ex j=1
            if ItemsNext[i] in items and ItemsNext[j] in items:
                a=items.index(ItemsNext[i]) #ex: 2
                b=items.index(ItemsNext[j]) #ex: 3
                assign(Dnext,matrix[a,b],i,j) #ex: 8.0

    for i in range(Dnext.shape[0]-1):
        oc= items.index(ItemsNext[i])
        oa= items.index(item1)
        ob= items.index(item2)
        assign(Dnext,(matrix[oa,oc]+matrix[ob,oc])/2,i,-1)

    print(ItemsNext)
    print(Dnext)
    return Dnext,ItemsNext

while len(Items_current)>1:
    _,Item1,Item2=where_is_min(D_current,Items_current)
    D_current,Items_current=combine(D_current,Items_current,Item1,Item2)
print("resulting UPGMA tree without distances:",Items_current[0])