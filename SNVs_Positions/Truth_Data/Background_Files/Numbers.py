# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Truth_Data'], 'Truth_Data_Positions': ['1104786'], 'Truth_Data_SNPs': ['1007793']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('Truth_Data_Counts.csv', sep=',', index = None)
