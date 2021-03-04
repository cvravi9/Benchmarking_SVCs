# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("VarScan_0.3_Count.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_0.5_Count.csv", sep = '\t', index_col= False)
df2 = pd.read_csv("VarScan_0.7_Count.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['ALT', 'REF'])
Second = pd.merge(First, df2, on=['ALT', 'REF'])

# Mentioning the column names and inputing the csv file.
Second.columns = ['REF', 'ALT', 'VarScan_0.3', 'VarScan_0.5', 'VarScan_0.7']
print(Second)

# Saving the results in csv.
Second.to_csv('VarScan_Comparisions.csv', index=False, encoding='utf-8')
Second.to_csv('VarScan_Plot_Comparisions.csv', sep='\t', index = None)
