# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Strelka_Miracum_0.4.frq", sep = '\t', index_col= False, error_bad_lines=False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff["CHROM-POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)

# Reorganising columns.
dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

# Reading csv files and concatinating "CHROM" and "POS"
dff1 = pd.read_csv("Strelka_Miracum_0.7.frq", sep = '\t', index_col= False, error_bad_lines=False)
dff1.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff1["CHROM-POS"] = dff1['CHROM'].astype(str) + '-' + dff1['POS'].astype(str)

# Reorganising columns.
dff1 = dff1.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff1.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff1 = dff1[cols]
print(dff1)

# Reading csv files and concatinating "CHROM" and "POS"
dff2 = pd.read_csv("Strelka_Somatic_0.4.frq", sep = '\t', index_col= False, error_bad_lines=False)
dff2.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff2["CHROM-POS"] = dff2['CHROM'].astype(str) + '-' + dff2['POS'].astype(str)

# Reorganising columns.
dff2 = dff2.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff2.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff2 = dff2[cols]
print(dff2)

# Reading csv files and concatinating "CHROM" and "POS"
dff3 = pd.read_csv("Strelka_Somatic_0.7.frq", sep = '\t', index_col= False, error_bad_lines=False)
dff3.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff3["CHROM-POS"] = dff3['CHROM'].astype(str) + '-' + dff3['POS'].astype(str)

# Reorganising columns.
dff3 = dff3.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff3.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff3 = dff3[cols]
print(dff3)

# Merging columns based on "CHROM-POS"
Result = pd.merge(dff, dff1, on="CHROM-POS")
First_Result = pd.merge(Result, dff2, on="CHROM-POS")
Second_Result = pd.merge(First_Result, dff3, on="CHROM-POS")
Second_Result.columns = ['CHROM_POS', 'Miracum_0.4_AF', 'Miracum_0.7_AF', 'Somatic_0.4_AF', 'Somatic_0.7_AF']
print(Second_Result)

# Saving the results in csv.
Second_Result.to_csv('Strelka_Germline_AF_Values.csv', sep='\t', index=False, encoding='utf-8')
Second_Result.to_csv('Strelka_Germline_AF_Plot_Values.csv', sep='\t', index =False)
