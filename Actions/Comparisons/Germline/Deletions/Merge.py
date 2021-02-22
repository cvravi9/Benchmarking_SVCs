# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("FreeBayes_Deletions_Counts.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("Strelka_Germline_Deletions_Counts.csv", sep = '\t', index_col= False)
df2 = pd.read_csv("VarScan_Germline_Deletions_Counts.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['Type'])
Second = pd.merge(First, df2, on=['Type'])
print(Second)

# Saving the results in csv.
Second.to_csv('Deletions_Comparision.csv', index=False, encoding='utf-8')
Second.to_csv('Indexed_Deletions_Comparisions.csv', sep='\t', index = None)
