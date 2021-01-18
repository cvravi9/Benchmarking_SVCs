# Importing the needed packages.
import matplotlib.pyplot as plt
import pandas as pd
import csv

# Mentioning the column names and inputing the csv file.
column_names = ["CHROM_POS", "NORMAL_DP", "TUMOR_DP"]
df = pd.read_csv("Final_Somatic_0.4.csv", sep= "\t", names=column_names)

# Converting the column into a list.
CHROM_POS_List = df.CHROM_POS.to_list()
NORMAL_List = df.NORMAL_DP.to_list()

# Printing the list.
print(CHROM_POS_List)
print(NORMAL_List)

# Showing the output and saving it into a PDF.
plt.plot(CHROM_POS_List, NORMAL_List, label='Position vs Normal Depth')
plt.show()
plt.savefig('Somatic_0.4_Normal_Plot.pdf')
