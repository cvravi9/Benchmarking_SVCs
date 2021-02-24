# Importing packages.
import numpy as np
import pandas as pd

# Importing frq files and assigning columns.
dff = pd.read_csv("Somatic_0.4_Chr5_Somatic.frq", sep = '\t', index_col= False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']

# Deleting the unneeded columns.
dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM'], axis=1)
print(dff)

# Saving the outcome to csv file.
dff.to_csv('Somatic_0.4_Chr5_Somatic.csv', sep='\t', index = None)
