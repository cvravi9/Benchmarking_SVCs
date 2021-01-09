import numpy as np
import pandas as pd

dff = pd.read_csv("Miracum_AF_0.4.frq", sep = '\t', index_col= False)
dff.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff["CHROM-POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)


dff = dff.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

dff1 = pd.read_csv("Somatic_AF_0.7.frq", sep = '\t', index_col= False)
dff1.columns = ['CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ']
dff1["CHROM-POS"] = dff1['CHROM'].astype(str) + '-' + dff1['POS'].astype(str)


dff1 = dff1.drop(['N_ALLELES', 'N_CHR', 'CHROM', 'POS'], axis=1)
cols = dff1.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff1 = dff1[cols]
print(dff1)

result = pd.merge(dff, dff1, on="CHROM-POS")
result.columns = ['CHROM-POS', 'Miracum_AF_0.4_REF', 'Somatic_AF_0.7_REF']
print(result)

result["REF_Comparision"] = result["Miracum_AF_0.4_REF"].equals(result["Somatic_AF_0.7_REF"])
print(result)

result.to_csv('0.4_vs_0.7_AF_Comparision.csv', sep='\t', index = None)