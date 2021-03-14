# Importing packages.
import numpy as np
import pandas as pd

# Inputing first vcf file.
df = pd.read_csv("Updated_Strelka_0.3.vcf", sep = '\t', index_col= False)

# Position outcomes.
print("Number of positions in Strelka 0.3:")
print(len(df))

# Inputing second vcf file
df1 = pd.read_csv("Updated_Strelka_0.5.vcf", sep = '\t', index_col= False)

# Position outcomes.
print("Number of positions in Strelka 0.5:")
print(len(df1))

# Inputing third vcf file.
df2 = pd.read_csv("Updated_Strelka_0.7.vcf", sep = '\t', index_col= False)

# Position outcomes.
print("Number of positions in Strelka 0.7:")
print(len(df2))

# Inputing first SNP file.
df3 = pd.read_csv("Updated_Strelka_0.3_SNPs.vcf", sep = '\t', index_col= False)

# Position outcomes.
print("Number of SNPs in Strelka 0.3:")
print(len(df3))

# Inputing second SNP file
df4 = pd.read_csv("Updated_Strelka_0.5_SNPs.vcf", sep = '\t', index_col= False)

# Position outcomes.
print("Number of SNPs in Strelka 0.5:")
print(len(df4))

# Inputing third SNP file.
df5 = pd.read_csv("Updated_Strelka_0.7_SNPs.vcf", sep = '\t', index_col= False)

# Position outcomes.
print("Number of SNPs in Strelka 0.7:")
print(len(df5))
