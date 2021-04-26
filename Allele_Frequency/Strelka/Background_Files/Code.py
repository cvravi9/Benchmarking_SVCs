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

# Merging columns based on "CHROM-POS"
# First = pd.merge(dff, dff1, on=['CHROM_POS'])
# Second = pd.merge(First, dff2, on=['CHROM_POS'])

# Renaming Columns
# Second.columns = ['CHROM_POS', 'Strelka_Normal_0.3', 'Strelka_Tumor_0.3', 'Strelka_0.5_Normal', 'Strelka_0.5_Tumor', 'Strelka_0.7_Normal', 'Strelka_0.7_Tumor']
# print(Second)

# The first step is to selected the needed columns in the vcf file.
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

# Merging columns based on "CHROM-POS"
# First = pd.merge(dff, dff1, on=['CHROM_POS'])
# Third = pd.merge(First, dff2, on=['CHROM_POS'])

# Renaming Columns
# Third.columns = ['CHROM_POS', 'Strelka_Normal_0.3', 'Strelka_Tumor_0.3', 'Strelka_0.5_Normal', 'Strelka_0.5_Tumor', 'Strelka_0.7_Normal', 'Strelka_0.7_Tumor']
# print(Third)
                                                                                               
# Assigning column names.
# Second.columns = ['CHROM_POS', 'Indel_Normal_0.3', 'Indel_Tumor_0.3', 'Indel_Normal_0.5', 'Indel_Tumor_0.5', 'Indel_Normal_0.7', 'Indel_Tumor_0.7']
# Third.columns = ['CHROM_POS', 'SNP_Normal_0.3', 'SNP_Tumor_0.3', 'SNP_Normal_0.5', 'SNP_Tumor_0.5', 'SNP_Normal_0.7', 'SNP_Tumor_0.7']
# print(Second)
# print(Third)

# Using merge function by setting how='inner'
# df = pd.merge(Second, Third, on='CHROM_POS', how='outer')
# df = []

# df = dff.merge(dfff, how='outer', on='CHROM_POS')
# print(df)

# frames = [dff, dfff]
# result = pd.concat(frames)
# print(result)
# dff['Tumor'] = df['Indel_Normal_0.3'].combine_first(df['SNP_Normal_0.3'])
# df['Tumor_0.3_AF'] = df['Indel_Tumor_0.3'].combine_first(df['SNP_Tumor_0.3'])
# df['Normal_0.5_AF'] = df['Indel_Normal_0.5'].combine_first(df['SNP_Normal_0.5'])
# df['Tumor_0.5_AF'] = df['Indel_Tumor_0.5'].combine_first(df['SNP_Tumor_0.5'])
# df['Normal_0.7_AF'] = df['Indel_Normal_0.7'].combine_first(df['SNP_Normal_0.7'])
# df['Tumor_0.7_AF'] = df['Indel_Tumor_0.7'].combine_first(df['SNP_Tumor_0.7'])
# print(df)

# Dropping unneeded columns.
# df = df.drop(['Indel_Normal_0.3', 'Indel_Tumor_0.3', 'Indel_Normal_0.5', 'Indel_Tumor_0.5', 'Indel_Normal_0.7', 'Indel_Tumor_0.7', 'SNP_Normal_0.3', 'SNP_Tumor_0.3', 'SNP_Normal_0.5', 'SNP_Tumor_0.5', 'SNP_Normal_0.7', 'SNP_Tumor_0.7'], axis=1)
# print(df) 

# Saving the result into a csv file for plotting.
# df.to_csv('Strelka_Allele_Frequency.csv', sep=',', index = False)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "GT:GQ:DP:AD:ADF:ADR".
dff[['INDEL3_Allele', 'INDEL3_Value']] = dff['Tumor_Allele_Frequency'].str.split(':',expand=True)
dff1[['INDEL5_Allele', 'INDEL5_Value']] = dff1['Tumor_Allele_Frequency'].str.split(':',expand=True)
dff2[['INDEL7_Allele', 'INDEL7_Value']] = dff2['Tumor_Allele_Frequency'].str.split(':',expand=True)
dfff[['SNV3_Allele', 'SNV3_Value']] = dfff['Tumor'].str.split(':',expand=True)
dfff1[['SNV5_Allele', 'SNV5_Value']] = dfff1['Tumor'].str.split(':',expand=True)
dfff2[['SNV7_Allele', 'SNV7_Value']] = dfff2['Tumor'].str.split(':',expand=True)
print(dff)


# Renaming Columns
# dff.columns = ['CHROM_POS', 'Strelka_Normal_0.3', 'Strelka_Tumor_0.3', 'Strelka_0.5_Normal', 'Strelka_0.5_Tumor', 'Strelka_0.7_Normal', 'Strelka_0.7_Tumor']

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
dff = dff.drop(['Tumor_Allele_Frequency', 'INDEL3_Allele'], axis=1)
dff1 = dff1.drop(['Tumor_Allele_Frequency', 'INDEL5_Allele'], axis=1)
dff2 = dff2.drop(['Tumor_Allele_Frequency', 'INDEL7_Allele'], axis=1)
dfff = dfff.drop(['Tumor', 'SNV3_Allele'], axis=1)
dfff1 = dfff1.drop(['Tumor', 'SNV5_Allele'], axis=1)
dfff2 = dfff2.drop(['Tumor', 'SNV7_Allele'], axis=1)

# Renaming the columns.
# dff.columns = ['Normal_0.3', 'Tumor_0.3', 'Normal_0.5', 'Tumor_0.5', 'Normal_0.7', 'Tumor_0.7']
# print(dff)

# Removing the columns.
dff = dff.drop(['CHROM_POS'], axis=1)
dff1 = dff1.drop(['CHROM_POS'], axis=1)
dff2 = dff2.drop(['CHROM_POS'], axis=1)
dfff = dfff.drop(['CHROM_POS'], axis=1)
dfff1 = dfff1.drop(['CHROM_POS'], axis=1)
dfff2 = dfff2.drop(['CHROM_POS'], axis=1)

# Converting string values columns to float.
dff['INDEL3_Value'] = dff['INDEL3_Value'].astype(float)
dff1['INDEL5_Value'] = dff1['INDEL5_Value'].astype(float)
dff2['INDEL7_Value'] = dff2['INDEL7_Value'].astype(float)
dfff['SNV3_Value'] = dfff['SNV3_Value'].astype(float)
dfff1['SNV5_Value'] = dfff1['SNV5_Value'].astype(float)
dfff2['SNV7_Value'] = dfff2['SNV7_Value'].astype(float)
print(dff)

# Getting a count based on allele frequency values.
IN1 = dff[dff < 0.26].count()
IN2 = dff[dff < 0.51].count()
IN3 = dff[dff < 0.76].count()
IN4 = dff[dff < 1.01].count()
print('Indel count')
print(IN1)

IN5 = dff1[dff1 < 0.26].count()
IN6 = dff1[dff1 < 0.51].count()
IN7 = dff1[dff1 < 0.76].count()
IN8 = dff1[dff1 < 1.01].count()

IN9 = dff2[dff2 < 0.26].count()
IN10 = dff2[dff2 < 0.51].count()
IN11 = dff2[dff2 < 0.76].count()
IN12 = dff2[dff2 < 1.01].count()

SN1 = dfff[dfff < 0.26].count()
SN2 = dfff[dfff < 0.51].count()
SN3 = dfff[dfff < 0.76].count()
SN4 = dfff[dfff < 1.01].count()

SN5 = dfff1[dfff1 < 0.26].count()
SN6 = dfff1[dfff1 < 0.51].count()
SN7 = dfff1[dfff1 < 0.76].count()
SN8 = dfff1[dfff1 < 1.01].count()

SN9 = dfff2[dfff2 < 0.26].count()
SN10 = dfff2[dfff2 < 0.51].count()
SN11 = dfff2[dfff2 < 0.76].count()
SN12 = dfff2[dfff2 < 1.01].count()
print('SNV count')
print(SN1)

# Getting the final values
IN13 = (IN1 - IN2).abs()
IN14 = (IN2 - IN3).abs()
IN15 = (IN3 - IN4).abs()
print(IN13)

IN16 = (IN5 - IN6).abs()
IN17 = (IN6 - IN7).abs()
IN18 = (IN7 - IN8).abs()

IN19 = (IN9 - IN10).abs()
IN20 = (IN10 - IN11).abs()
IN21 = (IN11 - IN12).abs()

SN13 = (SN1 - SN2).abs()
SN14 = (SN2 - SN3).abs()
SN15 = (SN3 - SN4).abs()

SN16 = (SN5 - SN6).abs()
SN17 = (SN6 - SN7).abs()
SN18 = (SN7 - SN8).abs()

SN19 = (SN9 - SN10).abs()
SN20 = (SN10 - SN11).abs()
SN21 = (SN11 - SN12).abs()

# Counting the numbers
df_Count = IN1 + SN1
print('Getting the count')
print(df_Count)

print(dff1)
print(dff5)
print(dff6)
print(dff7)

# Converting into list.
First_Column = dff1.tolist()
Second_Column = dff5.tolist()
Third_Column = dff6.tolist()
Fourth_Column = dff7.tolist()
Fifth_Column =['Normal_0.3', 'Tumor_0.3', 'Normal_0.5', 'Tumor_0.5', 'Normal_0.7', 'Tumor_0.7']
print(First_Column)
print(Second_Column)
print(Third_Column)
print(Fourth_Column)

# Declaring new columns.
dff8 = pd.DataFrame(Fifth_Column, columns = ['Type'])
dff8['Less than 0.25'] = First_Column
dff8['Between 0.25 & 0.50'] = Second_Column
dff8['Between 0.50 & 0.75'] = Third_Column
dff8['Between 0.75 & 1.00'] = Fourth_Column
print(dff8)

# Saving the results in csv.
dff8.to_csv('Strelka_Allele_Frequency_Counts.csv', sep=',', index = None)

dff9 = dff8.drop(['Type'], axis=1)
print(dff9)

# Converting the values to a list
List = dff9.values.tolist()
a1, a2, a3, a4, a5, a6 = List
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

# set width of bar
width = 0.10

# Columns from the file
# a1 = First_Column
# a2 = Second_Column
# a3 = Third_Column
# a4 = Fourth_Column

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['<= 0.25', '0.26 to 0.50', '0.51 to 0.75', '> 0.75']
explode = (0.1, 0, 0, 0)
colors = ['#FFD700','#FFAA1C','#FF8C01','#FF0000']
ax.pie(a1, explode=explode, labels = langs, colors=colors, autopct='%1.2f%%')
ax.set_title('Normal Allele Frequency Counts Percentage')
plt.savefig('Strelka_Normal_Allele_Frequency.png', dpi = 300)

fig1 = plt.figure()
ax1 = fig1.add_axes([0,0,1,1])
ax1.axis('equal')
langs = ['<= 0.25', '0.26 to 0.50', '0.51 to 0.75', '> 0.75']
explode = (0.1, 0, 0, 0)
colors = ['#FFD700','#FFAA1C','#FF8C01','#FF0000']
ax1.pie(a2, explode=explode, labels = langs, colors=colors, autopct='%1.2f%%')
ax1.set_title('Normal Allele Frequency Counts Percentage')
plt.savefig('Strelka_Tumor_Allele_Frequency.png', dpi = 300)

# Set position of bar on X axis
r1 = np.arange(len(a1))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]
r4 = [x + width for x in r3]
r5 = [x + width for x in r4]
r6 = [x + width for x in r5]

# Make the plot
plt.bar(r1, a1, color='#ff0000', width=width, edgecolor='white', label='Normal_0.3')
plt.bar(r2, a2, color='#ffa07a', width=width, edgecolor='white', label='Tumor_0.3')
plt.bar(r3, a3, color='#f08080', width=width, edgecolor='white', label='Normal_0.5')
plt.bar(r4, a4, color='#fa8072', width=width, edgecolor='white', label='Tumor_0.5')
plt.bar(r5, a5, color='#b22222', width=width, edgecolor='white', label='Normal_0.7')
plt.bar(r6, a6, color='#800000', width=width, edgecolor='white', label='Tumor_0.7')

csfont = {'fontname':'Comic Sans MS'}
hfont = {'fontname':'Helvetica'}

# Add xticks on the middle of the group bars
plt.xlabel('Strelka_Allele_Frequencies')
plt.xticks([r + width for r in range(len(a1))], ['<= 0.25', '<= 0.50', '<= 0.75', '<= 1.00'])

# Create legend & Show graphic
plt.legend()
plt.show()
plt.savefig('Strelka_Allele_Frequency_Plot.pdf')
plt.savefig('Strelka_Allele_Frequency_Plot.png', dpi = 300)
