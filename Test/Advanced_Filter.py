# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Final_Miracum_AF_Values.csv", sep = '\t', index_col= False)

# Mentioning the column names and inputing the csv file.
dff.columns = ['CHROM_POS', 'VarScan', 'Strelka', 'Equal', 'VarScan_Chr', 'VarScan_Value', 'Strelka_Chr', 'Strelka_Value', 'Difference']

# Reorganising columns.
# dff = dff.drop(['VarScan', 'Strelka', 'Equal'], axis=1)

comparison_column = np.where(dff["VarScan_Chr"] == dff["Strelka_Chr"], 0, 1)
dff["Chr_Equal"] = comparison_column
print(comparison_column)

# Eliminating all values of equals to 0.
needed_values = dff[~(dff == 1).any(axis=1)]
print(needed_values)

# Reorganising columns.
dff = dff.drop(['VarScan', 'Strelka', 'Equal'], axis=1)

dff = dff[dff.Chr_Equal != 0]
print(dff)

# selecting rows based on condition
dff = dff[dff['Difference'] > 0.75]
print(dff)

# Saving the results in csv.
dff.to_csv('Ultimate_Miracum_AF_Values.csv', sep='\t', index = None)
