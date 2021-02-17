# Importing the needed packages.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Mentioning the column names and inputing the csv file.
column_names = ["CHROM_POS", "VarScan", "Strelka", "Equal", "VarScan_Chr", "VarScan_Value", "Strelka_Chr", "Strelka_Value", "Difference"]
df = pd.read_csv("Final_Miracum_AF_Values.csv", sep= "\t", names=column_names)

# df['Difference'] = df['Difference'].astype(int)
        
# Converting the column into a list.
CHROM_POS_List = df.CHROM_POS.to_list()
Difference_List = df.VarScan_Value.to_list()
Sum_List = df.Strelka_Value.to_list()

print(CHROM_POS_List)
print(Difference_List)
print(Sum_List)

# Final_Difference = Difference_List.astype(np.float)
# [float(i) for i in Difference_List]

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 27743
colors = np.random.rand(N)

plt.scatter(CHROM_POS_List, Difference_List, s=None, c=colors, alpha=0.1, label='Postions vs VarScan')
plt.scatter(CHROM_POS_List, Sum_List, s=None, c=colors, alpha=0.1, label='Postions vs Strelka')
# plt.xticks([])
# plt.yticks([])
plt.legend()
plt.show()
plt.savefig('Test_Scatter.pdf')
