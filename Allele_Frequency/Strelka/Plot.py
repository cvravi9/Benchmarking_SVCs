# Importing the needed packages.
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import rc
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'serif'
import matplotlib.pyplot as plt
import csv
matplotlib.rcParams['font.sans-serif'] = ['Computer Modern Roman', 'sans-serif']

# Consider the Updated_Output.vcf as input.
df1 = pd.read_csv("Strelka7_INDEL_AF.csv", sep = ',', index_col= False)
df2 = pd.read_csv("Strelka7_SNV_AF.csv", sep = ',', index_col= False)

# Renaming the columns.
df1.columns = ['CHROM_POS', 'Tumor']
df2.columns = ['CHROM_POS', 'Tumor']

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "GT:GQ:DP:AD:ADF:ADR".
df1[['INDEL_Allele', 'INDEL_Value']] = df1['Tumor'].str.split(':',expand=True)
df2[['SNV_Allele', 'SNV_Value']] = df2['Tumor'].str.split(':',expand=True)
print(df1)
print(df2)

# Renaming Columns
# dff.columns = ['CHROM_POS', 'Strelka_Normal_0.3', 'Strelka_Tumor_0.3', 'Strelka_0.5_Normal', 'Strelka_0.5_Tumor', 'Strelka_0.7_Normal', 'Strelka_0.7_Tumor']

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
df1 = df1.drop(['CHROM_POS', 'Tumor', 'INDEL_Allele'], axis=1)
df2 = df2.drop(['CHROM_POS', 'Tumor', 'SNV_Allele'], axis=1)
print(df1)
print(df2)

# Converting string values columns to float.
df1['INDEL_Value'] = df1['INDEL_Value'].astype(float)
df2['SNV_Value'] = df2['SNV_Value'].astype(float)
print(df1)
print(df2)

# Getting a count based on allele frequency values.
IN1 = df1[df1 < 0.26].count()
IN2 = df1[df1 < 0.51].count()
IN3 = df1[df1 < 0.76].count()
IN4 = df1[df1 < 1.01].count()
print('Indel count')
print(IN1)

SN1 = df2[df2 < 0.26].count()
SN2 = df2[df2 < 0.51].count()
SN3 = df2[df2 < 0.76].count()
SN4 = df2[df2 < 1.01].count()

# Getting the final values
IN5 = (IN1 - IN2).abs()
IN6 = (IN2 - IN3).abs()
IN7 = (IN3 - IN4).abs()
print('Second round Indels')
print(IN5)

SN5 = (SN1 - SN2).abs()
SN6 = (SN2 - SN3).abs()
SN7 = (SN3 - SN4).abs()
print('Second round')
print(SN5)

# Converting into list.
First_Indels = IN1.tolist()
Second_Indels = IN5.tolist()
Third_Indels = IN6.tolist()
Fourth_Indels = IN7.tolist()
First_SNV = SN1.tolist()
Second_SNV = SN5.tolist()
Third_SNV = SN6.tolist()
Fourth_SNV = SN7.tolist()

# Final count.
First = np.add(First_Indels, First_SNV)
Second = np.add(Second_Indels, Second_SNV)
Third = np.add(Third_Indels, Third_SNV)
Fourth = np.add(Fourth_Indels, Fourth_SNV)
print('Testing the count')
print(First)

# Declaring new columns.
a1 = np.append(First, Second)
a1 = np.append(a1, Third)
a1 = np.append(a1, Fourth)
print(a1)

# set width of bar
width = 0.10

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['<= 0.25', '0.26 to 0.50', '0.51 to 0.75', '> 0.75']
explode = (0.1, 0, 0, 0)
colors = ['#FFD700','#FFAA1C','#FF8C01','#FF0000']
ax.pie(a1, explode=explode, labels = langs, colors=colors, autopct='%1.2f%%')
ax.set_title('Allele Frequency Counts Percentage')
plt.savefig('Strelka7_Allele_Frequency.png', dpi = 300)
