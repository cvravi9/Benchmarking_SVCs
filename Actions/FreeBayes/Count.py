# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Miracum_0.4', 'Miracum_0.7', 'Somatic_0.4', 'Somatic_0.7'], 'SNVs_Count': ['1011639', '1011639', '1011640', '1011639']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('SNVs_Counts.csv', sep='\t', index = None)
