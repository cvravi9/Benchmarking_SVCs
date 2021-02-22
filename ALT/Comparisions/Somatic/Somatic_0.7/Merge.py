# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_Somatic_0.7.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_Somatic_0.7.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['ALT', 'REF'])

# Mentioning the column names and inputing the csv file.
First.columns = ['REF', 'ALT', 'Strelka_Somatic_0.7', 'VarScan_Somatic_0.7']
print(First)

# Saving the results in csv.
First.to_csv('All_Counts.csv', index=False, encoding='utf-8')
First.to_csv('Indexed_Counts_Comparisions.csv', sep='\t', index = None)
