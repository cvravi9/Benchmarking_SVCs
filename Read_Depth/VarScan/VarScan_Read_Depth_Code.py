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
Second.columns = ['CHROM_POS', 'VarScan_Normal_0.3', 'VarScan_Tumor_0.3', 'VarScan_0.5_Normal', 'VarScan_0.5_Tumor', 'VarScan_0.7_Normal', 'VarScan_0.7_Tumor']
print(Second)

# Saving the results in csv.
Second.to_csv('VarScan_Read_Depth_Counts.csv', sep=',', index = None)
