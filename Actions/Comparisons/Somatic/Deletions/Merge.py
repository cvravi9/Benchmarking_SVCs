# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_Somatic_Deletions_Counts.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_Somatic_Deletions_Counts.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['Type'])
print(First)

# Saving the results in csv.
First.to_csv('Somatic_Deletions_Comparision.csv', index=False, encoding='utf-8')
