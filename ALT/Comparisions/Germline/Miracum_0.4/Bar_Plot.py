import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Indexed_Counts_Comparisions.csv", sep = '\t', index_col= False, error_bad_lines=False)
dff.columns = ['REF', 'ALT', 'FreeBayes', 'Strelka', 'VarScan']

# set width of bar
width = 0.25

# Columns from the file
a1 = dff.FreeBayes.to_list()
a2 = dff.Strelka.to_list()
a3 = dff.VarScan.to_list()

# Set position of bar on X axis
r1 = np.arange(len(a1))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]

# Make the plot
plt.bar(r1, a1, color='#FFD700', width=width, edgecolor='white', label='FreeBayes_Miracum_0.4')
plt.bar(r2, a2, color='#FFA500', width=width, edgecolor='white', label='Strelka_Miracum_0.4')
plt.bar(r3, a3, color='#DC143C', width=width, edgecolor='white', label='VarScan_Miracum_0.4')

# Add xticks on the middle of the group bars
plt.xlabel('Combinations')
plt.xticks([r + width for r in range(len(a1))], ['AA', 'AT', 'AG', 'AC', 'TT', 'TA', 'TG', 'TC', 'GG', 'GA', 'GT', 'GC', 'CC', 'CA', 'CT', 'CG'])

# Create legend & Show graphic
plt.legend()
plt.show()
plt.savefig('Counts_Plot.pdf')
