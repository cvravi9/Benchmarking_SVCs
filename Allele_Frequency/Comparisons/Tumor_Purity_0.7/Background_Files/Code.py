# Importing packages.
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt 
import csv

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Strelka_0.7.csv", sep = '\t', index_col= False)
df1 = pd.read_csv("VarScan_0.7.csv", sep = '\t', index_col= False)
df2 = pd.read_csv("Somatic_Truth.csv", sep = '\t', index_col= False)

# Merging columns based on "CHROM-POS"
First = pd.merge(df, df1, on=['CHROM_POS'])
Second = pd.merge(First, df2, on=['CHROM_POS'])

# Renaming Columns
Second.columns = ['CHROM_POS', 'Strelka_Normal', 'Strelka_Tumor', 'VarScan', 'Truth_Data']
print(Second)

# Saving the results in csv.
Second.to_csv('Tumor_Purity_0.7.csv', sep=',', index = None)

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "GT:GQ:DP:AD:ADF:ADR".
Second[['Strelka_Normal_Allele', 'Strelka_Normal_Value']] = Second['Strelka_Normal'].str.split(':',expand=True)
Second[['Strelka_Tumor_Allele', 'Strelka_Tumor_Value']] = Second['Strelka_Tumor'].str.split(':',expand=True)
Second[['VarScan_Normal_Allele', 'VarScan_Normal_Value']] = Second['VarScan'].str.split(':',expand=True)
Second[['Truth_Data_Allele', 'Truth_Data_Value']] = Second['Truth_Data'].str.split(':',expand=True)
print(Second)

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
dff = Second.drop(['CHROM_POS', 'Strelka_Normal', 'Strelka_Tumor', 'VarScan', 'Truth_Data', 'Strelka_Normal_Allele', 'Strelka_Tumor_Allele', 'VarScan_Normal_Allele', 'Truth_Data_Allele'], axis=1)
print(dff)

# Renaming the columns.
dff.columns = ['Strelka_Normal', 'Strelka_Tumor', 'VarScan', 'Truth_Data']
print(dff)

# Converting string values columns to float.
dff['Strelka_Normal'] = dff['Strelka_Normal'].astype(float)
dff['Strelka_Tumor'] = dff['Strelka_Tumor'].astype(float)
dff['VarScan'] = dff['VarScan'].astype(float)
dff['Truth_Data'] = dff['Truth_Data'].astype(float)
print(dff)

# Getting a count based on allele frequency values.
dff1 = dff[dff < 0.26].count()
dff2 = dff[dff < 0.51].count()
dff3 = dff[dff < 0.76].count()
dff4 = dff[dff < 1.01].count()

# Getting the final values
dff5 = (dff1 - dff2).abs()
dff6 = (dff2 - dff3).abs()
dff7 = (dff3 - dff4).abs()
print(dff1)
print(dff5)
print(dff6)
print(dff7)

# Converting into list.
First_Column = dff1.tolist()
Second_Column = dff5.tolist()
Third_Column = dff6.tolist()
Fourth_Column = dff7.tolist()
Fifth_Column =['Strelka_Normal', 'Strelka_Tumor', 'VarScan', 'Truth_Data']
print(First_Column)
print(Second_Column)
print(Third_Column)
print(Fourth_Column)

# Declaring new columns.
dff8 = pd.DataFrame(Fifth_Column, columns = ['Type'])
dff8['Less than 0.25'] = First_Column
dff8['Between 0.25 & 0.50'] = Second_Column
dff8['Between 0.50 & 0.75'] = Third_Column
dff8['Between 0.75 & 1.00'] = Fourth_Column
print(dff8)

# Saving the results in csv.
dff8.to_csv('Tumor_Purity_0.7_AF_Counts.csv', sep=',', index = None)

# set width of bar
width = 0.25

# Columns from the file
a1 = First_Column
a2 = Second_Column
a3 = Third_Column
a4 = Fourth_Column

# Set position of bar on X axis
r1 = np.arange(len(a1))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]
r4 = [x + width for x in r3]

# Make the plot
plt.bar(r1, a1, color='#FFD700', width=width, edgecolor='white', label='Strelka_Normal')
plt.bar(r2, a2, color='#FFAA1C', width=width, edgecolor='white', label='Strelka_Tumor')
plt.bar(r3, a3, color='#FF8C01', width=width, edgecolor='white', label='VarScan')
plt.bar(r4, a4, color='#FF0000', width=width, edgecolor='white', label='Truth_Data')

# Add xticks on the middle of the group bars
plt.xlabel('Tumor_0.7_Allele_Frequencies')
plt.xticks([r + width for r in range(len(a1))], ['<= 0.25', '<= 0.50', '<= 0.75', '<= 1.00'])

# Create legend & Show graphic
plt.legend()
plt.show()
plt.savefig('Tumor_Purity_0.7_AF_Plot.pdf')
