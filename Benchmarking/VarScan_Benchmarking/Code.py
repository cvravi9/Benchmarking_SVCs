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
print(len(df1))
print(len(df2))

# Merging columns based on "Positions"
dff1 = pd.merge(df1, df2, how="outer", on=['POS'])
dff2 = pd.merge(df1, df3, how="outer", on=['POS'])
dff3 = pd.merge(df1, df4, how="outer", on=['POS'])
print(dff1)
print(dff2)
print(dff3)

# Calculating the length
dff4 = len(dff1)
dff5 = len(dff2)
dff6 = len(dff3)

# Printing the outcome
print('Total number of positions in 0.3 & Truth Data')
print(dff4)
print('Total number of positions in 0.5 & Truth Data')
print(dff5)
print('Total number of positions in 0.7 & Truth Data')
print(dff6)

# Merging columns based on "Positions"
dff7 = pd.merge(df1, df2, how="outer", on=['POS'])
dff8 = pd.merge(df1, df3, how="outer", on=['POS'])
dff9 = pd.merge(df1, df4, how="outer", on=['POS'])

# Finding the True Positive Values
dff7["Comparison"] = np.where(dff7["ALT_x"] == dff7["ALT_y"], 0, 1)
dff8["Comparison"] = np.where(dff8["ALT_x"] == dff8["ALT_y"], 0, 1)
dff9["Comparison"] = np.where(dff9["ALT_x"] == dff9["ALT_y"], 0, 1)

# Selecting True-True Positive Comparison
dff10 = dff7.loc[dff7['Comparison'] == 0]
dff11 = dff8.loc[dff8['Comparison'] == 0]
dff12 = dff9.loc[dff9['Comparison'] == 0]

# Calculating the length
dff13 = len(dff10)
dff14 = len(dff11)
dff15 = len(dff12)

# Priting the outcome
print('True Positives in 0.3 & Truth Data')
print(dff13)
print('True Positives in 0.5 & Truth Data')
print(dff14)
print('True Positives in 0.7 & Truth Data')
print(dff15)

# Merging columns based on "Positions"
dff16 = pd.merge(df1, df2, how="outer", on=['POS'])
dff17 = pd.merge(df1, df3, how="outer", on=['POS'])
dff18 = pd.merge(df1, df4, how="outer", on=['POS'])

# Obtaining the True Negative
dff16["Comparison"] = np.where(((dff16["ALT_x"] == 'NaN') & (dff16["ALT_y"] == 'NaN')), 0, 1)
dff17["Comparison"] = np.where(((dff17["ALT_x"] == 'NaN') & (dff17["ALT_y"] == 'NaN')), 0, 1)
dff18["Comparison"] = np.where(((dff18["ALT_x"] == 'NaN') & (dff18["ALT_y"] == 'NaN')), 0, 1)

# Selecting True-True Positive Comparison
dff19 = dff16.loc[dff16['Comparison'] == 0]
dff20 = dff17.loc[dff17['Comparison'] == 0]
dff21 = dff18.loc[dff18['Comparison'] == 0]

# Total number of Positive Comparison
dff22 = len(dff19)
dff23 = len(dff20)
dff24 = len(dff21)

# Priting the outcome
print('True Negative in 0.3 & Truth Data')
print(dff22)
print('True Negative in 0.5 & Truth Data')
print(dff23)
print('True Negative in 0.7 & Truth Data')
print(dff24)

# Merging columns based on "Positions"
dff25 = pd.merge(df1, df2, how="right", on=['POS'])
dff26 = pd.merge(df1, df3, how="right", on=['POS'])
dff27 = pd.merge(df1, df4, how="right", on=['POS'])
print(dff25)

# Selecting False Positives Value
dff25["Comparison"] = np.where((dff25['ALT_x'] == 'NaN') & (dff25['ALT_y'] != 'NaN'), 0, 1)
dff26["Comparison"] = np.where((dff26['ALT_x'] == 'NaN') & (dff26['ALT_y'] != 'NaN'), 0, 1)
dff27["Comparison"] = np.where((dff27['ALT_x'] == 'NaN') & (dff27['ALT_y'] != 'NaN'), 0, 1)
print(dff25)

# Selecting True Negative Comparison
dff28 = dff25.loc[dff25['Comparison'] == 1]
dff29 = dff26.loc[dff26['Comparison'] == 1]
dff30 = dff27.loc[dff27['Comparison'] == 1]
print(dff28)

# Total number of False Positives
dff31 = len(dff28)
dff32 = len(dff29)
dff33 = len(dff30)

# Priting the outcome
print('False Positive in 0.3 & Truth Data')
print(dff31)
print('False Positive in 0.5 & Truth Data')
print(dff32)
print('False Positive in 0.7 & Truth Data')
print(dff33)

# Merging columns based on "Positions"
dff34 = pd.merge(df1, df2, how="outer", on=['POS'])
dff35 = pd.merge(df1, df3, how="outer", on=['POS'])
dff36 = pd.merge(df1, df4, how="outer", on=['POS'])
print(dff34)

# Obtaining False Negitive Value
dff34["Comparison"] = np.where((dff34['ALT_x'] != 'NaN') & (dff34['ALT_y'] == 'NaN'), 0, 1)
dff35["Comparison"] = np.where((dff35['ALT_x'] != 'NaN') & (dff35['ALT_y'] == 'NaN'), 0, 1)
dff36["Comparison"] = np.where((dff36['ALT_x'] != 'NaN') & (dff36['ALT_y'] == 'NaN'), 0, 1)
print(dff34)

# Selecting True Negative Comparison
dff37 = dff34.loc[dff34['Comparison'] == 1]
dff38 = dff35.loc[dff35['Comparison'] == 1]
dff39 = dff36.loc[dff36['Comparison'] == 1]
print(dff37)

# Total number of False Negatives
dff40 = len(dff37)
dff41 = len(dff38)
dff42 = len(dff39)

# Priting the outcome
print('False Negatives in 0.3 & Truth Data')
print(dff40)
print('False Negatives in 0.5 & Truth Data')
print(dff41)
print('False Negatives in 0.7 & Truth Data')
print(dff42)

# Delcaring a new dataframe.
df = pd.DataFrame()

# Taking all combinations as a list.
Type = ['VarScan_0.3', 'VarScan_0.5', 'VarScan_0.7']
Total = [dff4, dff5, dff6]
True_Positives = [dff13, dff14, dff15]
True_Negatives = [dff22, dff23, dff24]
False_Positives = [dff31, dff32, dff33]
False_Negatives = [dff40, dff41, dff42]

# Adding columns
df['Type'] = Type
df['Total_Positions'] = Total
df['True_Positive_Variants'] = True_Positives
df['True_Negative_Variants'] = True_Negatives
df['False_Positive_Variants'] = False_Positives
df['False_Negative_Variants'] = False_Negatives

# Collecting it into a dataframe.
print(df)

# Saving the results in csv.
df.to_csv('VarScan_Benchmarking.csv', sep=',', index = False)
