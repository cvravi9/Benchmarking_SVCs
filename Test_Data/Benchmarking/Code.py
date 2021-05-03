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
df1 = pd.read_csv("Updated_Test.vcf", sep = '\t', index_col= False)
df2 = pd.read_csv("Updated_Test.annot.vcf", sep = '\t', index_col= False)

# Merging columns based on "Positions"
dff1 = pd.merge(df1, df2, how="outer", on=['POS'])

# Renaming the columns after importing the input.
dff1.columns = ['POS', 'Truth_Data', 'Strelka_Three']
print(dff1)

# Total number of reads
dff4 = len(dff1)
print('Total lenght is')
print(dff4)

# Comparison column
dff1["TP"] = np.where(dff1["Truth_Data"].notnull() & dff1["Strelka_Three"].notnull(), 0, 1)
dff1["TN"] = np.where(dff1["Truth_Data"].isnull() & dff1["Strelka_Three"].isnull(), 0, 1)
dff1["FP"] = np.where(dff1["Truth_Data"].isnull() & dff1["Strelka_Three"].notnull(), 0, 1)
dff1["FN"] = np.where(dff1["Truth_Data"].notnull() & dff1["Strelka_Three"].isnull(), 0, 1)

# Selecting the columns
dff5 = dff1.loc[dff1['TP'] == 0]
dff6 = dff1.loc[dff1['TN'] == 0]
dff7 = dff1.loc[dff1['FP'] == 0]
dff8 = dff1.loc[dff1['FN'] == 0]

# Total numbers of Comparisons
dff9 = len(dff5)
dff10 = len(dff6)
dff11 = len(dff7)
dff12 = len(dff8)

print("Total number of True Positives:")
print(dff9)
print("Total number of True Negatives:")
print(dff10)
print("Total number of False Postivies:")
print(dff11)
print("Total number of False Negatives:")
print(dff12)

# Merging columns based on "Positions"
dff29 = pd.merge(df1, df2, on=['POS'])
dff29.columns = ['POS', 'Truth_Data', 'Strelka_Three']
print(dff29)

# Comparison column
dff29["Comparison"] = np.where((dff29["Truth_Data"] == dff29["Strelka_Three"]), 0, 1)

# Selecting Positive Comparison
dff35 = dff29.loc[dff29['Comparison'] == 0]

# Total number of Positive Comparison
dff38 = len(dff35)

# Selecting Negative Comparison
dff41 = dff29.loc[dff29['Comparison'] == 1]

# Total number of Negative Comparison
dff44 = len(dff41)

# Delcaring a new dataframe.
df = pd.DataFrame()

# Taking all combinations as a list.
Type = ['Count']
Total = [dff4]
True_Positive = [dff9]
True_Negative = [dff10]
False_Positives = [dff11]
False_Negatives = [dff12]
True_True_Postive = [dff38]
True_False_Postive = [dff44]

# Adding columns
df['Type'] = Type
df['Total'] = Total
df['True_Positives_ALTs'] = True_Positive
df['True_True_Positives_ALTs'] = True_True_Postive
df['True_False_Positives_ALTs'] = True_False_Postive
df['True_Negatives_ALTs'] = True_Negative
df['False_Positives_ALTs'] = False_Positives
df['False_Negatives_ALTs'] = False_Negatives

# Collecting it into a dataframe.
print(df)

# Saving the results in csv.
df.to_csv('Benchmarking.csv', sep=',', index = False)
