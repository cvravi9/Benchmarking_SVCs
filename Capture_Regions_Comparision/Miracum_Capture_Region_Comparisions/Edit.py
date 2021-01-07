import pandas as pd

First_Input = pd.read_csv("Miracum_0.4_Allele_Frequency.frq")
First_Input.to_csv('First_Input.csv', index = None)

df = pd.read_csv('First_Input.csv', sep='\t')
First_Input_Edit = pd.concat(df, keys=["CHROM", "POS"])
df1 = df['CHROM'].map(str) + '-' + df['POS'].map(str)
print(df1)

# dff = df.drop(['N_ALLELES', 'N_CHR', 'N_ALLELES.1', 'N_CHR.1', 'CHROM.1', 'POS.1', 'Unnamed: 5'], axis=1)
# print(dff)
