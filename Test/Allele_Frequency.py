# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("All_AF_Values.csv", sep = '\t', index_col= False)
dff = dff.drop(['Miracum_0.7_AF_VarScan', 'Somatic_0.4_AF_VarScan', 'Somatic_0.7_AF_VarScan', 'Miracum_0.7_AF_Strelka', 'Somatic_0.4_AF_Strelka', 'Somatic_0.7_AF_Strelka'], axis=1)
print(dff)

# Saving the results in csv.
dff.to_csv('Comparision_AF_Miracum.csv', sep='\t', index = None)
