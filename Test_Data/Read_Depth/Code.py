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
dff = dff.drop(['AF', 'DP4', 'HRUN', 'SB', 'INDEL', 'EFF', 'LOF', 'T'], axis=1)
print(dff)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "GT:PS:DP:GQ".
dff[['DP_Name', 'DP_Value']] = dff['DP'].str.split('=',expand=True)
print(dff)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM_POS', 'INFO', 'DP', 'DP_Name', 'DP_Value']
dff = dff.drop(['INFO', 'DP', 'DP_Name'], axis=1)
print(dff)

# Renaming columns
dff.columns = ['CHROM_POS', 'Read_Depth']

# Saving the result into a csv file for plotting.
dff.to_csv('Test_DP_Values.csv', sep=',', index = None)

# Converting the data to Integers.
dff = dff.drop(['CHROM_POS'], axis=1)
dff = dff.astype('int')
print(dff)

# Normality Test
dk = dff['Read_Depth']
dkk = dk.hist()
dkk.figure.savefig('Test_Histogram.png', dpi = 300)

# Finding the minimum values
min1 = dff['Read_Depth'].min()

# Finding the maximum values
max1 = dff['Read_Depth'].max()

# Finding the mean values
mean1 = dff['Read_Depth'].mean()

# Finding the minimum values
median1 = dff['Read_Depth'].median()

# Finding the standard deviation
std1 = dff['Read_Depth'].std()

# Delcaring a new dataframe.
df = pd.DataFrame()

# Taking all combinations as a list.
Minimum_Value = min1
Maximum_Value = max1
Mean_Value = mean1
Median_Value = median1
SD_Value = std1

# Adding columns
df['Test_Read_Depth'] = ['Minimum_Value', 'Maximum_Value', 'Mean_Value', 'Median_Value', 'SD_Value']
df['Values'] = [Minimum_Value, Maximum_Value, Mean_Value, Median_Value, SD_Value]

# Collecting it into a dataframe.
print(df)

# Saving the results in csv.
df.to_csv('Test_DP_Statistics.csv', sep=',', index = False)
df.to_html("Test_DP_Statistics.html")

# Total count
Counts = len(dff['Read_Depth'].index)
print('Total number of reads')
print(Counts)

# Selecting the range of values
SD_Lower = Mean_Value - SD_Value
SD_Higher = Mean_Value + SD_Value

# Filtering the data
dff = dff.loc[(dff['Read_Depth'] >= SD_Lower) & (dff['Read_Depth'] <= SD_Higher)]
print(dff)

# Final count
Count = len(dff['Read_Depth'].index)
print('Selected number of selected reads')
print(Count)

# Converting the values to a list
a1 = [Counts, Count]

# Getting plots
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Selected_Count', 'Filtered_Count']
explode = (0.1, 0)
colors = ['#FFD700','#FFAA1C']
ax.pie(a1, explode=explode, labels = langs, colors=colors, autopct='%1.2f%%')
plt.title('Read Depth Counts Percentage')
plt.savefig('Test_Read_Depth.pdf', dpi = 300)
