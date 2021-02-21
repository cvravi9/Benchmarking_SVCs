import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

# Reading csv files and concatinating "CHROM" and "POS"
dff = pd.read_csv("Indexed_Counts.csv", sep = '\t', index_col= False, error_bad_lines=False)
dff.columns = ['REF', 'ALT', 'FreeBayes', 'Strelka', 'VarScan']

# set width of bar
width = 0.25

# Columns from the file
a1 = dff.FreeBayes.to_list()
a2 = dff.Strelka.to_list()
a3 = dff.VarScan.to_list()

# Set position of bar on X axis
r1 = np.arange(len(a1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, a1, color='#7f6d5f', width=barWidth, edgecolor='white', label='var1')
plt.bar(r2, a2, color='#557f2d', width=barWidth, edgecolor='white', label='var2')
plt.bar(r3, a3, color='#2d7f5e', width=barWidth, edgecolor='white', label='var3')

# Add xticks on the middle of the group bars
plt.xlabel('Combinations')
plt.xticks([r + barWidth for r in range(len(a1))], ['AA', 'AT', 'AG', 'AC', 'TT', 'TA', 'TG', 'TC', 'GG', 'GA', 'GT', 'GC', 'CC', 'CA', 'CT', 'CG'])

# Create legend & Show graphic
plt.legend()
plt.show()
plt.savefig('Counts_Plot.pdf')
