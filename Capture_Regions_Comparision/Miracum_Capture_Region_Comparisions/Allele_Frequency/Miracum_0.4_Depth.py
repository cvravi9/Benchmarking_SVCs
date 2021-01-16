import numpy as np
import pandas as pd

dff = pd.read_csv("Updated_Test_Output.csv", sep = '\t', index_col= False)
dff.columns = ['CHROM', 'POS', 'FORMAT', 'NORMAL', 'TUMOR']
dff["CHROM-POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)


dff = dff.drop(['CHROM', 'POS', 'FORMAT'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]
print(dff)

dff[['NORMAL-GT','NORMAL-GQ','NORMAL-DP', 'NORMAL-AD','NORMAL-ADF', 'NORMAL-ADR']] = dff['NORMAL'].str.split(':',expand=True)
dff[['TUMOR-GT','TUMOR-GQ','TUMOR-DP', 'TUMOR-AD','TUMOR-ADF', 'TUMOR-ADR']] = dff['TUMOR'].str.split(':',expand=True)

dff = dff.drop(['NORMAL', 'TUMOR', 'NORMAL-GT', 'NORMAL-GQ', 'NORMAL-AD', 'NORMAL-ADF', 'NORMAL-ADR', 'TUMOR-GT', 'TUMOR-GQ', 'TUMOR-AD', 'TUMOR-ADF', 'TUMOR-ADR'], axis=1)
print(dff)

# result.to_csv('Miracum_AF_Comparision.csv', sep='\t', index = None)
