# Importing the needed packages.
import numpy as np
import pandas as pd

# Reading the csv input file that is obtained after performing the following operations on the vcf file.
# Step 1 - 'cut -f 1-2, 9-11 Input-VCF-File > Output-VCF-File'
# Step 2 - 'sed '/^#/d' Output-VCF-File > Updated_Output-VCF-File'

# The first step is to selected the needed columns in the vcf file.
# The second step if to eliminate all lines that start with a '#'
dff = pd.read_csv("Selected_Columns.vcf", sep = '\t', index_col= False)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM', 'POS', 'FORMAT', 'NORMAL', 'TUMOR']

# Concatinating the "CHROM" and "POS"
dff["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['CHROM', 'POS', 'FORMAT'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "GT:GQ:DP:AD:ADF:ADR".
dff[['NORMAL-GT', 'Normal_Read_Depth', 'NORMAL-AD','NORMAL-RO', 'NORMAL-QR', 'NORMAL-AO', 'NORMAL-QA', 'NORMAL-GL']] = dff['NORMAL'].str.split(':',expand=True)
dff[['TUMOR-GT','Tumor_Read_Depth', 'TUMOR-AD','TUMOR-RO', 'TUMOR-QR', 'TUMOR-AO', 'TUMOR-QA', 'TUMOR-GL']] = dff['TUMOR'].str.split(':',expand=True)

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
dff = dff.drop(['NORMAL', 'TUMOR', 'NORMAL-GT', 'NORMAL-AD', 'NORMAL-RO', 'NORMAL-QR', 'NORMAL-AO', 'NORMAL-QA', 'NORMAL-GL', 'TUMOR-GT', 'TUMOR-AD', 'TUMOR-RO', 'TUMOR-QR', 'TUMOR-AO', 'TUMOR-QA', 'TUMOR-GL'], axis=1)
print(dff)

# Saving the result into a csv file for plotting.
dff.to_csv('FreeBayes_Germline_Miracum_0.4.csv', sep='\t', index=False, encoding='utf-8')
dff.to_csv('FreeBayes_Germline_Miracum_0.4_Plot.csv', sep='\t', index = None)
