# Importing the needed packages.
import numpy as np
import pandas as pd

# Reading the csv input file that is obtained after performing the following operations on the vcf file.
# Step 1 - 'cut -f 1-2,9-11 Input-VCF-File > Output-VCF-File'
# Step 2 - 'sed '/^#/d' Output-VCF-File > Updated_Output-VCF-File'

# The first step is to selected the needed columns in the vcf file.
# The second step if to eliminate all lines that start with a '#'
dff = pd.read_csv("Updated_VarScan_0.3.vcf", sep = '\t', index_col= False)
dff1 = pd.read_csv("Updated_VarScan_0.5.vcf", sep = '\t', index_col= False)
dff2 = pd.read_csv("Updated_VarScan_0.7.vcf", sep = '\t', index_col= False)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM', 'POS', 'FORMAT', 'NORMAL', 'TUMOR']
dff1.columns = ['CHROM', 'POS', 'FORMAT', 'NORMAL', 'TUMOR']
dff2.columns = ['CHROM', 'POS', 'FORMAT', 'NORMAL', 'TUMOR']

# Concatinating the "CHROM" and "POS"
dff["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)
dff1["CHROM_POS"] = dff1['CHROM'].astype(str) + '-' + dff1['POS'].astype(str)
dff2["CHROM_POS"] = dff2['CHROM'].astype(str) + '-' + dff2['POS'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['CHROM', 'POS', 'FORMAT'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

dff1 = dff1.drop(['CHROM', 'POS', 'FORMAT'], axis=1)
cols = dff1.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff1 = dff1[cols]
print(dff1)

dff2 = dff2.drop(['CHROM', 'POS', 'FORMAT'], axis=1)
cols = dff2.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff2 = dff2[cols]
print(dff2)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "GT:GQ:DP:AD:ADF:ADR".
dff[['NORMAL-GT','NORMAL-GQ','Normal_Read_Depth', 'NORMAL-AD','NORMAL-ADF', 'NORMAL-ADR']] = dff['NORMAL'].str.split(':',expand=True)
dff[['TUMOR-GT','TUMOR-GQ','Tumor_Read_Depth', 'TUMOR-AD','TUMOR-ADF', 'TUMOR-ADR']] = dff['TUMOR'].str.split(':',expand=True)

dff1[['NORMAL-GT','NORMAL-GQ','Normal_Read_Depth', 'NORMAL-AD','NORMAL-ADF', 'NORMAL-ADR']] = dff1['NORMAL'].str.split(':',expand=True)
dff1[['TUMOR-GT','TUMOR-GQ','Tumor_Read_Depth', 'TUMOR-AD','TUMOR-ADF', 'TUMOR-ADR']] = dff1['TUMOR'].str.split(':',expand=True)

dff2[['NORMAL-GT','NORMAL-GQ','Normal_Read_Depth', 'NORMAL-AD','NORMAL-ADF', 'NORMAL-ADR']] = dff2['NORMAL'].str.split(':',expand=True)
dff2[['TUMOR-GT','TUMOR-GQ','Tumor_Read_Depth', 'TUMOR-AD','TUMOR-ADF', 'TUMOR-ADR']] = dff2['TUMOR'].str.split(':',expand=True)

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
dff = dff.drop(['NORMAL', 'TUMOR', 'NORMAL-GT', 'NORMAL-GQ', 'NORMAL-AD', 'NORMAL-ADF', 'NORMAL-ADR', 'TUMOR-GT', 'TUMOR-GQ', 'TUMOR-AD', 'TUMOR-ADF', 'TUMOR-ADR'], axis=1)
print(dff)

dff1 = dff1.drop(['NORMAL', 'TUMOR', 'NORMAL-GT', 'NORMAL-GQ', 'NORMAL-AD', 'NORMAL-ADF', 'NORMAL-ADR', 'TUMOR-GT', 'TUMOR-GQ', 'TUMOR-AD', 'TUMOR-ADF', 'TUMOR-ADR'], axis=1)
print(dff1)

dff2 = dff2.drop(['NORMAL', 'TUMOR', 'NORMAL-GT', 'NORMAL-GQ', 'NORMAL-AD', 'NORMAL-ADF', 'NORMAL-ADR', 'TUMOR-GT', 'TUMOR-GQ', 'TUMOR-AD', 'TUMOR-ADF', 'TUMOR-ADR'], axis=1)
print(dff2)

# Merging columns based on "CHROM-POS"
First = pd.merge(dff, dff1, on=['CHROM_POS'])
Second = pd.merge(First, dff2, on=['CHROM_POS'])

# Renaming Columns
Second.columns = ['CHROM_POS', 'VarScan_Normal_0.3', 'VarScan_Tumor_0.3', 'VarScan_Normal_0.5', 'VarScan_Tumor_0.5', 'VarScan_Normal_0.7', 'VarScan_Tumor_0.7']
print(Second)

# Saving the results in csv.
Second.to_csv('VarScan_Read_Depth_Counts.csv', sep=',', index = None)

Second.columns = ['CHROM_POS', 'Third_VarScan_Normal', 'Third_VarScan_Tumor', 'Fifth_VarScan_Normal', 'Fifth_VarScan_Tumor', 'Seventh_VarScan_Normal', 'Seventh_VarScan_Tumor']

# Converting the data to Integers.
Second = Second.drop(['CHROM_POS'], axis=1)
Second = Second.astype('int')
print(Second)

# Finding the minimum values
min1 = Second['Third_VarScan_Normal'].min()
min2 = Second['Third_VarScan_Tumor'].min()
min3 = Second['Fifth_VarScan_Normal'].min()
min4 = Second['Fifth_VarScan_Tumor'].min()
min5 = Second['Seventh_VarScan_Normal'].min()
min6 = Second['Seventh_VarScan_Tumor'].min()

# Finding the maximum values
max1 = Second['Third_VarScan_Normal'].max()
max2 = Second['Third_VarScan_Tumor'].max()
max3 = Second['Fifth_VarScan_Normal'].max()
max4 = Second['Fifth_VarScan_Tumor'].max()
max5 = Second['Seventh_VarScan_Normal'].max()
max6 = Second['Seventh_VarScan_Tumor'].max()

# Finding the mean values
mean1 = Second['Third_VarScan_Normal'].mean()
mean2 = Second['Third_VarScan_Tumor'].mean()
mean3 = Second['Fifth_VarScan_Normal'].mean()
mean4 = Second['Fifth_VarScan_Tumor'].mean()
mean5 = Second['Seventh_VarScan_Normal'].mean()
mean6 = Second['Seventh_VarScan_Tumor'].mean()

# Finding the median values
median1 = Second['Third_VarScan_Normal'].median()
median2 = Second['Third_VarScan_Tumor'].median()
median3 = Second['Fifth_VarScan_Normal'].median()
median4 = Second['Fifth_VarScan_Tumor'].median()
median5 = Second['Seventh_VarScan_Normal'].median()
median6 = Second['Seventh_VarScan_Tumor'].median()

# Finding the mode values
mode1 = Second['Third_VarScan_Normal'].mode()
mode2 = Second['Third_VarScan_Tumor'].mode()
mode3 = Second['Fifth_VarScan_Normal'].mode()
mode4 = Second['Fifth_VarScan_Tumor'].mode()
mode5 = Second['Seventh_VarScan_Normal'].mode()
mode6 = Second['Seventh_VarScan_Tumor'].mode()

# Finding the standard deviation
std1 = Second['Third_VarScan_Normal'].std()
std2 = Second['Third_VarScan_Tumor'].std()
std3 = Second['Fifth_VarScan_Normal'].std()
std4 = Second['Fifth_VarScan_Tumor'].std()
std5 = Second['Seventh_VarScan_Normal'].std()
std6 = Second['Seventh_VarScan_Tumor'].std()

# Delcaring a new dataframe.
df = pd.DataFrame()

# Taking all combinations as a list.
Type = ['VarScan_Normal_0.3', 'VarScan_Tumor_0.3', 'VarScan_Normal_0.5', 'VarScan_Tumor_0.5', 'VarScan_Normal_0.7', 'VarScan_Tumor_0.7']
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
df['Standard_Deviation'] = Std_Value

# Collecting it into a dataframe.
print(df)

# Saving the results in csv.
df.to_csv('VarScan_Read_Depth_Statistics.csv', sep=',', index = False)
