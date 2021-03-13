# Importing packages.
import numpy as np
import pandas as pd

# Inputing first vcf file.
df = pd.read_csv("Updated_Somatic_Truth.vcf", sep = '\t', index_col= False)

# Position outcomes.
print("Number of positions in Truth Data:")
print(len(df))

# Inputing third SNP file.
df2 = pd.read_csv("Updated_Somatic_Truth_SNVs.vcf", sep = '\t', index_col= False)

# Position outcomes.
print("Number of SNPs in Truth Data")
print(len(df2))
