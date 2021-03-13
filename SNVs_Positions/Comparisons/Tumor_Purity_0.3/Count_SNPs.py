# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Updated_Strelka_0.3_SNPs.vcf", sep = '\t', index_col= False)
df["REF_ALT"] = df["REF"] + df["ALT"]
print(df)

df1 = pd.read_csv("Updated_VarScan_0.3_SNPs.vcf", sep = '\t', index_col= False)
df1["REF_ALT"] = df1["REF"] + df1["ALT"]
print(df1)

df2 = pd.read_csv("Updated_Somatic_Truth_SNVs.vcf", sep = '\t', index_col= False)
df2["REF_ALT"] = df2["REF"] + df2["ALT"]
print(df2)

# Merging columns based on "POS"
First = pd.merge(df, df1, on=['REF_ALT'])
Second = pd.merge(df1, df2, on=['REF_ALT'])
Third = pd.merge(df2, df1, on=['REF_ALT'])
Fourth = pd.merge(First, df2, on=['REF_ALT'])

# Converting string values columns to string.
First['REF_ALT'] = First['REF_ALT'].astype(string)
Second['REF_ALT'] = Second['REF_ALT'].astype(string)
Third['REF_ALT'] = Third['REF_ALT'].astype(string)

# Position outcomes.
print("Number of SNPs in Strelka and VarScan:")
print(len(First))

print("Number of SNPs in VarScan and Truth Data:")
print(len(Second))

print("Number of SNPs in Truth Data and Strelka:")
print(len(Third))

print("Number of SNPs in Strelka, VarScan & Truth Data:")
print(len(Fourth))
