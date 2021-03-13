# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Tumor_Purity_0.3', 'Tumor_Purity_0.5', 'Tumor_Purity_0.7'], 'Strelka_Deletions_Count': ['296', '296', '296']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('Strelka_Deletions_Counts.csv', sep='\t', index = None)
