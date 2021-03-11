import pandas as pd

# Reading two csv files
data1 = pd.read_csv('Strelka_0.7_SNV.csv')
data2 = pd.read_csv('Strelka_0.7_Indels.csv')

# Using merge function by setting how='inner'
df = pd.merge(data1, data2, on='CHROM_POS', how='outer')
df['Normal_AF'] = df['Normal'].combine_first(df['Normal_Allele_Frequency'])
df['Tumor_AF'] = df['Tumor'].combine_first(df['Tumor_Allele_Frequency'])

# Dropping unneeded columns.
df = df.drop(['Normal', 'Tumor', 'Normal_Allele_Frequency', 'Tumor_Allele_Frequency'], axis=1)
print(df) 

# Saving the result into a csv file for plotting.
df.to_csv('Strelka_0.7.csv', sep=',', index=False, encoding='utf-8')
df.to_csv('Strelka_0.7_Plot.csv', sep='\t', index = None)
