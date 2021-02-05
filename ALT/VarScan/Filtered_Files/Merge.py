# Importing the needed packages.
import numpy as np
import pandas as pd

# Reading the csv input file that is obtained after performing the following operations on the vcf file.
dff = pd.read_csv("Selected_Miracum_0.4.csv", sep = '\t', index_col= False)
dff1 = pd.read_csv("Selected_Miracum_0.7.csv", sep = '\t', index_col= False)
dff2 = pd.read_csv("Selected_Somatic_0.4.csv", sep = '\t', index_col= False)
dff3 = pd.read_csv("Selected_Somatic_0.7.csv", sep = '\t', index_col= False)

# Merging the files based on CHROM-POS
Result = pd.merge(dff, dff1, on="CHROM_POS")
First_Result = pd.merge(Result, dff2, on="CHROM_POS")
Second_Result = pd.merge(First_Result, dff3, on="CHROM_POS")
print(Second_Result)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM_POS', 'REF', 'ALT']

# Saving the result into a csv file for plotting.
dff.to_csv('Comparisions_ALT.csv', sep='\t', index = None)
