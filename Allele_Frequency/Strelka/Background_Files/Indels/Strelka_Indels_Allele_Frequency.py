# Importing the needed packages.
import numpy as np
import pandas as pd

# The first step is to selected the neccessary columns.
# Step 1 - 'cut -f 1-2,4-5,9-11 Input.vcf > Output.vcf'

# Removing all the rows starting with a #
# Step 2 - 'sed '/^#/d' Output.vcf > Updated_Output.vcf'

# Consider the Updated_Output.vcf as input.
dff = pd.read_csv("Selected_Strelka_0.3_Indels.vcf", sep = '\t', index_col= False)
dff1 = pd.read_csv("Selected_Strelka_0.5_Indels.vcf", sep = '\t', index_col= False)
dff2 = pd.read_csv("Selected_Strelka_0.7_Indels.vcf", sep = '\t', index_col= False)

# Renaming the columns after importing the input.
dff.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'NORMAL', 'TUMOR']
dff1.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'NORMAL', 'TUMOR']
dff2.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'NORMAL', 'TUMOR']

# Concatinating the "CHROM" and "POS"
dff["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)
dff1["CHROM_POS"] = dff1['CHROM'].astype(str) + '-' + dff1['POS'].astype(str)
dff2["CHROM_POS"] = dff2['CHROM'].astype(str) + '-' + dff2['POS'].astype(str)

# Dropping of the unnecessary columns and reorganising them.
dff = dff.drop(['CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]

dff1 = dff1.drop(['CHROM', 'POS'], axis=1)
cols = dff1.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff1 = dff1[cols]

dff2 = dff2.drop(['CHROM', 'POS'], axis=1)
cols = dff2.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff2 = dff2[cols]

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Normal_DP', 'Normal_DP2', 'Normal_TAR', 'Normal_TIR', 'Normal_TOR', 'Normal_DP50', 'Normal_FDP50', 'Normal_SUBDP50', 'Normal_BCN50']] = dff['NORMAL'].str.split(':',expand=True)
dff[['Tumor_DP', 'Tumor_DP2', 'Tumor_TAR', 'Tumor_TIR', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50']] = dff['TUMOR'].str.split(':',expand=True)

dff1[['Normal_DP', 'Normal_DP2', 'Normal_TAR', 'Normal_TIR', 'Normal_TOR', 'Normal_DP50', 'Normal_FDP50', 'Normal_SUBDP50', 'Normal_BCN50']] = dff1['NORMAL'].str.split(':',expand=True)
dff1[['Tumor_DP', 'Tumor_DP2', 'Tumor_TAR', 'Tumor_TIR', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50']] = dff1['TUMOR'].str.split(':',expand=True)

dff2[['Normal_DP', 'Normal_DP2', 'Normal_TAR', 'Normal_TIR', 'Normal_TOR', 'Normal_DP50', 'Normal_FDP50', 'Normal_SUBDP50', 'Normal_BCN50']] = dff2['NORMAL'].str.split(':',expand=True)
dff2[['Tumor_DP', 'Tumor_DP2', 'Tumor_TAR', 'Tumor_TIR', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50']] = dff2['TUMOR'].str.split(':',expand=True)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['FORMAT', 'NORMAL', 'TUMOR', 'Normal_DP', 'Normal_DP2', 'Normal_TOR', 'Normal_DP50', 'Normal_FDP50', 'Normal_SUBDP50', 'Normal_BCN50', 'Tumor_DP', 'Tumor_DP2', 'Tumor_DP2', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50'], axis=1)

dff1 = dff1.drop(['FORMAT', 'NORMAL', 'TUMOR', 'Normal_DP', 'Normal_DP2', 'Normal_TOR', 'Normal_DP50', 'Normal_FDP50', 'Normal_SUBDP50', 'Normal_BCN50', 'Tumor_DP', 'Tumor_DP2', 'Tumor_DP2', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50'], axis=1)

dff2 = dff2.drop(['FORMAT', 'NORMAL', 'TUMOR', 'Normal_DP', 'Normal_DP2', 'Normal_TOR', 'Normal_DP50', 'Normal_FDP50', 'Normal_SUBDP50', 'Normal_BCN50', 'Tumor_DP', 'Tumor_DP2', 'Tumor_DP2', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50'], axis=1)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Normal_TAR_First', 'Normal_TAR_Second']] = dff['Normal_TAR'].str.split(',',expand=True)
dff[['Normal_TIR_First', 'Normal_TIR_Second']] = dff['Normal_TIR'].str.split(',',expand=True)
dff[['Tumor_TAR_First', 'Tumor_TAR_Second']] = dff['Tumor_TAR'].str.split(',',expand=True)
dff[['Tumor_TIR_First', 'Tumor_TIR_Second']] = dff['Tumor_TIR'].str.split(',',expand=True)

dff1[['Normal_TAR_First', 'Normal_TAR_Second']] = dff1['Normal_TAR'].str.split(',',expand=True)
dff1[['Normal_TIR_First', 'Normal_TIR_Second']] = dff1['Normal_TIR'].str.split(',',expand=True)
dff1[['Tumor_TAR_First', 'Tumor_TAR_Second']] = dff1['Tumor_TAR'].str.split(',',expand=True)
dff1[['Tumor_TIR_First', 'Tumor_TIR_Second']] = dff1['Tumor_TIR'].str.split(',',expand=True)

dff2[['Normal_TAR_First', 'Normal_TAR_Second']] = dff2['Normal_TAR'].str.split(',',expand=True)
dff2[['Normal_TIR_First', 'Normal_TIR_Second']] = dff2['Normal_TIR'].str.split(',',expand=True)
dff2[['Tumor_TAR_First', 'Tumor_TAR_Second']] = dff2['Tumor_TAR'].str.split(',',expand=True)
dff2[['Tumor_TIR_First', 'Tumor_TIR_Second']] = dff2['Tumor_TIR'].str.split(',',expand=True)

# Renaming the new table with column names.
dff.columns = ['CHROM_POS', 'REF', 'ALT', 'Normal_TAR', 'Normal_TIR', 'Tumor_TAR', 'Tumor_TAR', 'Normal_TAR_First', 'Normal_TAR_Second', 'Normal_TIR_First', 'Normal_TIR_Second', 'Tumor_TAR_First', 'Tumor_TAR_Second', 'Tumor_TIR_First', 'Tumor_TIR_Second']

dff1.columns = ['CHROM_POS', 'REF', 'ALT', 'Normal_TAR', 'Normal_TIR', 'Tumor_TAR', 'Tumor_TAR', 'Normal_TAR_First', 'Normal_TAR_Second', 'Normal_TIR_First', 'Normal_TIR_Second', 'Tumor_TAR_First', 'Tumor_TAR_Second', 'Tumor_TIR_First', 'Tumor_TIR_Second']

dff2.columns = ['CHROM_POS', 'REF', 'ALT', 'Normal_TAR', 'Normal_TIR', 'Tumor_TAR', 'Tumor_TAR', 'Normal_TAR_First', 'Normal_TAR_Second', 'Normal_TIR_First', 'Normal_TIR_Second', 'Tumor_TAR_First', 'Tumor_TAR_Second', 'Tumor_TIR_First', 'Tumor_TIR_Second']

# Dropping of the unnecessary columns and reorganising them.
dff = dff.drop(['Normal_TAR_Second', 'Normal_TIR_Second', 'Tumor_TAR_Second', 'Tumor_TIR_Second'], axis=1)
print(dff)

dff1 = dff1.drop(['Normal_TAR_Second', 'Normal_TIR_Second', 'Tumor_TAR_Second', 'Tumor_TIR_Second'], axis=1)
print(dff1)

dff2 = dff2.drop(['Normal_TAR_Second', 'Normal_TIR_Second', 'Tumor_TAR_Second', 'Tumor_TIR_Second'], axis=1)
print(dff2)

# Converting string values columns to int for calculations.
dff['Normal_TAR_First'] = dff['Normal_TAR_First'].astype(int)
dff['Normal_TIR_First'] = dff['Normal_TIR_First'].astype(int)
dff['Tumor_TAR_First'] = dff['Tumor_TAR_First'].astype(int)
dff['Tumor_TIR_First'] = dff['Tumor_TIR_First'].astype(int)

dff1['Normal_TAR_First'] = dff1['Normal_TAR_First'].astype(int)
dff1['Normal_TIR_First'] = dff1['Normal_TIR_First'].astype(int)
dff1['Tumor_TAR_First'] = dff1['Tumor_TAR_First'].astype(int)
dff1['Tumor_TIR_First'] = dff1['Tumor_TIR_First'].astype(int)

dff2['Normal_TAR_First'] = dff2['Normal_TAR_First'].astype(int)
dff2['Normal_TIR_First'] = dff2['Normal_TIR_First'].astype(int)
dff2['Tumor_TAR_First'] = dff2['Tumor_TAR_First'].astype(int)
dff2['Tumor_TIR_First'] = dff2['Tumor_TIR_First'].astype(int)

# Adding the values for the formula.
dff['SUM'] = dff["Normal_TAR_First"] + dff["Normal_TIR_First"]
dff['COMMON'] = dff["Tumor_TAR_First"] + dff["Tumor_TIR_First"]
print(dff)

dff1['SUM'] = dff1["Normal_TAR_First"] + dff1["Normal_TIR_First"]
dff1['COMMON'] = dff1["Tumor_TAR_First"] + dff1["Tumor_TIR_First"]
print(dff1)

dff2['SUM'] = dff2["Normal_TAR_First"] + dff2["Normal_TIR_First"]
dff2['COMMON'] = dff2["Tumor_TAR_First"] + dff2["Tumor_TIR_First"]
print(dff2)

# Getting Allele Frequency
dff['Normal_Allele_Frequency'] = dff['Normal_TIR_First']/dff['SUM']
dff['Tumor_Allele_Frequency'] = dff['Tumor_TIR_First']/dff['COMMON']

dff1['Normal_Allele_Frequency'] = dff1['Normal_TIR_First']/dff1['SUM']
dff1['Tumor_Allele_Frequency'] = dff1['Tumor_TIR_First']/dff1['COMMON']

dff2['Normal_Allele_Frequency'] = dff2['Normal_TIR_First']/dff2['SUM']
dff2['Tumor_Allele_Frequency'] = dff2['Tumor_TIR_First']/dff2['COMMON']

# Converting string values columans to int.
dff['Normal_Allele_Frequency'] = dff['Normal_Allele_Frequency'].astype(float).round(2)
dff['Tumor_Allele_Frequency'] = dff['Tumor_Allele_Frequency'].astype(float).round(2)

dff1['Normal_Allele_Frequency'] = dff1['Normal_Allele_Frequency'].astype(float).round(2)
dff1['Tumor_Allele_Frequency'] = dff1['Tumor_Allele_Frequency'].astype(float).round(2)

dff2['Normal_Allele_Frequency'] = dff2['Normal_Allele_Frequency'].astype(float).round(2)
dff2['Tumor_Allele_Frequency'] = dff2['Tumor_Allele_Frequency'].astype(float).round(2)

# Concatinating the "CHROM" and "POS"
dff["Normal_Allele_Frequency"] = dff['REF'].astype(str) + ':' + dff['Normal_Allele_Frequency'].astype(str)
dff["Tumor_Allele_Frequency"] = dff['REF'].astype(str) + ':' + dff['Tumor_Allele_Frequency'].astype(str)

dff1["Normal_Allele_Frequency"] = dff1['REF'].astype(str) + ':' + dff1['Normal_Allele_Frequency'].astype(str)
dff1["Tumor_Allele_Frequency"] = dff1['REF'].astype(str) + ':' + dff1['Tumor_Allele_Frequency'].astype(str)

dff2["Normal_Allele_Frequency"] = dff2['REF'].astype(str) + ':' + dff2['Normal_Allele_Frequency'].astype(str)
dff2["Tumor_Allele_Frequency"] = dff2['REF'].astype(str) + ':' + dff2['Tumor_Allele_Frequency'].astype(str)

# Dropping of the unnecessary columns and reorganising them.
dff = dff.drop(['REF', 'ALT', 'Normal_TAR', 'Normal_TIR', 'Tumor_TAR', 'Tumor_TAR', 'Normal_TAR_First', 'Normal_TIR_First', 'Tumor_TAR_First', 'Tumor_TIR_First', 'SUM', 'COMMON'], axis=1)
print(dff)

dff1 = dff1.drop(['REF', 'ALT', 'Normal_TAR', 'Normal_TIR', 'Tumor_TAR', 'Tumor_TAR', 'Normal_TAR_First', 'Normal_TIR_First', 'Tumor_TAR_First', 'Tumor_TIR_First', 'SUM', 'COMMON'], axis=1)
print(dff1)

dff2 = dff2.drop(['REF', 'ALT', 'Normal_TAR', 'Normal_TIR', 'Tumor_TAR', 'Tumor_TAR', 'Normal_TAR_First', 'Normal_TIR_First', 'Tumor_TAR_First', 'Tumor_TIR_First', 'SUM', 'COMMON'], axis=1)
print(dff2)

# Merging columns based on "CHROM-POS"
First = pd.merge(dff, dff1, on=['CHROM_POS'])
Second = pd.merge(First, dff2, on=['CHROM_POS'])

# Renaming Columns
Second.columns = ['CHROM_POS', 'Strelka_Normal_0.3', 'Strelka_Tumor_0.3', 'Strelka_0.5_Normal', 'Strelka_0.5_Tumor', 'Strelka_0.7_Normal', 'Strelka_0.7_Tumor']
print(Second)

# Saving the results in csv.
Second.to_csv('Strelka_Allele_Frequency.csv', sep=',', index = None)