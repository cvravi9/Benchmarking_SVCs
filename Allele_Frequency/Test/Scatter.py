# Importing the needed packages.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Mentioning the column names and inputing the csv file.
column_names = ["CHROM_POS", "VarScan", "Strelka", "Equal", "VarScan_Chr", "VarScan_Value", "Strelka_Chr", "Strelka_Value", "Difference"]
df = pd.read_csv("Boolean_Miracum_AF_Values.csv", sep= "\t", names=column_names)

# Converting the column into a list.
CHROM_POS_List = df.CHROM_POS.to_list()
Difference_List = df.Difference.to_list()


plt.scatter(CHROM_POS_List, Difference_List, label='Positions vs Allele Frequency')
plt.xticks([])
plt.yticks([])
plt.legend()
plt.show()
plt.savefig('Test_Scatter.pdf')
