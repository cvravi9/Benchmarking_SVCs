# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_0.3.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_0.3.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['CHROM_POS'])

# Assigning column names.
First.columns = ['CHROM_POS', 'Strelka_Normal_Read_Depth', 'Strelka_Tumor_Read_Depth', 'VarScan_Normal_Read_Depth', 'VarScan_Tumor_Read_Depth']
print(First)

# Saving the results in csv.
First.to_csv('Tumor_Purity_0.3_Read_Depths.csv', sep=',', index=False, encoding='utf-8')
First.to_csv('Tumor_Purity_0.3_Plot_Read_Depths.csv', sep='\t', index = None)
