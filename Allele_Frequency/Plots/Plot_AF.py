# Importing the needed packages.
import matplotlib.pyplot as plt
import pandas as pd
import csv

# Mentioning the column names and inputing the csv file.
column_names = ["POS", "ALLELE"]
df = pd.read_csv("Somatic_0.4_AF_Plot.csv", sep= "\t", names=column_names)

# Converting the column into a list.
POS_List = df.POS.to_list()
FREQ_List = df.ALLELE.to_list()

# Printing the list.
print(POS_List)
print(FREQ_List)

# Showing the output and saving it into a PDF.
plt.plot(POS_List, FREQ_List, label='Postions vs Allele Frequency')
plt.show()
plt.savefig('Somatic_0.4_Plot.pdf')
