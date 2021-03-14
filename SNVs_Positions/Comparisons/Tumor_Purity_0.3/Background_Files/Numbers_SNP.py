# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Strelka', 'VarScan', 'Truth_Data', 'Strelka_and_VarScan', 'VarScan_and_Truth_Data', 'Truth_Data_and_Strelka', 'Strelka_and_VarScan_and_Truth_Data'], 'SNPs': ['12897', '26312', '1007793', '2778', '2484', '2484', '875']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('SNPs_Count.csv', sep=',', index = None)
