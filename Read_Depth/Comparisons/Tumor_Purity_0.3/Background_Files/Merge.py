# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_Read_Depth_Counts.csv", sep = ',', index_col= False)
df1 = pd.read_csv("VarScan_Read_Depth_Counts.csv", sep = ',', index_col= False)
df2 = pd.read_csv("Truth_Data_Read_Depth_Counts.csv", sep = ',', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['CHROM_POS'])
print(First)
Second = pd.merge(First, df2, on=['CHROM_POS'])

# Assigning column names.
Second.columns = ['CHROM_POS', 'Strelka_Normal_0.3_Read_Depth', 'Strelka_Tumor_0.3_Read_Depth', 'Strelka_Normal_0.5_Read_Depth', 'Strelka_Tumor_0.5_Read_Depth', 'Strelka_Normal_0.7_Read_Depth', 'Strelka_Tumor_0.7_Read_Depth', 'VarScan_Normal_0.3_Read_Depth', 'VarScan_Tumor_0.3_Read_Depth', 'VarScan_Normal_0.5_Read_Depth', 'VarScan_Tumor_0.5_Read_Depth', 'VarScan_Normal_0.7_Read_Depth', 'VarScan_Tumor_0.7_Read_Depth', 'Somatic_Truth_Read_Depth']

# Deleting the unneeded columns.
Second = Second.drop(['CHROM_POS', 'Strelka_Normal_0.5_Read_Depth', 'Strelka_Tumor_0.5_Read_Depth', 'Strelka_Normal_0.7_Read_Depth', 'Strelka_Tumor_0.7_Read_Depth', 'VarScan_Normal_0.5_Read_Depth', 'VarScan_Tumor_0.5_Read_Depth', 'VarScan_Normal_0.7_Read_Depth', 'VarScan_Tumor_0.7_Read_Depth', 'Somatic_Truth_Read_Depth'], axis=1)
print(Second)

# Saving the results in csv.
Second.to_csv('Tumor_Purity_0.3_Read_Depths.csv', sep=',', index=False)
