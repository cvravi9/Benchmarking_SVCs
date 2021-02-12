# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Boolean_Miracum_AF_Values.csv", sep = '\t', index_col= False)

needed_values = dff[~(dff == 0).any(axis=1)]
print(needed_values)

# Saving the results in csv.
needed_values.to_csv('Final_Miracum_AF_Values.csv', sep='\t', index = None)
