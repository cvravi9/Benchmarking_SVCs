# Importing the needed packages.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Mentioning the column names and inputing the csv file.
column_names = ["CHROM_POS", "VarScan", "Strelka", "Equal", "VarScan_Chr", "VarScan_Value", "Strelka_Chr", "Strelka_Value", "Difference"]
df = pd.read_csv("Chr17.csv", sep= "\t", names=column_names)

# Converting the column into a list.
CHROM_POS_List = df.CHROM_POS.to_list()
VarScan_List = df.VarScan_Value.to_list()
Strelka_List = df.Strelka_Value.to_list()

x = np.arange(len(CHROM_POS_List))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.barh(x, VarScan_List, width, color='red', label='VarScan')
rects2 = ax.barh(x + width, Strelka_List, width, color='yellow', label='Strelka')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Score Scale')
ax.set_title('Allele Frequency Value')
ax.set_yticks(x)
ax.set_yticklabels(CHROM_POS_List)
ax.legend()

plt.show()
plt.savefig('Test_Chr17.pdf')
