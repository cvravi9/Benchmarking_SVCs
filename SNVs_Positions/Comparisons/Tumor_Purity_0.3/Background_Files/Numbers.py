# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Strelka', 'VarScan', 'Truth_Data', 'Strelka_and_VarScan', 'VarScan_and_Truth_Data', 'Truth_Data_and_Strelka', 'Strelka_and_VarScan_and_Truth_Data'], 'Positions': ['13315', '29316', '1104786', '3104', '2843', '2843', '1052']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('Positions_Count.csv', sep=',', index = None)
