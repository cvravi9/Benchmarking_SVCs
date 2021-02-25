# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("FreeBayes_Germline_AF_Values.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("Strelka_Germline_AF_Values.csv", sep = '\t', index_col= False)
df2 = pd.read_csv("VarScan_Germline_AF_Values.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['CHROM_POS'])
Second = pd.merge(First, df2, on=['CHROM_POS'])

# Assigning column names.
Second.columns = ['CHROM_POS', 'FreeBayes_Miracum_0.4', 'FreeBayes_Miracum_0.7', 'FreeBayes_Somatic_0.4', 'FreeBayes_Somatic_0.7', 'Strelka_Miracum_0.4', 'Strelka_Miracum_0.7', 'Strelka_Somatic_0.4', 'Strelka_Somatic_0.7', 'VarScan_Miracum_0.4', 'VarScan_Miracum_0.7', 'VarScan_Somatic_0.4', 'VarScan_Somatic_0.7']
Third = Second.drop(['CHROM_POS', 'FreeBayes_Miracum_0.4', 'FreeBayes_Miracum_0.7', 'FreeBayes_Somatic_0.7', 'Strelka_Miracum_0.4', 'Strelka_Miracum_0.7', 'Strelka_Somatic_0.7', 'VarScan_Miracum_0.4', 'VarScan_Miracum_0.7', 'VarScan_Somatic_0.7'], axis=1)
print(Third)

# Saving the results in csv.
Third.to_csv('All_Germline_Somatic_0.4.csv', sep='\t', index=False, encoding='utf-8')
Third.to_csv('All_Germline_Somatic_0.4_Plot.csv', sep='\t', index = None)
