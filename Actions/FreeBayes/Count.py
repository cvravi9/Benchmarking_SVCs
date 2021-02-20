# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Miracum-0.4', 'Miracum_0.7', 'Somatic_0.4', 'Somatic_0.7'], 'Deletion_Count': ['4382', '4382', '4385', '4382']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('Deletions_Counts.csv', index=False, encoding='utf-8')
