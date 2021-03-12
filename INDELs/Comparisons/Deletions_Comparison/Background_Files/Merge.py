# Importing packages.
import numpy as np
import pandas as pd

# Adding somatic truth value.

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_Deletions_Counts.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_Deletions_Counts.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['Type'])

# Declare a list that is to be converted into a column
deletions = ['53883', '53883', '53883']

# Using 'Address' as the column name
# and equating it to the list
First['Truth_Data_Deletions'] = deletions
print(First)
  
# Saving the results in csv.
First.to_csv('Deletions_Comparision.csv', index=False, encoding='utf-8')
