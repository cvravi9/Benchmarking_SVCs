# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_Read_Depth_Counts.csv", sep = ',', index_col= False)
df1 = pd.read_csv("VarScan_Read_Depth_Counts.csv", sep = ',', index_col= False)
df2 = pd.read_csv("Truth_Data_Read_Depth_Counts.csv", sep = ',', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['CHROM_POS'])
Second = pd.merge(First, df2, on=['CHROM_POS'])

# Assigning column names.
Second.columns = ['CHROM_POS', 'Strelka_Normal_0.3_Read_Depth', 'Strelka_Tumor_0.3_Read_Depth', 'Strelka_Normal_0.5_Read_Depth', 'Strelka_Tumor_0.5_Read_Depth', 'Strelka_Normal_0.7_Read_Depth', 'Strelka_Tumor_0.7_Read_Depth', 'VarScan_Normal_0.3_Read_Depth', 'VarScan_Tumor_0.3_Read_Depth', 'VarScan_Normal_0.5_Read_Depth', 'VarScan_Tumor_0.5_Read_Depth', 'VarScan_Normal_0.7_Read_Depth', 'VarScan_Tumor_0.7_Read_Depth', 'Somatic_Truth_Read_Depth']

# Deleting the unneeded columns.
Second = Second.drop(['Strelka_Normal_0.3_Read_Depth', 'Strelka_Tumor_0.3_Read_Depth', 'Strelka_Normal_0.7_Read_Depth', 'Strelka_Tumor_0.7_Read_Depth', 'VarScan_Normal_0.3_Read_Depth', 'VarScan_Tumor_0.3_Read_Depth', 'VarScan_Normal_0.7_Read_Depth', 'VarScan_Tumor_0.7_Read_Depth'], axis=1)
print(Second)

# Saving the results in csv.
Second.to_csv('Tumor_Purity_0.5_Read_Depths.csv', sep=',', index=False)

Second.columns = ['CHROM_POS', 'Strelka_Normal', 'Strelka_Tumor', 'VarScan_Normal', 'VarScan_Tumor', 'Truth_Data']
print(Second)

# Finding the minimum values
min1 = Second['Strelka_Normal'].min()
min2 = Second['Strelka_Tumor'].min()
min3 = Second['VarScan_Normal'].min()
min4 = Second['VarScan_Tumor'].min()
min5 = Second['Truth_Data'].min()

# Finding the maximum values
max1 = Second['Strelka_Normal'].max()
max2 = Second['Strelka_Tumor'].max()
max3 = Second['VarScan_Normal'].max()
max4 = Second['VarScan_Tumor'].max()
max5 = Second['Truth_Data'].max()

# Finding the mean values
mean1 = Second['Strelka_Normal'].mean()
mean2 = Second['Strelka_Tumor'].mean()
mean3 = Second['VarScan_Normal'].mean()
mean4 = Second['VarScan_Tumor'].mean()
mean5 = Second['Truth_Data'].mean()

# Finding the minimum values
median1 = Second['Strelka_Normal'].median()
median2 = Second['Strelka_Tumor'].median()
median3 = Second['VarScan_Normal'].median()
median4 = Second['VarScan_Tumor'].median()
median5 = Second['Truth_Data'].median()

# Finding the minimum values
mode1 = Second['Strelka_Normal'].mode()
mode2 = Second['Strelka_Tumor'].mode()
mode3 = Second['VarScan_Normal'].mode()
mode4 = Second['VarScan_Tumor'].mode()
mode5 = Second['Truth_Data'].mode()

# Delcaring a new dataframe.
df = pd.DataFrame()

# Taking all combinations as a list.
Type = ['Strelka_Normal_0.5', 'Strelka_Tumor_0.5', 'VarScan_Normal_0.5', 'VarScan_Tumor_0.5', 'Truth_Data']
Minimum_Value = [min1, min2, min3, min4, min5]
Maximum_Value = [max1, max2, max3, max4, max5]
Mean_Value = [mean1, mean2, mean3, mean4, mean5]
Median_Value = [median1, median2, median3, median4, median5]
Mode_Value = [mode1, mode2, mode3, mode4, mode5]

# Adding columns
df['Type'] = Type
df['Minimum_Value'] = Minimum_Value
df['Maximum_Value'] = Maximum_Value
df['Mean_Value'] = Mean_Value
df['Median_Value'] = Median_Value
df['Mode_Value'] = Mode_Value
# Collecting it into a dataframe.
print(df)

# Saving the results in csv.
df.to_csv('Tumor_Purity_0.5_Read_Depth_Statistics.csv', sep=',', index = False)
