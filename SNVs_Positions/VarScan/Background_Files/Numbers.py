# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['VarScan_Tumor_Purity_0.3', 'VarScan_Tumor_Purity_0.5', 'VarScan_Tumor_Purity_0.7'], 'Strelka_Positions': ['29316', '29294', '29171'], 'Strelka_SNPs': ['26312', '26290', '26185']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('VarScan_Counts.csv', sep=',', index = None)
