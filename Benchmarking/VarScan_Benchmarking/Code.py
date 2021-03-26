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
print(len(df1))
print(len(df2))

# Merging columns based on "Positions"
dff3 = pd.merge(df1, df2, how="outer", on=['POS'])
dff8 = pd.merge(df1, df2, how="outer", on=['POS'])
print(dff3)

# Calculating the length
dff4 = len(dff3)

# Printing the outcome
print('Total number of positions in 0.3 & Truth Data')
print(dff4)

# Obtaining the True Negative
dff3.dropna(subset = ["ALT_x"], inplace=True)
dff3.dropna(subset = ["ALT_y"], inplace=True)
dff5 = len(dff3)
print(dff3)

# Printing the outcome
print('Total number of non-zero positions in 0.3 & Truth Data')
print(dff5)

# Comparison column
dff3["Comparison"] = np.where(dff3["ALT_x"] == dff3["ALT_y"], 0, 1)
print(dff3)

# Selecting True-True Positive Comparison
dff4 = dff3.loc[dff3['Comparison'] == 0]

# Total number of Positive Comparison
dff5 = len(dff4)
print(dff5)

# Selecting True-True Positive Comparison
dff6 = dff3.loc[dff3['Comparison'] == 1]

# Calculating the length
dff7 = len(dff6)
print(dff7)

print(dff8)
# Selecting True Negative Value
dff8["Comparison"] = np.where((dff8['ALT_x'] != 'NaN') & (dff8['ALT_y'] == 'NaN'), 0, 1)
print(dff8)

# Selecting True Negative Comparison
dff9 = dff8.loc[dff8['Comparison'] == 0]
print(dff9)

# Total number of True Negative Comparison
dff10 = len(dff9)
print(dff10)

# Priting the outcome
# print('True Positives in 0.3 & Truth Data')
# print(dff9)

# Merging columns based on "Positions"
# dff25 = pd.merge(df1, df2, how="right", on=['POS'])
# print(dff25)

# Selecting False Positives Value
# dff25["Comparison"] = np.where((dff25['ALT_x'] == 'NaN') & (dff25['ALT_y'] != 'NaN'), 0, 1)
# print(dff25)

# Selecting True Negative Comparison
# dff28 = dff25.loc[dff25['Comparison'] == 1]
# print(dff28)

# Total number of False Positives
# dff31 = len(dff28)

# Priting the outcome
# print('False Positive in 0.3 & Truth Data')
# print(dff31)

# Obtaining False Negitive Value
# dff34["Comparison"] = np.where((dff34['ALT_x'] != 'NaN') & (dff34['ALT_y'] == 'NaN'), 0, 1)
# print(dff34)

# Selecting True Negative Comparison
# dff37 = dff34.loc[dff34['Comparison'] == 1]
# print(dff37)

# Total number of False Negatives
# dff40 = len(dff37)

# Priting the outcome
# print('False Negatives in 0.3 & Truth Data')
# print(dff40)

# Delcaring a new dataframe.
# df = pd.DataFrame()

# Taking all combinations as a list.
# Type = ['VarScan_0.3']
# Total = [dff4]
# True_Positives = [dff13]
# True_Negatives = [dff22]
# False_Positives = [dff31]
# False_Negatives = [dff40]

# Adding columns
# df['Type'] = Type
# df['Total_Positions'] = Total
# df['True_Positive_Variants'] = True_Positives
# df['True_Negative_Variants'] = True_Negatives
# df['False_Positive_Variants'] = False_Positives
# df['False_Negative_Variants'] = False_Negatives

# Collecting it into a dataframe.
# print(df)

# Saving the results in csv.
# df.to_csv('VarScan_Benchmarking.csv', sep=',', index = False)
