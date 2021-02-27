# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_Somatic_Somatic_0.7.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_Somatic_Somatic_0.7.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['CHROM_POS'])

# Assigning column names.
First.columns = ['CHROM_POS', 'Strelka_Normal_Read_Depth', 'Strelka_Tumor_Read_Depth', 'Strelka_Normal1_Read_Depth', 'Strelka_Tumor1_Read_Depth', 'VarScan_Normal_Read_Depth', 'VarScan_Tumor_Read_Depth']
print(First)

# Saving the results in csv.
First.to_csv('All_Somatic_Somatic_0.7_Read_Depths.csv', sep=',', index=False, encoding='utf-8')
First.to_csv('All_Somatic_Somatic_0.7_Plot_Read_Depths.csv', sep='\t', index = None)
