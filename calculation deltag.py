import math

def calc_dG(seq):
    """
    Calculate deltaG of RNA/DNA sequence using the nearest-neighbor model with SantaLucia parameters.
    seq: RNA/DNA sequence as a string.
    Returns deltaG in kcal/mol.
    """
    # SantaLucia parameters for nearest-neighbor model
    enthalpy = {'AA': -7.9, 'AC': -8.4, 'AG': -7.8, 'AT': -7.2,
                'CA': -8.5, 'CC': -8.0, 'CG': -10.6, 'CT': -7.8,
                'GA': -8.2, 'GC': -9.8, 'GG': -8.0, 'GT': -8.4,
                'TA': -7.2, 'TC': -8.2, 'TG': -8.5, 'TT': -7.9}
    entropy = {'AA': -22.2, 'AC': -22.4, 'AG': -21.0, 'AT': -20.4,
               'CA': -22.7, 'CC': -19.9, 'CG': -27.2, 'CT': -21.0,
               'GA': -22.2, 'GC': -24.4, 'GG': -19.9, 'GT': -22.4,
               'TA': -21.3, 'TC': -22.2, 'TG': -22.7, 'TT': -22.2}

    # calculate deltaG using nearest-neighbor model
    dG = 0.0
    for i in range(len(seq)-1):
        dinucleotide = seq[i:i+2]
        dG += enthalpy[dinucleotide] * 1000.0  # convert to cal/mol
    dG += entropy[seq[0:2]] * 1000.0  # add first entropy
    dG += entropy[seq[-2:]] * 1000.0  # add last entropy
    dG += 1.987 * 298.15 * math.log(1.0 / 4.0)  # add salt correction
    dG /= 1000.0  # convert back to kcal/mol

    return dG
seq = "GCGCGCGCTTTTTTTTAAAAAAA"
seq="CAC AGA GAC ACA AGA GAG GGG C".replace(" ","")
dG = calc_dG(seq)
print("DeltaG = {:.2f} kcal/mol".format(dG))


enthalpy = {'AA': -7.9, 'AC': -8.4, 'AG': -7.8, 'AT': -7.2,
                'CA': -8.5, 'CC': -8.0, 'CG': -10.6, 'CT': -7.8,
                'GA': -8.2, 'GC': -9.8, 'GG': -8.0, 'GT': -8.4,
                'TA': -7.2, 'TC': -8.2, 'TG': -8.5, 'TT': -7.9}
entropy = {'AA': -22.2, 'AC': -22.4, 'AG': -21.0, 'AT': -20.4,
           'CA': -22.7, 'CC': -19.9, 'CG': -27.2, 'CT': -21.0,
           'GA': -22.2, 'GC': -24.4, 'GG': -19.9, 'GT': -22.4,
           'TA': -21.3, 'TC': -22.2, 'TG': -22.7, 'TT': -22.2}

dH=0
dS=0
for i in range(len(seq)-1):
    dH+=enthalpy[seq[i:i+2]]
    dS+=entropy[seq[i:i+2]]
print (dH)
print(dS)
