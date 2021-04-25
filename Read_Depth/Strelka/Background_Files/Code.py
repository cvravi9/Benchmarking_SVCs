
# Importing the needed packages.
import numpy as np
import pandas as pd
from scipy.stats import shapiro
import matplotlib
from matplotlib import rc
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'serif'
import matplotlib.pyplot as plt
import csv

# Reading the csv input file that is obtained after performing the following operations on the vcf file.
# Step 1 - 'cut -f 1-2,9-11 Input-VCF-File > Output-VCF-File'
# Step 2 - 'sed '/^#/d' Output-VCF-File > Updated_Output-VCF-File'

# The first step is to selected the needed columns in the vcf file.
# The second step if to eliminate all lines that start with a '#'
dff = pd.read_csv("Updated_Strelka_0.3.vcf", sep = '\t', index_col= False)
dff1 = pd.read_csv("Updated_Strelka_0.5.vcf", sep = '\t', index_col= False)
dff2 = pd.read_csv("Updated_Strelka_0.7.vcf", sep = '\t', index_col= False)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM', 'POS', 'FORMAT', 'NORMAL', 'TUMOR']
dff1.columns = ['CHROM', 'POS', 'FORMAT', 'NORMAL', 'TUMOR']
dff2.columns = ['CHROM', 'POS', 'FORMAT', 'NORMAL', 'TUMOR']

# Concatinating the "CHROM" and "POS"
dff["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)
dff1["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)
dff2["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

dff1 = dff1.drop(['CHROM', 'POS'], axis=1)
cols = dff1.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff1 = dff1[cols]
print(dff1)

dff2 = dff2.drop(['CHROM', 'POS'], axis=1)
cols = dff2.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff2 = dff2[cols]
print(dff2)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Normal_Read_Depth', 'NORMAL-FDP', 'NORMAL-SDP', 'NORMAL-SUBDP', 'NORMAL-AU', 'NORMAL-CU', 'NORMAL-GU', 'NORMAL-TU', 'NORMAL-Last']] = dff['NORMAL'].str.split(':',expand=True)
dff[['Tumor_Read_Depth', 'TUMOR-FDP', 'TUMOR-SDP', 'TUMOR-SUBDP', 'TUMOR-AU', 'TUMOR-CU', 'TUMOR-GU', 'TUMOR-TU', 'TUMOR-Last']] = dff['TUMOR'].str.split(':',expand=True)

dff1[['Normal_Read_Depth', 'NORMAL-FDP', 'NORMAL-SDP', 'NORMAL-SUBDP', 'NORMAL-AU', 'NORMAL-CU', 'NORMAL-GU', 'NORMAL-TU', 'NORMAL-Last']] = dff1['NORMAL'].str.split(':',expand=True)
dff1[['Tumor_Read_Depth', 'TUMOR-FDP', 'TUMOR-SDP', 'TUMOR-SUBDP', 'TUMOR-AU', 'TUMOR-CU', 'TUMOR-GU', 'TUMOR-TU', 'TUMOR-Last']] = dff1['TUMOR'].str.split(':',expand=True)

dff2[['Normal_Read_Depth', 'NORMAL-FDP', 'NORMAL-SDP', 'NORMAL-SUBDP', 'NORMAL-AU', 'NORMAL-CU', 'NORMAL-GU', 'NORMAL-TU', 'NORMAL-Last']] = dff2['NORMAL'].str.split(':',expand=True)
dff2[['Tumor_Read_Depth', 'TUMOR-FDP', 'TUMOR-SDP', 'TUMOR-SUBDP', 'TUMOR-AU', 'TUMOR-CU', 'TUMOR-GU', 'TUMOR-TU', 'TUMOR-Last']] = dff2['TUMOR'].str.split(':',expand=True)

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
dff = dff.drop(['NORMAL', 'TUMOR', 'NORMAL-FDP', 'NORMAL-SDP', 'NORMAL-SUBDP', 'NORMAL-AU', 'NORMAL-CU', 'NORMAL-GU', 'NORMAL-TU', 'NORMAL-Last', 'TUMOR-FDP', 'TUMOR-SDP', 'TUMOR-SUBDP', 'TUMOR-AU', 'TUMOR-CU', 'TUMOR-GU', 'TUMOR-TU', 'TUMOR-Last'], axis=1)

dff1 = dff1.drop(['NORMAL', 'TUMOR', 'NORMAL-FDP', 'NORMAL-SDP', 'NORMAL-SUBDP', 'NORMAL-AU', 'NORMAL-CU', 'NORMAL-GU', 'NORMAL-TU', 'NORMAL-Last', 'TUMOR-FDP', 'TUMOR-SDP', 'TUMOR-SUBDP', 'TUMOR-AU', 'TUMOR-CU', 'TUMOR-GU', 'TUMOR-TU', 'TUMOR-Last'], axis=1)

dff2 = dff2.drop(['NORMAL', 'TUMOR', 'NORMAL-FDP', 'NORMAL-SDP', 'NORMAL-SUBDP', 'NORMAL-AU', 'NORMAL-CU', 'NORMAL-GU', 'NORMAL-TU', 'NORMAL-Last', 'TUMOR-FDP', 'TUMOR-SDP', 'TUMOR-SUBDP', 'TUMOR-AU', 'TUMOR-CU', 'TUMOR-GU', 'TUMOR-TU', 'TUMOR-Last'], axis=1)

# Replacing '.' values with '0'
dff.replace('.', '0', inplace=True)
dff1.replace('.', '0', inplace=True)
dff2.replace('.', '0', inplace=True)

# Converting string values columans to int.
dff['Normal_Read_Depth'] = dff['Normal_Read_Depth'].astype(int)
dff['Tumor_Read_Depth'] = dff['Tumor_Read_Depth'].astype(int)

dff1['Normal_Read_Depth'] = dff1['Normal_Read_Depth'].astype(int)
dff1['Tumor_Read_Depth'] = dff1['Tumor_Read_Depth'].astype(int)

dff2['Normal_Read_Depth'] = dff2['Normal_Read_Depth'].astype(int)
dff2['Tumor_Read_Depth'] = dff2['Tumor_Read_Depth'].astype(int)
print(dff)
print(dff1)
print(dff2)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['FORMAT'], axis=1)
dff.columns = ['CHROM_POS', 'Normal_Read_Depth', 'Tumor_Read_Depth']
print(dff)

dff1 = dff1.drop(['FORMAT'], axis=1)
dff1.columns = ['CHROM_POS', 'Normal_Read_Depth', 'Tumor_Read_Depth']
print(dff1)

dff2 = dff2.drop(['FORMAT'], axis=1)
dff2.columns = ['CHROM_POS', 'Normal_Read_Depth', 'Tumor_Read_Depth']
print(dff2)

# Merging columns based on "CHROM-POS"
First = pd.merge(dff, dff1, on=['CHROM_POS'])
Second = pd.merge(First, dff2, on=['CHROM_POS'])

# Renaming Columns
Second.columns = ['CHROM_POS', 'Strelka_Normal_0.3', 'Strelka_Tumor_0.3', 'Strelka_Normal_0.5', 'Strelka_Tumor_0.5', 'Strelka_Normal_0.7', 'Strelka_Tumor_0.7']
print(Second)

# Saving the results in csv.
Second.to_csv('Strelka_Read_Depth.csv', sep=',', index = None)

Second.columns = ['CHROM_POS', 'Third_Strelka_Normal', 'Third_Strelka_Tumor', 'Fifth_Strelka_Normal', 'Fifth_Strelka_Tumor', 'Seventh_Strelka_Normal', 'Seventh_Strelka_Tumor']

# Converting the data to Integers.
Second = Second.drop(['CHROM_POS'], axis=1)
Second = Second.astype('int')
print(Second)

# Normality Test
dk = Second['Third_Strelka_Normal']
dkk = dk.hist()
dkk.figure.savefig('Strelka_Normal_Histogram.png', dpi = 300)

dk1 = Second['Third_Strelka_Tumor']
dkk1 = dk1.hist()
dkk1.figure.savefig('Strelka_Tumor_Histogram.png', dpi = 300)

# Finding the minimum values
min1 = Second['Third_Strelka_Normal'].min()
min2 = Second['Third_Strelka_Tumor'].min()
min3 = Second['Fifth_Strelka_Normal'].min()
min4 = Second['Fifth_Strelka_Tumor'].min()
min5 = Second['Seventh_Strelka_Normal'].min()
min6 = Second['Seventh_Strelka_Tumor'].min()

# Finding the maximum values
max1 = Second['Third_Strelka_Normal'].max()
max2 = Second['Third_Strelka_Tumor'].max()
max3 = Second['Fifth_Strelka_Normal'].max()
max4 = Second['Fifth_Strelka_Tumor'].max()
max5 = Second['Seventh_Strelka_Normal'].max()
max6 = Second['Seventh_Strelka_Tumor'].max()

# Finding the mean values
mean1 = Second['Third_Strelka_Normal'].mean()
mean2 = Second['Third_Strelka_Tumor'].mean()
mean3 = Second['Fifth_Strelka_Normal'].mean()
mean4 = Second['Fifth_Strelka_Tumor'].mean()
mean5 = Second['Seventh_Strelka_Normal'].mean()
mean6 = Second['Seventh_Strelka_Tumor'].mean()

# Finding the minimum values
median1 = Second['Third_Strelka_Normal'].median()
median2 = Second['Third_Strelka_Tumor'].median()
median3 = Second['Fifth_Strelka_Normal'].median()
median4 = Second['Fifth_Strelka_Tumor'].median()
median5 = Second['Seventh_Strelka_Normal'].median()
median6 = Second['Seventh_Strelka_Tumor'].median()

# Finding the minimum values
mode1 = Second['Third_Strelka_Normal'].mode()
mode2 = Second['Third_Strelka_Tumor'].mode()
mode3 = Second['Fifth_Strelka_Normal'].mode()
mode4 = Second['Fifth_Strelka_Tumor'].mode()
mode5 = Second['Seventh_Strelka_Normal'].mode()
mode6 = Second['Seventh_Strelka_Tumor'].mode()

# Finding the standard deviation
std1 = Second['Third_Strelka_Normal'].std()
std2 = Second['Third_Strelka_Tumor'].std()
std3 = Second['Fifth_Strelka_Normal'].std()
std4 = Second['Fifth_Strelka_Tumor'].std()
std5 = Second['Seventh_Strelka_Normal'].std()
std6 = Second['Seventh_Strelka_Tumor'].std()

# Delcaring a new dataframe.
df = pd.DataFrame()

# Taking all combinations as a list.
Type = ['Strelka_Normal_0.3', 'Strelka_Tumor_0.3', 'Strelka_Normal_0.5', 'Strelka_Tumor_0.5', 'Strelka_Normal_0.7', 'Strelka_Tumor_0.7']
Minimum_Value = [min1, min2, min3, min4, min5, min6]
Maximum_Value = [max1, max2, max3, max4, max5, max6]
Mean_Value = [mean1, mean2, mean3, mean4, mean5, mean6]
Median_Value = [median1, median2, median3, median4, median5, median6]
Mode_Value = [mode1, mode2, mode3, mode4, mode5, mode6]
Std_Value = [std1, std2, std3, std4, std5, std6]

# Adding columns
df['Type'] = Type
df['Minimum_Value'] = Minimum_Value
df['Maximum_Value'] = Maximum_Value
df['Mean_Value'] = Mean_Value
df['Median_Value'] = Median_Value
df['Mode_Value'] = Mode_Value
df['SD_Value'] = Std_Value

# Collecting it into a dataframe.
print(df)

# Saving the results in csv.
df.to_csv('Strelka_Read_Depth_Statistics.csv', sep=',', index = False)

# Total count
Counts = len(Second['Third_Strelka_Normal'].index)
print('Total number of reads')
print(Counts)

# Selecting the range of values
Normal_SD_Lower = df['Mean_Value'].iloc[0] - df['SD_Value'].iloc[0]
Normal_SD_Higher = df['Mean_Value'].iloc[0] + df['SD_Value'].iloc[0]
Tumor_SD_Lower = df['Mean_Value'].iloc[1] - df['SD_Value'].iloc[1]
Tumor_SD_Higher = df['Mean_Value'].iloc[1] + df['SD_Value'].iloc[1]

# Filtering the data
Second = Second.loc[(Second['Third_Strelka_Normal'] >= Normal_SD_Lower) & (Second['Third_Strelka_Normal'] <= Normal_SD_Higher) & (Second['Third_Strelka_Tumor'] >= Tumor_SD_Lower) & (Second['Third_Strelka_Tumor'] <= Tumor_SD_Higher)]
print(Second)

# Final count
Count = len(Second['Third_Strelka_Normal'].index)
print('Selected number of selected reads')
print(Count)

# Filtered reads
Toll = Counts - Count

# Converting the values to a list
a1 = [Count, Toll]

# Getting plots
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Selected_Count', 'Filtered_Count']
explode = (0.1, 0)
colors = ['#FFD700','#FFAA1C']
ax.pie(a1, explode=explode, labels = langs, colors=colors, autopct='%1.2f%%')
ax.set_title('Read Depth Counts Percentage')
plt.savefig('Strelka_Read_Depth.png', dpi = 300)
