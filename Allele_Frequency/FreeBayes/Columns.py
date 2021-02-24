# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("FreeBayes_AF_Chr1_Values.csv", sep = ',', index_col= False)
print(dff)

dff.columns = ['CHROM_POS', 'Miracum_0.4_AF', 'Miracum_0.7_AF',' Somatic_0.4_AF', 'Somatic_0.7_AF']

# Saving the results in csv.
dff.to_csv('FreeBayes_AF_Chr1_Values.csv', index=False, encoding='utf-8')
