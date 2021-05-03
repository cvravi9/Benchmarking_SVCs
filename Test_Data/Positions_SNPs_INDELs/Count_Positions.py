# Importing packages.
import numpy as np
import pandas as pd
import matplotlib
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
from matplotlib import rc
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'serif'

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Updated_Test.vcf", sep = '\t', index_col= False)
df1 = pd.read_csv("Updated_Test.annot.vcf", sep = '\t', index_col= False)

# Renaming the columns.
df.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
df1.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']

# Merging columns based on "POS"
First = pd.merge(df, df1, on=['POS'])

# Position outcomes.
print("Number of Test Positions:")
Strelka_Positions = len(df)
print(Strelka_Positions)

print("Number of Test.annot Positions:")
VarScan_Positions = len(df1)
print(VarScan_Positions)

print("Number of Positions in Test and Test.annot:")
Strelka_VarScan_Positions = len(First)
print(Strelka_VarScan_Positions)

# Delcaring a new dataframe.
df3 = []

# Taking all combinations as a list.
data = {'Type': ['Test', 'Test.annot', 'Common_Positions'], 'Positions': [Strelka_Positions, VarScan_Positions, Strelka_VarScan_Positions]}

# Collecting it into a dataframe.
df3 = pd.DataFrame(data)
print(df3)

# Saving the results in csv.
df3.to_csv('Positions_Count.csv', sep=',', index = None)

# Formulas
Test_Exclude = Strelka_Positions - Strelka_VarScan_Positions
Testannot_Exclude = VarScan_Positions - Strelka_VarScan_Positions

# Set of values.
subsets = (Test_Exclude, Testannot_Exclude, Strelka_VarScan_Positions)

# Adding venn diagram.
v = venn2(subsets, set_labels = ('Test', 'Test.annot'), set_colors=('red', 'orange', 'skyblue'))

# Saving the values.
plt.title("Positions [SNPs + Indels]")
plt.show()
plt.savefig('Positions_Plot.pdf')
