# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Boolean_Miracum_AF_Values.csv", sep = '\t', index_col= False)

# Mentioning the column names and inputing the csv file.
dff.columns = ['CHROM_POS', 'VarScan', 'Strelka', 'Equal']

# Eliminating all values of equals to 0.
needed_values = dff[~(dff == 0).any(axis=1)]
print(needed_values)

# Splitting values.
dff[['VarScan_Chr','VarScan_Value']] = dff['VarScan'].str.split(':',expand=True)
dff[['Strelka_Chr','Strelka_Value']] = dff['Strelka'].str.split(':',expand=True)
print(dff)

VarScan_Value_List = dff.VarScan_Value.to_list()
Strelka_Value_List = dff.Strelka_Value.to_list()

dff[['Difference']] = dff["VarScan_Value"] - dff["Strelka_Value"]
print(dff)

# Saving the results in csv.
dff.to_csv('Final_Miracum_AF_Values.csv', sep='\t', index = None)
