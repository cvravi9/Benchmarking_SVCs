# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Comparision_Miracum_AF_Values.csv", sep = '\t', index_col= False)
comparison_column = np.where(dff["Miracum_0.4_AF"] == dff["Miracum_0.7_AF"], True, False)
dff["Equal"] = comparison_column
print(comparison_column)

needed_values = dff.loc[dff['Equal'] == 'False']
print(needed_values)

# Saving the results in csv.
needed_values.to_csv('Final_Equals_Miracum_AF.csv', sep='\t', index = None)
