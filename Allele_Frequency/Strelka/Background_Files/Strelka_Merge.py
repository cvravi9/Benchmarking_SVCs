import pandas as pd

# Reading two csv files
data1 = pd.read_csv('Strelka_Indels.csv')
data2 = pd.read_csv('Strelka_SNPs.csv')

# Assigning column names.
data1.columns = ['CHROM_POS', 'Indel_Normal_0.3', 'Indel_Tumor_0.3', 'Indel_Normal_0.5', 'Indel_Tumor_0.5', 'Indel_Normal_0.7', 'Indel_Tumor_0.7']
data2.columns = ['CHROM_POS', 'SNP_Normal_0.3', 'SNP_Tumor_0.3', 'SNP_Normal_0.5', 'SNP_Tumor_0.5', 'SNP_Normal_0.7', 'SNP_Tumor_0.7']
print(data1)
print(data2)

# Using merge function by setting how='inner'
df = pd.merge(data1, data2, on='CHROM_POS', how='outer')
df['Normal_0.3_AF'] = df['Indel_Normal_0.3'].combine_first(df['SNP_Normal_0.3'])
df['Tumor_0.3_AF'] = df['Indel_Tumor_0.3'].combine_first(df['SNP_Tumor_0.3'])
df['Normal_0.5_AF'] = df['Indel_Normal_0.5'].combine_first(df['SNP_Normal_0.5'])
df['Tumor_0.5_AF'] = df['Indel_Tumor_0.5'].combine_first(df['SNP_Tumor_0.5'])
df['Normal_0.7_AF'] = df['Indel_Normal_0.7'].combine_first(df['SNP_Normal_0.7'])
df['Tumor_0.7_AF'] = df['Indel_Tumor_0.7'].combine_first(df['SNP_Tumor_0.7'])
print(df)

# Dropping unneeded columns.
df = df.drop(['Indel_Normal_0.3', 'Indel_Tumor_0.3', 'Indel_Normal_0.5', 'Indel_Tumor_0.5', 'Indel_Normal_0.7', 'Indel_Tumor_0.7', 'SNP_Normal_0.3', 'SNP_Tumor_0.3', 'SNP_Normal_0.5', 'SNP_Tumor_0.5', 'SNP_Normal_0.7', 'SNP_Tumor_0.7'], axis=1)
print(df) 

# Saving the result into a csv file for plotting.
df.to_csv('Strelka_Allele_Frequency.csv', sep=',', index = False)
