# Importing the needed packages.
import numpy as np
import pandas as pd

# Reading the csv input file that is obtained after performing the following operations on the vcf file.
# Step 1 - 'cut -f 1-2,4-5,9-11 Input-VCF-File > Output-VCF-File'
# Step 2 - 'sed '/^#/d' Output-VCF-File > Updated_Output-VCF-File'

# The first step is to selected the needed columns in the vcf file.
# The second step if to eliminate all lines that start with a '#'
dff = pd.read_csv("Selected_Strelka_0.3_Indels.vcf", sep = '\t', index_col= False)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'NORMAL', 'TUMOR']

# Concatinating the "CHROM" and "POS"
dff["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Normal_DP', 'Normal_DP2', 'Normal_TAR', 'Normal_TIR', 'Normal_TOR', 'Normal_DP50', 'Normal_FDP50', 'Normal_SUBDP50', 'Normal_BCN50']] = dff['NORMAL'].str.split(':',expand=True)
dff[['Tumor_DP', 'Tumor_DP2', 'Tumor_TAR', 'Tumor_TIR', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50']] = dff['TUMOR'].str.split(':',expand=True)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['FORMAT', 'NORMAL', 'TUMOR', 'Normal_DP', 'Normal_DP2', 'Normal_TOR', 'Normal_DP50', 'Normal_FDP50', 'Normal_SUBDP50', 'Normal_BCN50', 'Tumor_DP', 'Tumor_DP2', 'Tumor_DP2', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50'], axis=1)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Normal_TAR_First', 'Normal_TAR_Second']] = dff['Normal_TAR'].str.split(',',expand=True)
dff[['Normal_TIR_First', 'Normal_TIR_Second']] = dff['Normal_TIR'].str.split(',',expand=True)
dff[['Tumor_TAR_First', 'Tumor_TAR_Second']] = dff['Tumor_TAR'].str.split(',',expand=True)
dff[['Tumor_TIR_First', 'Tumor_TIR_Second']] = dff['Tumor_TIR'].str.split(',',expand=True)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM_POS', 'REF', 'ALT', 'Normal_TAR', 'Normal_TIR', 'Tumor_TAR', 'Tumor_TAR', 'Normal_TAR_First', 'Normal_TAR_Second', 'Normal_TIR_First', 'Normal_TIR_Second', 'Tumor_TAR_First', 'Tumor_TAR_Second', 'Tumor_TIR_First', 'Tumor_TIR_Second']

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['Normal_TAR_Second', 'Normal_TIR_Second', 'Tumor_TAR_Second', 'Tumor_TIR_Second'], axis=1)
print(dff)

# Converting string values columns to int.
dff['Normal_TAR'] = dff['Normal_TAR'].astype(int)
dff['Normal_TIR'] = dff['Normal_TIR'].astype(int)
dff['Tumor_TAR'] = dff['Tumor_TAR'].astype(int)
dff['Tumor_TIR'] = dff['Tumor_TIR'].astype(int)

# Getting Allele Frequency
dff['Normal_Allele_Frequency'] = dff['Normal_TAR']/dff['Normal_TIR']
dff['Tumor_Allele_Frequency'] = dff['Tumor_TAR']/dff['Tumor_TIR']

# Converting string values columans to int.
dff['Normal_Allele_Frequency'] = dff['Normal_Allele_Frequency'].astype(float).round(2)
dff['Tumor_Allele_Frequency'] = dff['Tumor_Allele_Frequency'].astype(float).round(2)

# Concatinating the "CHROM" and "POS"
dff["Normal_Allele_Frequency"] = dff['REF'].astype(str) + ':' + dff['Normal_Allele_Frequency'].astype(str)
dff["Tumor_Allele_Frequency"] = dff['REF'].astype(str) + ':' + dff['Tumor_Allele_Frequency'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
# dff = dff.drop(['REF', 'ALT', 'NORMAL', 'TUMOR', 'SUM'], axis=1)
print(dff)

# Saving the result into a csv file for plotting.
dff.to_csv('Strelka_0.3_Indels.csv', sep=',', index=False, encoding='utf-8')
dff.to_csv('Strelka_0.3_Plot_Indels.csv', sep='\t', index = None)
