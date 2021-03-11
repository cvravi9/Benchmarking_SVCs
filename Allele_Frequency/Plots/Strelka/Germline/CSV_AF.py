# Importing packages.
import numpy as np
import pandas as pd

# Importing frq files and assigning columns.
dff = pd.read_csv("Strelka_Miracum_0.4.frq", sep = '\t', index_col= False, error_bad_lines=False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']

# Deleting the unneeded columns.
dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM'], axis=1)
print(dff)

# Saving the outcome to csv file.
dff.to_csv('Strelka_Miracum_0.4.csv', sep='\t', index = None)

# Importing frq files and assigning columns.
dff = pd.read_csv("Strelka_Miracum_0.7.frq", sep = '\t', index_col= False, error_bad_lines=False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']

# Deleting the unneeded columns.
dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM'], axis=1)
print(dff)

# Saving the outcome to csv file.
dff.to_csv('Strelka_Miracum_0.7.csv', sep='\t', index = None)

# Importing frq files and assigning columns.
dff = pd.read_csv("Strelka_Somatic_0.4.frq", sep = '\t', index_col= False, error_bad_lines=False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']

# Deleting the unneeded columns.
dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM'], axis=1)
print(dff)

# Saving the outcome to csv file.
dff.to_csv('Strelka_Somatic_0.4.csv', sep='\t', index = None)

# Importing frq files and assigning columns.
dff = pd.read_csv("Strelka_Somatic_0.7.frq", sep = '\t', index_col= False, error_bad_lines=False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']

# Deleting the unneeded columns.
dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM'], axis=1)
print(dff)

# Saving the outcome to csv file.
dff.to_csv('Strelka_Somatic_0.7.csv', sep='\t', index = None)
