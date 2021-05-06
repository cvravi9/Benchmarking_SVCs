# Importing packages.
import numpy as np
import pandas as pd

# Inputing vcf files for positions.
df = pd.read_csv("Updated_Test.vcf", sep = '\t', index_col= False)
df1 = pd.read_csv("Updated_Test.annot.vcf", sep = '\t', index_col= False)

# Renaming the columns.
df.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
df1.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']

# Inputing vcf files for SNPs.
df3 = pd.read_csv("Updated_Test_SNPs.vcf", sep = '\t', index_col= False)
df4 = pd.read_csv("Updated_Test.annot_SNPs.vcf", sep = '\t', index_col= False)

# Renaming the columns.
df3.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
df4.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']

# Inputing vcf files for Indels.
df6 = pd.read_csv("Updated_Test_INDELs.vcf", sep = '\t', index_col= False)
df7 = pd.read_csv("Updated_Test.annot_INDELs.vcf", sep = '\t', index_col= False)

# Renaming the columns.
df6.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
df7.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']

# Outcome for positions.
Strelka3_Positions = len(df['POS'])
Strelka5_Positions = len(df1['POS'])

print("Number of positions in Test:")
print(Strelka3_Positions)
print("Number of positions in Test.annot:")
print(Strelka5_Positions)

# Outcome for SNPs.
Strelka3_SNPs = len(df3)
Strelka5_SNPs = len(df4)

print("Number of SNPs in Test:")
print(Strelka3_SNPs)
print("Number of SNPs in Test.annot:")
print(Strelka5_SNPs)

# Outcome for SNPs.
Strelka3_Indels = len(df6)
Strelka5_Indels = len(df7)

print("Number of Indels in Test:")
print(Strelka3_Indels)
print("Number of Indels in Test.annot:")
print(Strelka5_Indels)

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Test', 'Test.annot'], 'Positions': [Strelka3_Positions, Strelka5_Positions], 'SNPs': [Strelka3_SNPs, Strelka5_SNPs], 'INDELs': [Strelka3_Indels, Strelka5_Indels]}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('PSI_Counts.csv', sep=',', index = None)
df.to_html("PSI_Counts.html")
