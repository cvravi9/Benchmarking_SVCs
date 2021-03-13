# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Updated_Strelka_0.3.vcf", sep = '\t', index_col= False)
df1 = pd.read_csv("Updated_VarScan_0.3.vcf", sep = '\t', index_col= False)
df2 = pd.read_csv("Updated_Somatic_Truth.vcf", sep = '\t', index_col= False)

# Merging columns based on "POS"
First = pd.merge(df, df1, on=['POS'])
Second = pd.merge(df1, df2, on=['POS'])
Third = pd.merge(df2, df1, on=['POS'])
Fourth = pd.merge(First, df2, on=['POS'])

# Position outcomes.
print("Number of positions in Strelka and VarScan:")
print(len(First))

print("Number of positions in VarScan and Truth Data:")
print(len(Second))

print("Number of positions in Truth Data and Strelka:")
print(len(Third))

print("Number of positions in Strelka, VarScan & Truth Data:")
print(len(Fourth))
