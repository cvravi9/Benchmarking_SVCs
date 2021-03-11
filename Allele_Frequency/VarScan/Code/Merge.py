# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("VarScan_0.3.frq", sep = '\t', index_col= False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)

# Reorganising columns.
dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

# Reading csv files and concatinating "CHROM" and "POS"
dff1 = pd.read_csv("VarScan_0.5.frq", sep = '\t', index_col= False)
dff1.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff1["CHROM_POS"] = dff1['CHROM'].astype(str) + '-' + dff1['POS'].astype(str)

# Reorganising columns.
dff1 = dff1.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff1.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff1 = dff1[cols]
print(dff1)

# Reading csv files and concatinating "CHROM" and "POS"
dff2 = pd.read_csv("VarScan_0.7.frq", sep = '\t', index_col= False)
dff2.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff2["CHROM_POS"] = dff2['CHROM'].astype(str) + '-' + dff2['POS'].astype(str)

# Reorganising columns.
dff2 = dff2.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff2.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff2 = dff2[cols]
print(dff2)

# Merging columns based on "CHROM-POS"
Result = pd.merge(dff, dff1, on="CHROM_POS")
First_Result = pd.merge(Result, dff2, on="CHROM_POS")
First_Result.columns = ['CHROM_POS', 'VarScan_0.3_AF', 'VarScan_0.5_AF', 'VarScan_0.7_AF']

# Saving the results in csv.
First_Result.to_csv('VarScan_AF_Values.csv', sep='\t', index=False, encoding='utf-8')
First_Result.to_csv('VarScan_AF_Plot_Values.csv', sep='\t', index = None)
