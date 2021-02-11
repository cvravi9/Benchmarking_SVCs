# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Allele_Frequency_Values.csv", sep = '\t', index_col= False)
dff = dff.drop(['Miracum_0.7_AF', 'Somatic_0.4_AF'], axis=1)
print(dff)

# Saving the results in csv.
dff.to_csv('Comparision_AF_0.4_vs_0.7.csv', sep='\t', index = None)
