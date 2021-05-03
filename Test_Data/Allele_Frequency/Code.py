# Importing the needed packages.
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import rc
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'serif'
import matplotlib.pyplot as plt
import csv

# Reading the csv input file that is obtained after performing the following operations on the vcf file.
# Step 1 - 'cut -f 1-2,9-10 Input.vcf > Output.vcf'
# Step 2 - 'sed '/^#/d' Output.vcf > Updated.vcf'

# The first step is to selected the needed columns in the vcf file.
# The second step if to eliminate all lines that start with a '#'
dff = pd.read_csv("Updated_Test.vcf", sep = '\t', index_col= False)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM', 'POS', 'INFO']

# Concatinating the "CHROM" and "POS"
dff["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "GT:PS:DP:GQ".
dff[['AF', 'DP', 'DP4', 'HRUN', 'SB', 'INDEL', 'EFF', 'LOF', 'T']] = dff['INFO'].str.split(';',expand=True)

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
dff = dff.drop(['DP', 'DP4', 'HRUN', 'SB', 'INDEL', 'EFF', 'LOF', 'T'], axis=1)
print(dff)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "GT:PS:DP:GQ".
dff[['AF_Name', 'AF_Value']] = dff['AF'].str.split('=',expand=True)
print(dff)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM_POS', 'INFO', 'AF', 'AF_Name', 'AF_Value']
dff = dff.drop(['INFO', 'AF', 'AF_Name'], axis=1)
print(dff)

# Renaming columns
dff.columns = ['CHROM_POS', 'AF']

# Saving the result into a csv file for plotting.
dff.to_csv('Test_AF_Values.csv', sep=',', index = None)

# Dropping of the unnecessary column
df = dff.drop(['CHROM_POS'], axis=1)

# Converting string values columns to float.
df['AF'] = df['AF'].astype(float)

# Getting a count based on allele frequency values.
df1 = df[df < 0.26].count()
df2 = df[df < 0.51].count()
df3 = df[df < 0.76].count()
df4 = df[df < 1.01].count()
print('First quater')
print(df1)

# Getting the final values
df5 = (df1 - df2).abs()
df6 = (df2 - df3).abs()
df7 = (df3 - df4).abs()
print('Second quater')
print(df5)
print(df6)
print(df7)

# Converting into list.
First = df1.tolist()
Second = df5.tolist()
Third = df6.tolist()
Fourth = df7.tolist()

# Declaring new columns.
a1 = np.append(First, Second)
a1 = np.append(a1, Third)
a1 = np.append(a1, Fourth)
print(a1)

# set width of bar
width = 0.10

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['<= 0.25', '0.26 to 0.50', '0.51 to 0.75', '> 0.75']
explode = (0.1, 0.3, 0.1, 0.1)
colors = ['#FFD700','#FFAA1C','#FF8C01','#FF0000']
ax.pie(a1, explode=explode, labels = langs, colors=colors, autopct='%1.2f%%')
ax.set_title('Allele Frequency Counts Percentage')
plt.savefig('Test_Allele_Frequency.png', dpi = 300)
