# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Strelka_Positions', 'VarScan_Positions', 'Truth_Data_Positions', 'Strelka_and_VarScan_Positions', 'VarScan_and_Truth_Data_Positions', 'Truth_Data_and_Strelka_Positions', 'Strelka_VarScan_Truth_Data_Positions'], 'Positions': ['13315', '29316', '1104786', '3104', '2843', '2843', '1052']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('Positions_Counts.csv', sep=',', index = None)
