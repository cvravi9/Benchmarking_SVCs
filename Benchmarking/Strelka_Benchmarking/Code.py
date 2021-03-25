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
df2 = pd.read_csv("Updated_Strelka_0.3.vcf", sep = '\t', index_col= False)
df3 = pd.read_csv("Updated_Strelka_0.5.vcf", sep = '\t', index_col= False)
df4 = pd.read_csv("Updated_Strelka_0.7.vcf", sep = '\t', index_col= False)

# Merging columns based on "Positions"
dff1 = pd.merge(df1, df2, on=['POS'])
dff2 = pd.merge(df1, df3, on=['POS'])
dff3 = pd.merge(df1, df4, on=['POS'])
print(dff1)
print(dff2)
print(dff3)

# Comparison column
dff1["Comparison"] = np.where(dff1["ALT_x"] == dff1["ALT_y"], 0, 1)
dff2["Comparison"] = np.where(dff2["ALT_x"] == dff2["ALT_y"], 0, 1)
dff3["Comparison"] = np.where(dff3["ALT_x"] == dff3["ALT_y"], 0, 1)

# Total numbers of Comparisons
dff4 = len(dff1)
dff5 = len(dff2)
dff6 = len(dff3)

# Selecting True-True Positive Comparison
dff7 = dff1.loc[dff1['Comparison'] == 0]
dff8 = dff2.loc[dff1['Comparison'] == 0]
dff9 = dff3.loc[dff1['Comparison'] == 0]

# Total number of Positive Comparison
dff10 = len(dff7)
dff11 = len(dff8)
dff12 = len(dff9)

# Selecting True-False Positive Comparison
dff13 = dff1.loc[dff1['Comparison'] == 1]
dff14 = dff2.loc[dff1['Comparison'] == 1]
dff15 = dff3.loc[dff1['Comparison'] == 1]

# Total number of Negative Comparison
dff16 = len(dff13)
dff17 = len(dff14)
dff18 = len(dff15)

# Merging True Negitive Values
dff19 = df1.merge(df2, how='outer', on=['POS'])
dff20 = df1.merge(df3, how='outer', on=['POS'])
dff21 = df1.merge(df4, how='outer', on=['POS'])

# Selecting True Negitive Value
dff19["Comparison"] = np.where((dff19['ALT_x'] == 'NaN') & (dff19['ALT_y'] == 'NaN'), 0, 1)
dff20["Comparison"] = np.where((dff20['ALT_x'] == 'NaN') & (dff20['ALT_y'] == 'NaN'), 0, 1)
dff21["Comparison"] = np.where((dff21['ALT_x'] == 'NaN') & (dff21['ALT_y'] == 'NaN'), 0, 1)

# Selecting True Negitive Comparison
dff22 = dff19.loc[dff19['Comparison'] == 0]
dff23 = dff20.loc[dff20['Comparison'] == 0]
dff24 = dff21.loc[dff21['Comparison'] == 0]

# Total number of Positive Comparison
dff25 = len(dff22)
dff26 = len(dff23)
dff27 = len(dff24)

# Obtaining False Postives.
dff28 = df2.merge(df1, how='left', on='POS')
dff29 = df3.merge(df1, how='left', on='POS')
dff30 = df4.merge(df1, how='left', on='POS')

# Selecting False Postives Value
dff28["Comparison"] = np.where((dff28['ALT_x'] != 'NaN') & (dff28['ALT_y'] == 'NaN'), 0, 1)
dff29["Comparison"] = np.where((dff29['ALT_x'] != 'NaN') & (dff29['ALT_y'] == 'NaN'), 0, 1)
dff30["Comparison"] = np.where((dff30['ALT_x'] != 'NaN') & (dff30['ALT_y'] == 'NaN'), 0, 1)

# Total number of False Postives
dff31 = len(dff28)
dff32 = len(dff29)
dff33 = len(dff30)

# Obtaining False Negatives.
dff34 = df1.merge(df2, how='left', on='POS')
dff35 = df1.merge(df3, how='left', on='POS')
dff36 = df1.merge(df4, how='left', on='POS')
print(dff34)

# Selecting True Negitive Value
dff34["Comparison"] = np.where((dff34['ALT_x'] != 'NaN') & (dff34['ALT_y'] == 'NaN'), 0, 1)
dff35["Comparison"] = np.where((dff35['ALT_x'] != 'NaN') & (dff35['ALT_y'] == 'NaN'), 0, 1)
dff36["Comparison"] = np.where((dff36['ALT_x'] != 'NaN') & (dff36['ALT_y'] == 'NaN'), 0, 1)
print(dff34)

# Total number of False Postives
dff37 = len(dff34)
dff38 = len(dff35)
dff39 = len(dff36)
print(dff37)

# Delcaring a new dataframe.
# df = pd.DataFrame()

# Taking all combinations as a list.
# Type = ['Strelka_0.3', 'Strelka_0.5', 'Strelka_0.7']
# Total = [dff4, dff5, dff6]
# True_True_Positive = [dff10, dff11, dff12]
# True_False_Positive = [dff16, dff17, dff18]

# Adding columns
# df['Type'] = Type
# df['Total_Common_Positions'] = Total
# df['True_True_Positive_ALTs'] = True_True_Positive
# df['True_False_Positive_ALTs'] = True_False_Positive

# Collecting it into a dataframe.
# print(df)

# Saving the results in csv.
# df.to_csv('Strelka_Benchmarking.csv', sep=',', index = False)

# Concatinating two files.
# dff19 = df1.merge(df2, how='left', on='POS')
# dff22 = len(dff19)
# dff23 = len(df1)
# dff24 = len(df2)
# print(dff22)
# print(dff23)
# print(dff24)

# dff25 = df1.merge(df2, how='outer', on='POS')
# dff26 = len(dff25)
# print(dff26)

# dff20 = df2.merge(df1, how='left', on='POS')
# print(dff20)

# dff21 = dff20["ALT_y"].isna().sum()
# print(dff21)
