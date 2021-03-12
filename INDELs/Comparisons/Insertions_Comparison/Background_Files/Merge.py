# Importing packages.
import numpy as np
import pandas as pd

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_Insertions_Counts.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_Insertions_Counts.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['Type'])

# Declare a list that is to be converted into a column
insertions = ['44592', '44592', '44592']

# Using 'Address' as the column name
# and equating it to the list
First['Truth_Data_Deletions'] = insertions
print(First)

# Saving the results in csv.
First.to_csv('Insertions_Comparision.csv', index=False, encoding='utf-8')
