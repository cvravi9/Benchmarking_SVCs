# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Updated_Strelka_0.3_SNPs.vcf", sep = '\t', index_col= False)
df1 = pd.read_csv("Updated_VarScan_0.3_SNPs.vcf", sep = '\t', index_col= False)
df2 = pd.read_csv("Updated_Somatic_Truth_SNVs.vcf", sep = '\t', index_col= False)
df3 = pd.read_csv("Updated_Strelka_0.3.vcf", sep = '\t', index_col= False)
df4 = pd.read_csv("Updated_VarScan_0.3.vcf", sep = '\t', index_col= False)
df5 = pd.read_csv("Updated_Somatic_Truth.vcf", sep = '\t', index_col= False)
print("Length of Strelka SNPs:")
print(len(df))
print("Length of VarScan SNPs:")
print(len(df1))
print("Length of Truth SNPs:")
print(len(df2))
print("Length of Strelka:")
print(len(df3))
print("Length of VarScan:")
print(len(df4))
print("Length of Truth:")
print(len(df5))

# Adding REF and ALT
df["REF_ALT"] = df["REF"] + df["ALT"]
df1["REF_ALT"] = df1["REF"] + df1["ALT"]
df2["REF_ALT"] = df2["REF"] + df2["ALT"]

# Merging columns based on "POS"
First = pd.merge(df, df1, on=['POS'])
Second = pd.merge(df1, df2, on=['POS'])
Third = pd.merge(df2, df1, on=['POS'])
Fourth = pd.merge(First, df2, on=['POS'])

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
# First = First.drop(['REF', 'ALT'], axis=1)
# Second = Second.drop(['REF', 'ALT'], axis=1)
# Third = Third.drop(['REF', 'ALT'], axis=1)
# Fourth = Fourth.drop(['REF', 'ALT'], axis=1)
print(First)
print(Second)
print(Third)
print(Fourth)

# Adding comparisons.
# Position outcomes.
print("Number of SNPs in Strelka and VarScan:")
print(len(First))

print("Number of SNPs in VarScan and Truth Data:")
print(len(Second))

print("Number of SNPs in Truth Data and Strelka:")
print(len(Third))

print("Number of SNPs in Strelka, VarScan & Truth Data:")
print(len(Fourth))
