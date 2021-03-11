import pandas as pd

# Reading two csv files
data1 = pd.read_csv('Strelka_0.3.csv')
data2 = pd.read_csv('Strelka_0.5.csv')
data3 = pd.read_csv('Strelka_0.7.csv')

# Using merge function by setting how='inner'
df = pd.merge(data1, data2, on='CHROM_POS')
dff = pd.merge(df, data3, on='CHROM_POS')

# Naming the columns after importing the csv file.
dff.columns = ['CHROM_POS', 'NORMAL_0.3', 'TUMOR_0.3', 'NORMAL_0.5', 'TUMOR_0.5', 'NORMAL_0.7', 'TUMOR_0.7']
print(dff) 

# Saving the result into a csv file for plotting.
dff.to_csv('Strelka_Allele_Frequency.csv', sep=',', index=False, encoding='utf-8')
dff.to_csv('Strelka_Allele_Frequency_Plot.csv', sep='\t', index = None)
