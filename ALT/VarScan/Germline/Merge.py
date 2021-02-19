# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Miracum_0.4_Count.csv", sep = '\t', index_col= False)
df.columns = ['REF', 'ALT', 'Miracum_0.4']

df1 = pd.read_csv("Miracum_0.7_Count.csv", sep = '\t', index_col= False)
df1.columns = ['REF', 'ALT', 'Miracum_0.7']

df2 = pd.read_csv("Somatic_0.4_Count.csv", sep = '\t', index_col= False)
df2.columns = ['REF', 'ALT', 'Somatic_0.4']

df3 = pd.read_csv("Somatic_0.7_Count.csv", sep = '\t', index_col= False)
df3.columns = ['REF', 'ALT', 'Somatic_0.7']

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on="ALT")
Second = pd.merge(First, df2, on="ALT")
Third = pd.merge(Second, df3, on="ALT")
Third.columns = ['REF', 'ALT', 'Miracum_0.4', 'Miracum_0.7', 'Somatic_0.4', 'Somatic_0.7']
print(Third)

# Saving the results in csv.
# Third.to_csv('Combinations_Count_Values.csv', sep='\t', index = None)
