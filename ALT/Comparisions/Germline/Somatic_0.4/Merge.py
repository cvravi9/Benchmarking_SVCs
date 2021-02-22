# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("FreeBayes_Somatic_0.4.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("Strelka_Somatic_0.4.csv", sep = '\t', index_col= False)
df2 = pd.read_csv("VarScan_Somatic_0.4.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['ALT', 'REF'])
Second = pd.merge(First, df2, on=['ALT', 'REF'])

# Mentioning the column names and inputing the csv file.
Second.columns = ['REF', 'ALT', 'FreeBayes_Somatic_0.4', 'Strelka_Somatic_0.4', 'VarScan_Somatic_0.4']
print(Second)

# Saving the results in csv.
# Second.to_csv('Counts_Comparisions.csv', index=False, encoding='utf-8')
Second.to_csv('Indexed_Counts_Comparisions.csv', sep='\t', index = None)
