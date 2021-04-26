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
df = pd.read_csv("VarScan7_AF.csv", sep = ',', index_col= False)

# Creating new columns by splitting the "Allele" and "Value" by ':'.
df[['VarScan_Allele', 'VarScan_Value']] = df['ALLELE:FREQ'].str.split(':',expand=True)

# Dropping of the unnecessary columns and only choosing the "NORMAL Depth" i.e. "NORMAL-DP" and "TUMOR Depth" i.e. "TUMOR-DP"
df = df.drop(['CHROM_POS', 'ALLELE:FREQ', 'VarScan_Allele'], axis=1)

# Renaming the columns.
df.columns = ['AF']
print(df)

# Converting string values columns to float.
df['AF'] = df['AF'].astype(float)

# Getting a count based on allele frequency values.
df1 = df[df < 0.26].count()
df2 = df[df < 0.51].count()
df3 = df[df < 0.76].count()
df4 = df[df < 1.01].count()
print('First quater')
print(df1)

# Getting the final values
df5 = (df1 - df2).abs()
df6 = (df2 - df3).abs()
df7 = (df3 - df4).abs()
print('Second quater')
print(df5)
print(df6)
print(df7)

# Converting into list.
First = df1.tolist()
Second = df5.tolist()
Third = df6.tolist()
Fourth = df7.tolist()

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
plt.savefig('VarScan7_Allele_Frequency.png', dpi = 300)
