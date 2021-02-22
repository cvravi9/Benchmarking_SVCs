# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Miracum_0.4_Count.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("Miracum_0.7_Count.csv", sep = '\t', index_col= False)
df2 = pd.read_csv("Somatic_0.4_Count.csv", sep = '\t', index_col= False)
df3 = pd.read_csv("Somatic_0.7_Count.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['ALT', 'REF'])
Second = pd.merge(First, df2, on=['ALT', 'REF'])
Third = pd.merge(Second, df3, on=['ALT', 'REF'])
print(Third)

# Saving the results in csv.
# Third.to_csv('All_Counts.csv', index=False, encoding='utf-8')
Third.to_csv('Indexed_Counts.csv', sep='\t', index = None)
