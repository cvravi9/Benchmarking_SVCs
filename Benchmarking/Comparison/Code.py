# Importing packages.
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import rc
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'serif'
import matplotlib.pyplot as plt
import csv

# Reading csv files and concatinating "CHROM" and "POS"
df1 = pd.read_csv("Updated_Truth.vcf", sep = '\t', index_col= False)
df2 = pd.read_csv("Updated_VarScan_0.3.vcf", sep = '\t', index_col= False)
df3 = pd.read_csv("Updated_VarScan_0.5.vcf", sep = '\t', index_col= False)
df4 = pd.read_csv("Updated_VarScan_0.7.vcf", sep = '\t', index_col= False)
df5 = pd.read_csv("Updated_Strelka_0.3.vcf", sep = '\t', index_col= False)
df6 = pd.read_csv("Updated_Strelka_0.5.vcf", sep = '\t', index_col= False)
df7 = pd.read_csv("Updated_Strelka_0.7.vcf", sep = '\t', index_col= False)

# Merging columns based on "Positions"
dff1 = pd.merge(df1, df2, on=['POS'])
dff2 = pd.merge(df1, df3, on=['POS'])
dff3 = pd.merge(df1, df4, on=['POS'])
dff4 = pd.merge(df1, df5, on=['POS'])
dff5 = pd.merge(df1, df6, on=['POS'])
dff6 = pd.merge(df1, df7, on=['POS'])
print(dff1)
print(dff2)
print(dff3)
print(dff4)
print(dff5)
print(dff6)

# Merging columns based on "Positions"
dff7 = pd.merge(dff1, dff4, on=['POS'])
dff8 = pd.merge(dff2, dff5, on=['POS'])
dff9 = pd.merge(dff3, dff6, on=['POS'])
dff7.columns = ['Position', 'First', 'Second', 'Third', 'Fourth']
dff8.columns = ['Position', 'First', 'Second', 'Third', 'Fourth']
dff9.columns = ['Position', 'First', 'Second', 'Third', 'Fourth']
print(dff7)
print(dff8)
print(dff9)

# Comparison column
dff7["Comparison"] = np.where((dff7["First"] == dff7["Third"]) & (dff7["Second"] == dff7["Fourth"]), 0, 1)
dff8["Comparison"] = np.where((dff8["First"] == dff8["Third"]) & (dff8["Second"] == dff8["Fourth"]), 0, 1)
dff9["Comparison"] = np.where((dff9["First"] == dff9["Third"]) & (dff9["Second"] == dff9["Fourth"]), 0, 1)

# Total numbers of Comparisons
dff10 = len(dff7)
dff11 = len(dff8)
dff12 = len(dff9)

# Selecting Positive Comparison
dff13 = dff7.loc[dff7['Comparison'] == 0]
dff14 = dff8.loc[dff8['Comparison'] == 0]
dff15 = dff9.loc[dff9['Comparison'] == 0]

# Total number of Positive Comparison
dff16 = len(dff13)
dff17 = len(dff14)
dff18 = len(dff15)

# Selecting Negative Comparison
dff19 = dff7.loc[dff7['Comparison'] == 1]
dff20 = dff8.loc[dff8['Comparison'] == 1]
dff21 = dff9.loc[dff9['Comparison'] == 1]

# Total number of Negative Comparison
dff22 = len(dff19)
dff23 = len(dff20)
dff24 = len(dff21)

# Delcaring a new dataframe.
df = pd.DataFrame()

# Taking all combinations as a list.
Type = ['0.3', '0.5', '0.7']
Total = [dff10, dff11, dff12]
True_True_Positive = [dff16, dff17, dff18]
True_False_Positive = [dff22, dff23, dff24]

# Adding columns
df['Tumor_Purity'] = Type
df['Total_Common_Positions'] = Total
df['True_True_Positive_ALTs'] = True_True_Positive
df['True_False_Positive_ALTs'] = True_False_Positive

# Collecting it into a dataframe.
print(df)

# Saving the results in csv.
df.to_csv('Common_Benchmarking.csv', sep=',', index = False)
