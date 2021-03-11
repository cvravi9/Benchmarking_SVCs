import pandas as pd

# Reading the three vcf files with their allele frequencies.
data1 = pd.read_csv('Strelka_0.3.csv')
data2 = pd.read_csv('Strelka_0.5.csv')
data3 = pd.read_csv('Strelka_0.7.csv')

# Merging the csv files for comparison.
df = pd.merge(data1, data2, on='CHROM_POS')
dff = pd.merge(df, data3, on='CHROM_POS')

# Renaming the columns in the csv file.
dff.columns = ['CHROM_POS', 'NORMAL_0.3', 'TUMOR_0.3', 'NORMAL_0.5', 'TUMOR_0.5', 'NORMAL_0.7', 'TUMOR_0.7']
print(dff) 

# Saving the result into a csv file.
dff.to_csv('Strelka_Allele_Frequency.csv', sep=',', index=False, encoding='utf-8')
dff.to_csv('Strelka_Allele_Frequency_Plot.csv', sep='\t', index = None)
