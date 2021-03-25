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

# Finding the True Positive Values
dff1["Comparison"] = np.where(dff1["ALT_x"] == dff1["ALT_y"], 0, 1)
dff2["Comparison"] = np.where(dff2["ALT_x"] == dff2["ALT_y"], 0, 1)
dff3["Comparison"] = np.where(dff3["ALT_x"] == dff3["ALT_y"], 0, 1)

# Selecting True-True Positive Comparison
dff7 = dff1.loc[dff1['Comparison'] == 0]
dff8 = dff2.loc[dff1['Comparison'] == 0]
dff9 = dff3.loc[dff1['Comparison'] == 0]

# Calculating the length
dff10 = len(dff7)
dff11 = len(dff8)
dff12 = len(dff9)

# Priting the outcome
print('True Positives in 0.3 & Truth Data')
print(dff10)
print('True Positives in 0.5 & Truth Data')
print(dff11)
print('True Positives in 0.7 & Truth Data')
print(dff12)

# Dropping an unneeded column
dff1 = dff1.drop(['Comparison'], axis=1)
dff2 = dff2.drop(['Comparison'], axis=1)
dff3 = dff3.drop(['Comparison'], axis=1)

# Obtaining the True Negative
dff1["Comparison"] = np.where(((dff1["ALT_x"] == 'NaN') & (dff1["ALT_y"] == 'NaN')), 0, 1)
dff2["Comparison"] = np.where(((dff2["ALT_x"] == 'NaN') & (dff2["ALT_y"] == 'NaN')), 0, 1)
dff3["Comparison"] = np.where(((dff3["ALT_x"] == 'NaN') & (dff3["ALT_y"] == 'NaN')), 0, 1)

# Selecting True-True Positive Comparison
dff13 = dff13.loc[dff13['Comparison'] == 0]
dff14 = dff14.loc[dff14['Comparison'] == 0]
dff15 = dff15.loc[dff15['Comparison'] == 0]

# Total number of Positive Comparison
dff16 = len(dff13)
dff17 = len(dff14)
dff18 = len(dff15)

# Priting the outcome
print('True Negative in 0.3 & Truth Data')
print(dff16)
print('True Negative in 0.5 & Truth Data')
print(dff17)
print('True Negative in 0.7 & Truth Data')
print(dff18)

# Selecting False Positives Value
dff1["Comparison"] = np.where((dff1['ALT_x'] == 'NaN') & (dff1['ALT_y'] != 'NaN'), 0, 1)
dff2["Comparison"] = np.where((dff2['ALT_x'] == 'NaN') & (dff2['ALT_y'] != 'NaN'), 0, 1)
dff3["Comparison"] = np.where((dff3['ALT_x'] == 'NaN') & (dff3['ALT_y'] != 'NaN'), 0, 1)

# Selecting True Negative Comparison
dff19 = dff1.loc[dff1['Comparison'] == 0]
dff20 = dff2.loc[dff2['Comparison'] == 0]
dff21 = dff3.loc[dff3['Comparison'] == 0]

# Total number of False Positives
dff22 = len(dff19)
dff23 = len(dff20)
dff24 = len(dff21)

# Priting the outcome
print('False Positive in 0.3 & Truth Data')
print(dff22)
print('False Positive in 0.5 & Truth Data')
print(dff23)
print('False Positive in 0.7 & Truth Data')
print(dff24)

# Dropping an unneeded column
dff1 = dff1.drop(['Comparison'], axis=1)
dff2 = dff2.drop(['Comparison'], axis=1)
dff3 = dff3.drop(['Comparison'], axis=1)

# Obtaining False Negitive Value
dff1["Comparison"] = np.where((dff1['ALT_x'] != 'NaN') & (dff1['ALT_y'] == 'NaN'), 0, 1)
dff2["Comparison"] = np.where((dff2['ALT_x'] != 'NaN') & (dff2['ALT_y'] == 'NaN'), 0, 1)
dff3["Comparison"] = np.where((dff3['ALT_x'] != 'NaN') & (dff3['ALT_y'] == 'NaN'), 0, 1)

# Selecting True Negative Comparison
dff25 = dff1.loc[dff1['Comparison'] == 0]
dff26 = dff2.loc[dff2['Comparison'] == 0]
dff27 = dff3.loc[dff3['Comparison'] == 0]

# Total number of False Negatives
dff28 = len(dff25)
dff29 = len(dff26)
dff30 = len(dff27)

# Priting the outcome
print('False Negatives in 0.3 & Truth Data')
print(dff28)
print('False Negatives in 0.5 & Truth Data')
print(dff29)
print('False Negatives in 0.7 & Truth Data')
print(dff30)

# Delcaring a new dataframe.
df = pd.DataFrame()

# Taking all combinations as a list.
Type = ['VarScan_0.3', 'VarScan_0.5', 'VarScan_0.7']
Total = [dff4, dff5, dff6]
True_Positives = [dff16, dff17, dff18]
True_Negatives = [dff25, dff26, dff27]
False_Positives = [dff31, dff32, dff33]
False_Negatives = [dff37, dff38, dff39]

# Adding columns
df['Type'] = Type
df['Total_Common_Positions'] = Total
df['True_True_Positive_ALTs'] = True_True_Positive
df['True_False_Positive_ALTs'] = True_False_Positive
df['True_Negatives_ALTs'] = True_Negative
df['False_Positives_ALTs'] = False_Positives
df['False_Negatives_ALTs'] = False_Negatives

# Collecting it into a dataframe.
print(df)

# Saving the results in csv.
df.to_csv('VarScan_Benchmarking.csv', sep=',', index = False)
