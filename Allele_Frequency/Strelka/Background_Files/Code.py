# Importing the needed packages.
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import rc
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'serif'
import matplotlib.pyplot as plt
import csv

matplotlib.rcParams['font.sans-serif'] = ['Computer Modern Roman', 'sans-serif']

# The first step is to selected the neccessary columns.
# Step 1 - 'cut -f 1-2,4-5,9-11 Input.vcf > Output.vcf'

# Removing all the rows starting with a #
# Step 2 - 'sed '/^#/d' Output.vcf > Updated_Output.vcf'

# Consider the Updated_Output.vcf as input.
dff = pd.read_csv("Updated_Strelka_0.3_INDEL.vcf", sep = '\t', index_col= False)
dff1 = pd.read_csv("Updated_Strelka_0.5_INDEL.vcf", sep = '\t', index_col= False)
dff2 = pd.read_csv("Updated_Strelka_0.7_INDEL.vcf", sep = '\t', index_col= False)

# Renaming the columns after importing the input.
dff.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'TUMOR']
dff1.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'TUMOR']
dff2.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'TUMOR']

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

# Creating new columns by splitting the "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Tumor_DP', 'Tumor_DP2', 'Tumor_TAR', 'Tumor_TIR', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50']] = dff['TUMOR'].str.split(':',expand=True)
dff1[['Tumor_DP', 'Tumor_DP2', 'Tumor_TAR', 'Tumor_TIR', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50']] = dff1['TUMOR'].str.split(':',expand=True)
dff2[['Tumor_DP', 'Tumor_DP2', 'Tumor_TAR', 'Tumor_TIR', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50']] = dff2['TUMOR'].str.split(':',expand=True)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['FORMAT', 'TUMOR', 'Tumor_DP', 'Tumor_DP2', 'Tumor_DP2', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50'], axis=1)
dff1 = dff1.drop(['FORMAT', 'TUMOR', 'Tumor_DP', 'Tumor_DP2', 'Tumor_DP2', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50'], axis=1)
dff2 = dff2.drop(['FORMAT', 'TUMOR', 'Tumor_DP', 'Tumor_DP2', 'Tumor_DP2', 'Tumor_TOR', 'Tumor_DP50', 'Tumor_FDP50', 'Tumor_SUBDP50', 'Tumor_BCN50'], axis=1)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Tumor_TAR_First', 'Tumor_TAR_Second']] = dff['Tumor_TAR'].str.split(',',expand=True)
dff[['Tumor_TIR_First', 'Tumor_TIR_Second']] = dff['Tumor_TIR'].str.split(',',expand=True)

dff1[['Tumor_TAR_First', 'Tumor_TAR_Second']] = dff1['Tumor_TAR'].str.split(',',expand=True)
dff1[['Tumor_TIR_First', 'Tumor_TIR_Second']] = dff1['Tumor_TIR'].str.split(',',expand=True)

dff2[['Tumor_TAR_First', 'Tumor_TAR_Second']] = dff2['Tumor_TAR'].str.split(',',expand=True)
dff2[['Tumor_TIR_First', 'Tumor_TIR_Second']] = dff2['Tumor_TIR'].str.split(',',expand=True)

# Renaming the new table with column names.
dff.columns = ['CHROM_POS', 'REF', 'ALT', 'Tumor_TAR', 'Tumor_TAR', 'Tumor_TAR_First', 'Tumor_TAR_Second', 'Tumor_TIR_First', 'Tumor_TIR_Second']
dff1.columns = ['CHROM_POS', 'REF', 'ALT', 'Tumor_TAR', 'Tumor_TAR', 'Tumor_TAR_First', 'Tumor_TAR_Second', 'Tumor_TIR_First', 'Tumor_TIR_Second']
dff2.columns = ['CHROM_POS', 'REF', 'ALT', 'Tumor_TAR', 'Tumor_TAR', 'Tumor_TAR_First', 'Tumor_TAR_Second', 'Tumor_TIR_First', 'Tumor_TIR_Second']

# Dropping of the unnecessary columns and reorganising them.
dff = dff.drop(['Tumor_TAR_Second', 'Tumor_TIR_Second'], axis=1)
print(dff)

dff1 = dff1.drop(['Tumor_TAR_Second', 'Tumor_TIR_Second'], axis=1)
print(dff1)

dff2 = dff2.drop(['Tumor_TAR_Second', 'Tumor_TIR_Second'], axis=1)
print(dff2)

# Converting string values columns to int for calculations.
dff['Tumor_TAR_First'] = dff['Tumor_TAR_First'].astype(int)
dff['Tumor_TIR_First'] = dff['Tumor_TIR_First'].astype(int)

dff1['Tumor_TAR_First'] = dff1['Tumor_TAR_First'].astype(int)
dff1['Tumor_TIR_First'] = dff1['Tumor_TIR_First'].astype(int)

dff2['Tumor_TAR_First'] = dff2['Tumor_TAR_First'].astype(int)
dff2['Tumor_TIR_First'] = dff2['Tumor_TIR_First'].astype(int)

# Adding the values for the formula.
dff['COMMON'] = dff["Tumor_TAR_First"] + dff["Tumor_TIR_First"]
print(dff)

dff1['COMMON'] = dff1["Tumor_TAR_First"] + dff1["Tumor_TIR_First"]
print(dff1)

dff2['COMMON'] = dff2["Tumor_TAR_First"] + dff2["Tumor_TIR_First"]
print(dff2)

# Getting Allele Frequency
dff['Tumor_Allele_Frequency'] = dff['Tumor_TIR_First']/dff['COMMON']
dff1['Tumor_Allele_Frequency'] = dff1['Tumor_TIR_First']/dff1['COMMON']
dff2['Tumor_Allele_Frequency'] = dff2['Tumor_TIR_First']/dff2['COMMON']

# Converting string values columans to int.
dff['Tumor_Allele_Frequency'] = dff['Tumor_Allele_Frequency'].astype(float).round(2)
dff1['Tumor_Allele_Frequency'] = dff1['Tumor_Allele_Frequency'].astype(float).round(2)
dff2['Tumor_Allele_Frequency'] = dff2['Tumor_Allele_Frequency'].astype(float).round(2)

# Concatinating the "CHROM" and "POS"
dff["Tumor_Allele_Frequency"] = dff['REF'].astype(str) + ':' + dff['Tumor_Allele_Frequency'].astype(str)
dff1["Tumor_Allele_Frequency"] = dff1['REF'].astype(str) + ':' + dff1['Tumor_Allele_Frequency'].astype(str)
dff2["Tumor_Allele_Frequency"] = dff2['REF'].astype(str) + ':' + dff2['Tumor_Allele_Frequency'].astype(str)

# Dropping of the unnecessary columns and reorganising them.
dff = dff.drop(['REF', 'ALT', 'Tumor_TAR', 'Tumor_TAR', 'Tumor_TAR_First', 'Tumor_TIR_First', 'COMMON'], axis=1)
print(dff)

dff1 = dff1.drop(['REF', 'ALT', 'Tumor_TAR', 'Tumor_TAR', 'Tumor_TAR_First', 'Tumor_TIR_First', 'COMMON'], axis=1)
print(dff1)

dff2 = dff2.drop(['REF', 'ALT', 'Tumor_TAR', 'Tumor_TAR', 'Tumor_TAR_First', 'Tumor_TIR_First', 'COMMON'], axis=1)
print(dff2)

# Saving the results in csv.
dff.to_csv('Strelka3_INDEL_AF.csv', sep=',', index = False)
dff1.to_csv('Strelka5_INDEL_AF.csv', sep=',', index = False)
dff2.to_csv('Strelka7_INDEL_AF.csv', sep=',', index = False)

# The second step if to eliminate all lines that start with a '#'
dfff = pd.read_csv("Updated_Strelka_0.3_SNV.vcf", sep = '\t', index_col= False)
dfff1 = pd.read_csv("Updated_Strelka_0.5_SNV.vcf", sep = '\t', index_col= False)
dfff2 = pd.read_csv("Updated_Strelka_0.7_SNV.vcf", sep = '\t', index_col= False)

# Naming the columns after importing the csv file.
dfff.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'TUMOR']
dfff1.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'TUMOR']
dfff2.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'TUMOR']

# Concatinating the "CHROM" and "POS"
dfff["CHROM_POS"] = dfff['CHROM'].astype(str) + '-' + dfff['POS'].astype(str)
dfff1["CHROM_POS"] = dfff1['CHROM'].astype(str) + '-' + dfff1['POS'].astype(str)
dfff2["CHROM_POS"] = dfff2['CHROM'].astype(str) + '-' + dfff2['POS'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
dfff = dfff.drop(['CHROM', 'POS'], axis=1)
cols = dfff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dfff = dfff[cols]

dfff1 = dfff1.drop(['CHROM', 'POS'], axis=1)
cols = dfff1.columns.tolist()
cols = cols[-1:] + cols[:-1]
dfff1 = dfff1[cols]

dfff2 = dfff2.drop(['CHROM', 'POS'], axis=1)
cols = dfff2.columns.tolist()
cols = cols[-1:] + cols[:-1]
dfff2 = dfff2[cols]

# Adding columns for single read depth value.
dfff['REF_U'] = dfff["REF"] + "U"
dfff['ALT_U'] = dfff["ALT"] + "U"

dfff1['REF_U'] = dfff1["REF"] + "U"
dfff1['ALT_U'] = dfff1["ALT"] + "U"

dfff2['REF_U'] = dfff2["REF"] + "U"
dfff2['ALT_U'] = dfff2["ALT"] + "U"

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dfff[['Tumor_DP', 'Tumor_FDP', 'Tumor_SDP', 'Tumor_SUBDP', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU']] = dfff['TUMOR'].str.split(':',expand=True)
dfff1[['Tumor_DP', 'Tumor_FDP', 'Tumor_SDP', 'Tumor_SUBDP', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU']] = dfff1['TUMOR'].str.split(':',expand=True)
dfff2[['Tumor_DP', 'Tumor_FDP', 'Tumor_SDP', 'Tumor_SUBDP', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU']] = dfff2['TUMOR'].str.split(':',expand=True)

# Dropping of the unnecessary columns and reorganising the columns.
dfff = dfff.drop(['FORMAT', 'TUMOR', 'Tumor_DP', 'Tumor_FDP', 'Tumor_SDP', 'Tumor_SUBDP'], axis=1)
dfff1 = dfff1.drop(['FORMAT', 'TUMOR', 'Tumor_DP', 'Tumor_FDP', 'Tumor_SDP', 'Tumor_SUBDP'], axis=1)
dfff2 = dfff2.drop(['FORMAT', 'TUMOR', 'Tumor_DP', 'Tumor_FDP', 'Tumor_SDP', 'Tumor_SUBDP'], axis=1)

for i in dfff['CHROM_POS']:
    dfff.loc[dfff['REF_U'] == 'AU', 'REF_Tumor'] = dfff.Tumor_AU
    dfff.loc[dfff['REF_U'] == 'CU', 'REF_Tumor'] = dfff.Tumor_CU
    dfff.loc[dfff['REF_U'] == 'GU', 'REF_Tumor'] = dfff.Tumor_GU
    dfff.loc[dfff['REF_U'] == 'TU', 'REF_Tumor'] = dfff.Tumor_TU
    dfff.loc[dfff['ALT_U'] == 'AU', 'ALT_Tumor'] = dfff.Tumor_AU
    dfff.loc[dfff['ALT_U'] == 'CU', 'ALT_Tumor'] = dfff.Tumor_CU
    dfff.loc[dfff['ALT_U'] == 'GU', 'ALT_Tumor'] = dfff.Tumor_GU
    dfff.loc[dfff['ALT_U'] == 'TU', 'ALT_Tumor'] = dfff.Tumor_TU
print(dfff)

for i in dff1['CHROM_POS']:
    dfff1.loc[dfff1['REF_U'] == 'AU', 'REF_Tumor'] = dfff1.Tumor_AU
    dfff1.loc[dfff1['REF_U'] == 'CU', 'REF_Tumor'] = dfff1.Tumor_CU
    dfff1.loc[dfff1['REF_U'] == 'GU', 'REF_Tumor'] = dfff1.Tumor_GU
    dfff1.loc[dfff1['REF_U'] == 'TU', 'REF_Tumor'] = dfff1.Tumor_TU
    dfff1.loc[dfff1['ALT_U'] == 'AU', 'ALT_Tumor'] = dfff1.Tumor_AU
    dfff1.loc[dfff1['ALT_U'] == 'CU', 'ALT_Tumor'] = dfff1.Tumor_CU
    dfff1.loc[dfff1['ALT_U'] == 'GU', 'ALT_Tumor'] = dfff1.Tumor_GU
    dfff1.loc[dfff1['ALT_U'] == 'TU', 'ALT_Tumor'] = dfff1.Tumor_TU
print(dfff1)

for i in dff2['CHROM_POS']:
    dfff2.loc[dfff2['REF_U'] == 'AU', 'REF_Tumor'] = dfff2.Tumor_AU
    dfff2.loc[dfff2['REF_U'] == 'CU', 'REF_Tumor'] = dfff2.Tumor_CU
    dfff2.loc[dfff2['REF_U'] == 'GU', 'REF_Tumor'] = dfff2.Tumor_GU
    dfff2.loc[dfff2['REF_U'] == 'TU', 'REF_Tumor'] = dfff2.Tumor_TU
    dfff2.loc[dfff2['ALT_U'] == 'AU', 'ALT_Tumor'] = dfff2.Tumor_AU
    dfff2.loc[dfff2['ALT_U'] == 'CU', 'ALT_Tumor'] = dfff2.Tumor_CU
    dfff2.loc[dfff2['ALT_U'] == 'GU', 'ALT_Tumor'] = dfff2.Tumor_GU
    dfff2.loc[dfff2['ALT_U'] == 'TU', 'ALT_Tumor'] = dfff2.Tumor_TU
print(dfff2)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dfff[['REF_Tumor_First', 'REF_Tumor_Second']] = dfff['REF_Tumor'].str.split(',',expand=True)
dfff[['ALT_Tumor_First', 'ALT_Tumor_Second']] = dfff['ALT_Tumor'].str.split(',',expand=True)
print(dfff)

dfff1[['REF_Tumor_First', 'REF_Tumor_Second']] = dfff1['REF_Tumor'].str.split(',',expand=True)
dfff1[['ALT_Tumor_First', 'ALT_Tumor_Second']] = dfff1['ALT_Tumor'].str.split(',',expand=True)
print(dfff1)

dfff2[['REF_Tumor_First', 'REF_Tumor_Second']] = dfff2['REF_Tumor'].str.split(',',expand=True)
dfff2[['ALT_Tumor_First', 'ALT_Tumor_Second']] = dfff2['ALT_Tumor'].str.split(',',expand=True)
print(dfff2)

# Dropping of the unnecessary columns and reorganising the columns.
dfff = dfff.drop(['REF_U', 'ALT_U', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU', 'REF_Tumor_Second', 'ALT_Tumor_Second'], axis=1)
print(dfff)

dfff1 = dfff1.drop(['REF_U', 'ALT_U', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU', 'REF_Tumor_Second', 'ALT_Tumor_Second'], axis=1)
print(dfff1)

dfff2 = dfff2.drop(['REF_U', 'ALT_U', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU', 'REF_Tumor_Second', 'ALT_Tumor_Second'], axis=1)
print(dfff2)

# Naming the columns after importing the csv file.
dfff.columns = ['CHROM_POS', 'REF', 'ALT', 'REF_Tumor', 'ALT_Tumor', 'REF_Tumor_First', 'ALT_Tumor_First']
print(dfff)

dfff1.columns = ['CHROM_POS', 'REF', 'ALT', 'REF_Tumor', 'ALT_Tumor', 'REF_Tumor_First', 'ALT_Tumor_First']
print(dfff1)

dfff2.columns = ['CHROM_POS', 'REF', 'ALT', 'REF_Tumor', 'ALT_Tumor', 'REF_Tumor_First', 'ALT_Tumor_First']
print(dfff2)

# Converting string values columns to int.
dfff['REF_Tumor_First'] = dfff['REF_Tumor_First'].astype(int)
dfff['ALT_Tumor_First'] = dfff['ALT_Tumor_First'].astype(int)
print(dfff)

dfff1['REF_Tumor_First'] = dfff1['REF_Tumor_First'].astype(int)
dfff1['ALT_Tumor_First'] = dfff1['ALT_Tumor_First'].astype(int)
print(dfff1)

dfff2['REF_Tumor_First'] = dfff2['REF_Tumor_First'].astype(int)
dfff2['ALT_Tumor_First'] = dfff2['ALT_Tumor_First'].astype(int)
print(dfff2)

# Adding the values for formula.
dfff['COMMON'] = dfff["REF_Tumor_First"] + dfff["ALT_Tumor_First"]
dfff1['COMMON'] = dfff1["REF_Tumor_First"] + dfff1["ALT_Tumor_First"]
dfff2['COMMON'] = dfff2["REF_Tumor_First"] + dfff2["ALT_Tumor_First"]

# Getting Allele Frequency
dfff['Tumor'] = dfff['ALT_Tumor_First']/dfff['COMMON']
dfff1['Tumor'] = dfff1['ALT_Tumor_First']/dfff1['COMMON']
dfff2['Tumor'] = dfff2['ALT_Tumor_First']/dfff2['COMMON']

# Converting string values columans to int.
dfff['Tumor'] = dfff['Tumor'].astype(float).round(2)
dfff1['Tumor'] = dfff1['Tumor'].astype(float).round(2)
dfff2['Tumor'] = dfff2['Tumor'].astype(float).round(2)

# Concatinating the "CHROM" and "POS"
dfff["Tumor"] = dfff['REF'].astype(str) + ':' + dfff['Tumor'].astype(str)
dfff1["Tumor"] = dfff1['REF'].astype(str) + ':' + dfff1['Tumor'].astype(str)
dfff2["Tumor"] = dfff2['REF'].astype(str) + ':' + dfff2['Tumor'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
dfff = dfff.drop(['REF', 'ALT', 'REF_Tumor', 'ALT_Tumor', 'REF_Tumor_First', 'ALT_Tumor_First', 'COMMON'], axis=1)
dfff1 = dfff1.drop(['REF', 'ALT', 'REF_Tumor', 'ALT_Tumor', 'REF_Tumor_First', 'ALT_Tumor_First', 'COMMON'], axis=1)
dfff2 = dfff2.drop(['REF', 'ALT', 'REF_Tumor', 'ALT_Tumor', 'REF_Tumor_First', 'ALT_Tumor_First', 'COMMON'], axis=1)

# Saving the results in csv.
dfff.to_csv('Strelka3_SNV_AF.csv', sep=',', index = False)
dfff1.to_csv('Strelka5_SNV_AF.csv', sep=',', index = False)
dfff2.to_csv('Strelka7_SNV_AF.csv', sep=',', index = False)
