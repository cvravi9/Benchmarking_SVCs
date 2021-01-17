import numpy as np
import pandas as pd

dff = pd.read_csv("Miracum_0.4_Allele_Frequency.frq", sep = '\t', index_col= False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']

dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM'], axis=1)
print(dff)

dff.to_csv('Miracum_0.4_AF_Plot.csv', sep='\t', index = None)
