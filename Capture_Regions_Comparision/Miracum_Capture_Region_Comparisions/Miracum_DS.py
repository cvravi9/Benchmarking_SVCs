import numpy as np
import pandas as pd

dff = pd.read_csv("Miracum_DS_0.4.ldepth", sep = '\t', index_col= False)
dff.columns = ['CHROM', 'POS', 'SUM_DEPTH', 'SUMSQ_DEPTH']
dff["CHROM-POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)

dff = dff.drop(['CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

dff1 = pd.read_csv("Miracum_DS_0.7.ldepth", sep = '\t', index_col= False)
dff1.columns = ['CHROM', 'POS', 'SUM_DEPTH', 'SUMSQ_DEPTH']
dff1["CHROM-POS"] = dff1['CHROM'].astype(str) + '-' + dff1['POS'].astype(str)

dff1 = dff1.drop(['CHROM', 'POS'], axis=1)
cols = dff1.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff1 = dff1[cols]
print(dff1)

result = pd.merge(dff, dff1, on="CHROM-POS")
result.columns = ['CHROM-POS', 'SUM_DEPTH_DS_0.4_REF', 'SUMSQ_DEPTH_DS_0.4_REF', 'SUM_DEPTH_DS_0.7_REF', 'SUMSQ_DEPTH_DS_0.7_REF']
print(result)

result["SUM_DEPTH_REF_Comparision"] = result["SUM_DEPTH_DS_0.4_REF"].equals(result["SUM_DEPTH_DS_0.7_REF"])
print(result)

result["SUMSQ_DEPTH_REF_Comparision"] = result["SUMSQ_DEPTH_DS_0.4_REF"].equals(result["SUMSQ_DEPTH_DS_0.7_REF"])
print(result)

result.to_csv('Miracum_DS_Comparision.csv', sep='\t', index = None)
