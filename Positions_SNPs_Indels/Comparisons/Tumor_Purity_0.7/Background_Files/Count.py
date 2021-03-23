# Importing packages.
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import rc
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'serif'
from matplotlib import pyplot as plt
from matplotlib_venn import venn3_circles, venn3_unweighted
from matplotlib_venn import _common, _venn3
from matplotlib.patches import Circle

# Reading csv files and concatinating "CHROM" and "POS"
df = pd.read_csv("Updated_Strelka_0.7.vcf", sep = '\t', index_col= False)
df1 = pd.read_csv("Updated_VarScan_0.7.vcf", sep = '\t', index_col= False)
df2 = pd.read_csv("Updated_Somatic_Truth.vcf", sep = '\t', index_col= False)

# Merging columns based on "POS"
First = pd.merge(df, df1, on=['POS'])
Second = pd.merge(df1, df2, on=['POS'])
Third = pd.merge(df, df2, on=['POS'])
Fourth = pd.merge(First, df2, on=['POS'])

# Position outcomes.
print("Number of positions in Strelka:")
Strelka_Positions = len(df)
print(Strelka_Positions)

print("Number of positions in VarScan:")
VarScan_Positions = len(df1)
print(VarScan_Positions)

print("Number of positions in Truth Data:")
Truth_Positions = len(df2)
print(Truth_Positions)

print("Number of positions in Strelka and VarScan:")
Strelka_VarScan_Positions = len(First)
print(Strelka_VarScan_Positions)

print("Number of positions in VarScan and Truth Data:")
VarScan_Truth_Positions = len(Second)
print(VarScan_Truth_Positions)

print("Number of positions in Truth Data and Strelka:")
Strelka_Truth_Positions = len(Third)
print(Strelka_Truth_Positions)

print("Number of positions in Strelka, VarScan & Truth Data:")
Strelka_VarScan_Truth_Positions = len(Fourth)
print(Strelka_VarScan_Truth_Positions)

# Delcaring a new dataframe.
df3 = []

# Taking all combinations as a list.
data = {'Type': ['Strelka', 'VarScan', 'Truth_Data', 'Strelka_and_VarScan', 'VarScan_and_Truth_Data', 'Truth_Data_and_Strelka', 'Strelka_and_VarScan_and_Truth_Data'], 'Positions': [Strelka_Positions, VarScan_Positions, Truth_Positions, Strelka_VarScan_Positions, VarScan_Truth_Positions, Strelka_Truth_Positions, Strelka_VarScan_Truth_Positions]}

# Collecting it into a dataframe.
df3 = pd.DataFrame(data)
print(df3)

# Saving the results in csv.
df3.to_csv('Positions_Count.csv', sep=',', index = None)

# Formulas
Strelka_Exclude = Strelka_Positions - Strelka_VarScan_Positions - Strelka_Truth_Positions - Strelka_VarScan_Truth_Positions
VarScan_Exclude = VarScan_Positions - Strelka_VarScan_Positions - VarScan_Truth_Positions - Strelka_VarScan_Truth_Positions
Truth_Exclude = Truth_Positions - VarScan_Truth_Positions - Strelka_Truth_Positions - Strelka_VarScan_Truth_Positions

# Set of values.
subsets = (Strelka_Exclude, VarScan_Exclude, Strelka_VarScan_Positions, Truth_Exclude, Strelka_Truth_Positions, VarScan_Truth_Positions, Strelka_VarScan_Truth_Positions)

# Adding venn diagram.
v = venn3_unweighted(subsets, set_labels = ('Strelka_0.7', 'VarScan_0.7', 'Truth_Data'), set_colors=('red', 'orange', 'skyblue'))
areas = (1, 1, 1, 1, 1, 1, 1)
centers, radii = _venn3.solve_venn3_circles(areas)

# Saving the values.
plt.title("Positions")
plt.show()
plt.savefig('Tumor_Purity_0.7_Positions_Plot.pdf')
plt.savefig('Tumor_Purity_0.7_Positions_Plot.png', dpi = 300)
