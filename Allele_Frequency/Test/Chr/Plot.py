# Importing the needed packages.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Mentioning the column names and inputing the csv file.
column_names = ["CHROM_POS", "VarScan", "Strelka", "Equal", "VarScan_Chr", "VarScan_Value", "Strelka_Chr", "Strelka_Value", "Difference"]
df = pd.read_csv("Chr5.csv", sep= "\t", names=column_names)

# Converting the column into a list.
CHROM_POS_List = df.CHROM_POS.to_list()
VarScan_List = df.VarScan_Value.to_list()
Strelka_List = df.Strelka_Value.to_list()

x = np.arange(len(CHROM_POS_List))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, VarScan_List, width, label='VarScan')
rects2 = ax.bar(x + width/2, Strelka_List, width, label='Strelka')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Score Scale')
ax.set_title('Allele Frequency Value')
ax.set_xticks(x)
ax.set_xticklabels(CHROM_POS_List)
ax.legend()

plt.show()
plt.savefig('Test_Chr5.pdf')
