# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Strelka_Normal', 'Strelka_Tumor', 'VarScan', 'Truth_Data'], '<=(0.25)': ['496', '1032', '0', '0'], '<=(0.50)': ['561', '0', '0', '1032'], '<=(0.75)': ['2', '0', '1032', '0'], '<=(1.00)': ['0', '0', '0', '0']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('Tumor_0.5_AF_Counts.csv', sep=',', index=False, encoding='utf-8')