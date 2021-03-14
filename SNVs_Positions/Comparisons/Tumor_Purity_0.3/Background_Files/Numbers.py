# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Strelka_Tumor_Purity_0.3', 'Strelka_Tumor_Purity_0.5', 'Strelka_Tumor_Purity_0.7'], 'Strelka_Positions': ['13315', '13315', '13315'], 'Strelka_SNPs': ['12897', '12897', '12897']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('Strelka_Counts.csv', sep=',', index = None)
