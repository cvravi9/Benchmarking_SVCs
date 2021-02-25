# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_Somatic_AF_Values.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_Somatic_AF_Values.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['CHROM_POS'])

# Assigning column names.
First.columns = ['CHROM_POS', 'Strelka_Miracum_0.4', 'Strelka_Miracum_0.7', 'Strelka_Somatic_0.4', 'Strelka_Somatic_0.7', 'VarScan_Miracum_0.4', 'VarScan_Miracum_0.7', 'VarScan_Somatic_0.4', 'VarScan_Somatic_0.7']
Second = First.drop(['CHROM_POS', 'Strelka_Miracum_0.4', 'Strelka_Somatic_0.4', 'Strelka_Somatic_0.7', 'VarScan_Miracum_0.4', 'VarScan_Somatic_0.4', 'VarScan_Somatic_0.7'], axis=1)
print(Second)

# Saving the results in csv.
Second.to_csv('All_Somatic_Miracum_0.7.csv', sep='\t', index=False, encoding='utf-8')
Second.to_csv('All_Somatic_Miracum_0.7_Plot.csv', sep='\t', index = None)
