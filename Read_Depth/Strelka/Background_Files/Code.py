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

# Saving the results in csv.
dff.to_csv('Strelka3_Read_Depth.csv', sep=',', index = None)
dff1.to_csv('Strelka5_Read_Depth.csv', sep=',', index = None)
dff2.to_csv('Strelka7_Read_Depth.csv', sep=',', index = None)

# Converting the data to Integers.
dff = dff.drop(['CHROM_POS'], axis=1)
dff = dff.astype('int')
print(dff)

dff1 = dff1.drop(['CHROM_POS'], axis=1)
dff1 = dff1.astype('int')
print(dff1)

dff2 = dff2.drop(['CHROM_POS'], axis=1)
dff2 = dff2.astype('int')
print(dff2)


# Normality Test
# dk = Second['Third_Strelka_Normal']
# dkk = dk.hist()
# dkk.figure.savefig('Strelka_Normal_Histogram.png', dpi = 300)

# dk1 = Second['Third_Strelka_Tumor']
# dkk1 = dk1.hist()
# dkk1.figure.savefig('Strelka_Tumor_Histogram.png', dpi = 300)

# Finding the minimum values
min1 = dff['Normal_Read_Depth'].min()
min2 = dff['Tumor_Read_Depth'].min()
min3 = dff1['Normal_Read_Depth'].min()
min4 = dff1['Tumor_Read_Depth'].min()
min5 = dff2['Normal_Read_Depth'].min()
min6 = dff2['Tumor_Read_Depth'].min()

# Finding the maximum values
max1 = dff['Normal_Read_Depth'].max()
max2 = dff['Tumor_Read_Depth'].max()
max3 = dff1['Normal_Read_Depth'].max()
max4 = dff1['Tumor_Read_Depth'].max()
max5 = dff2['Normal_Read_Depth'].max()
max6 = dff2['Tumor_Read_Depth'].max()

# Finding the mean values
mean1 = dff['Normal_Read_Depth'].mean()
mean2 = dff['Tumor_Read_Depth'].mean()
mean3 = dff1['Normal_Read_Depth'].mean()
mean4 = dff1['Tumor_Read_Depth'].mean()
mean5 = dff2['Normal_Read_Depth'].mean()
mean6 = dff2['Tumor_Read_Depth'].mean()

# Finding the minimum values
median1 = dff['Normal_Read_Depth'].median()
median2 = dff['Tumor_Read_Depth'].median()
median3 = dff1['Normal_Read_Depth'].median()
median4 = dff1['Tumor_Read_Depth'].median()
median5 = dff2['Normal_Read_Depth'].median()
median6 = dff2['Tumor_Read_Depth'].median()

# Finding the minimum values
mode1 = dff['Normal_Read_Depth'].mode()
mode2 = dff['Tumor_Read_Depth'].mode()
mode3 = dff1['Normal_Read_Depth'].mode()
mode4 = dff1['Tumor_Read_Depth'].mode()
mode5 = dff2['Normal_Read_Depth'].mode()
mode6 = dff2['Tumor_Read_Depth'].mode()

# Finding the standard deviation
std1 = dff['Normal_Read_Depth'].std()
std2 = dff['Tumor_Read_Depth'].std()
std3 = dff1['Normal_Read_Depth'].std()
std4 = dff1['Tumor_Read_Depth'].std()
std5 = dff2['Normal_Read_Depth'].std()
std6 = dff2['Tumor_Read_Depth'].std()

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
dff_Count = len(dff['Normal_Read_Depth'].index)
dff1_Count = len(dff1['Normal_Read_Depth'].index)
dff2_Count = len(dff2['Normal_Read_Depth'].index)

# Selecting the range of values
dff_Normal_Lower = df['Mean_Value'].iloc[0] - df['SD_Value'].iloc[0]
dff_Normal_Higher = df['Mean_Value'].iloc[0] + df['SD_Value'].iloc[0]
dff_Tumor_Lower = df['Mean_Value'].iloc[1] - df['SD_Value'].iloc[1]
dff_Tumor_Higher = df['Mean_Value'].iloc[1] + df['SD_Value'].iloc[1]

dff1_Normal_Lower = df['Mean_Value'].iloc[2] - df['SD_Value'].iloc[2]
dff1_Normal_Higher = df['Mean_Value'].iloc[2] + df['SD_Value'].iloc[2]
dff1_Tumor_Lower = df['Mean_Value'].iloc[3] - df['SD_Value'].iloc[3]
dff1_Tumor_Higher = df['Mean_Value'].iloc[3] + df['SD_Value'].iloc[3]

dff2_Normal_Lower = df['Mean_Value'].iloc[4] - df['SD_Value'].iloc[4]
dff2_Normal_Higher = df['Mean_Value'].iloc[4] + df['SD_Value'].iloc[4]
dff2_Tumor_Lower = df['Mean_Value'].iloc[5] - df['SD_Value'].iloc[5]
dff2_Tumor_Higher = df['Mean_Value'].iloc[5] + df['SD_Value'].iloc[5]

# Filtering the data
dff = dff.loc[(dff['Normal_Read_Depth'] >= dff_Normal_Lower) & (dff['Normal_Read_Depth'] <= dff_Normal_Higher) & (dff['Tumor_Read_Depth'] >= dff_Tumor_Lower) & (dff['Tumor_Read_Depth'] <= dff_Tumor_Higher)]
dff1 = dff1.loc[(dff1['Normal_Read_Depth'] >= dff1_Normal_Lower) & (dff1['Normal_Read_Depth'] <= dff1_Normal_Higher) & (dff1['Tumor_Read_Depth'] >= dff1_Tumor_Lower) & (dff1['Tumor_Read_Depth'] <= dff1_Tumor_Higher)]
dff2 = dff2.loc[(dff2['Normal_Read_Depth'] >= dff2_Normal_Lower) & (dff2['Normal_Read_Depth'] <= dff2_Normal_Higher) & (dff2['Tumor_Read_Depth'] >= dff2_Tumor_Lower) & (dff2['Tumor_Read_Depth'] <= dff2_Tumor_Higher)]
print(dff)
print(dff1)
print(dff2)

# Final counts
dff_Counts = len(dff['Normal_Read_Depth'].index)
dff1_Counts = len(dff1['Normal_Read_Depth'].index)
dff2_Counts = len(dff2['Normal_Read_Depth'].index)

# Filtered reads
dff_Toll = dff_Count - dff_Counts
dff1_Toll = dff1_Count - dff1_Counts
dff2_Toll = dff2_Count - dff2_Counts

# Converting the values to a list
a1 = [dff_Counts, dff_Toll]
a2 = [dff1_Counts, dff1_Toll]
a3 = [dff2_Counts, dff2_Toll]

# Getting plots
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Selected_Count', 'Filtered_Count']
explode = (0.1, 0)
colors = ['#FFD700','#FFAA1C']
ax.pie(a1, explode=explode, labels = langs, colors=colors, autopct='%1.2f%%')
ax.set_title('Read Depth Counts Percentage')
plt.savefig('Strelka3_Read_Depth.png', dpi = 300)

fig1 = plt.figure()
ax1 = fig1.add_axes([0,0,1,1])
ax1.axis('equal')
langs1 = ['Selected_Count', 'Filtered_Count']
explode1 = (0.1, 0)
colors1 = ['#FFD700','#FFAA1C']
ax1.pie(a2, explode=explode1, labels = langs1, colors=colors1, autopct='%1.2f%%')
ax1.set_title('Read Depth Counts Percentage')
plt.savefig('Strelka5_Read_Depth.png', dpi = 300)

fig2 = plt.figure()
ax2 = fig2.add_axes([0,0,1,1])
ax2.axis('equal')
langs2 = ['Selected_Count', 'Filtered_Count']
explode2 = (0.1, 0)
colors2 = ['#FFD700','#FFAA1C']
ax2.pie(a3, explode=explode2, labels = langs2, colors=colors2, autopct='%1.2f%%')
ax2.set_title('Read Depth Counts Percentage')
plt.savefig('Strelka7_Read_Depth.png', dpi = 300)
