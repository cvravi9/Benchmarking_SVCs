# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("FreeBayes_Germline_Somatic_0.4.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("Strelka_Germline_Somatic_0.4.csv", sep = '\t', index_col= False)
df2 = pd.read_csv("VarScan_Germline_Somatic_0.4.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['CHROM_POS'])
Second = pd.merge(First, df2, on=['CHROM_POS'])

# Assigning column names.
Second.columns = ['CHROM_POS', 'FreeBayes_Normal_Read_Depth', 'FreeBayes_Tumor_Read_Depth', 'Strelka_Normal_Read_Depth', 'Strelka_Tumor_Read_Depth', 'VarScan_Normal_Read_Depth', 'VarScan_Tumor_Read_Depth']
print(Second)

# Saving the results in csv.
Second.to_csv('All_Germline_Somatic_0.4_Read_Depths.csv', sep='\t', index=False, encoding='utf-8')
Second.to_csv('All_Germline_Somatic_0.4_Plot_Read_Depths.csv', sep='\t', index = None)
