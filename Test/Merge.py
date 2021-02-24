# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Allele_Frequency_Values.csv", sep = '\t', index_col= False)
dff = pd.read_csv("Miracum_AF_Values.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
Result = pd.merge(df, dff, on="CHROM-POS")
Result.columns = ['CHROM-POS', 'Miracum_0.4_AF_VarScan', 'Miracum_0.7_AF_VarScan', 'Somatic_0.4_AF_VarScan', 'Somatic_0.7_AF_VarScan', 'Miracum_0.4_AF_Strelka', 'Miracum_0.7_AF_Strelka', 'Somatic_0.4_AF_Strelka', 'Somatic_0.7_AF_Strelka']
print(Result)

# Saving the results in csv.
Result.to_csv('All_AF_Values.csv', sep='\t', index = None)
