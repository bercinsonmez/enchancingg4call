import math

def calc_dG(seq):
    # define nearest neighbor parameters for RNA
    NN = {'AU': -1.0, 'UA': -1.0, 'GC': -1.44, 'CG': -2.17, 'GU': -0.42, 'UG': -0.66}
    dG = 0.0
    seq = seq.upper().replace('T', 'U') # convert any Ts to Us
    for i in range(len(seq)-1):
        dinuc = seq[i:i+2]
        if dinuc in NN:
            dG += NN[dinuc]
    dG += 0.2 * (seq.count('G') + seq.count('C') - 1) + 5.7  # add initiation and symmetry corrections
    dG -= 1.4  # subtract salt correction (50 mM Na+)
    dG *= -1000  # convert from kcal/mol to J/mol
    return dG

# example usage
seq = 'GCGGCGAACGGUACAGUUUACACUGGUCGAUCCGAACGGUAGCCUAAAUUCUCUAGUGCCCUCCACCCUUGGUCU'
dG = calc_dG(seq)
print("DeltaG = %.2f J/mol" % dG)
