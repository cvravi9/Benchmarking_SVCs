# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Comparision_AF_Miracum.csv", sep = '\t', index_col= False)
comparison_column = np.where(dff["Miracum_0.4_AF_VarScan"] == dff["Miracum_0.4_AF_Strelka"], 0, 1)
dff["Equal"] = comparison_column
print(comparison_column)

# Saving the results in csv.
dff.to_csv('Boolean_Miracum_AF_Values.csv', sep='\t', index = None)
