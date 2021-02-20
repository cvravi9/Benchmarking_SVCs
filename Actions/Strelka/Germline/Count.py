# Importing packages.
import numpy as np
import pandas as pd

# Delcaring a new dataframe.
df = []

# Taking all combinations as a list.
data = {'Type': ['Miracum_0.4', 'Miracum_0.7', 'Somatic_0.4', 'Somatic_0.7'], 'Stelka_Germline_SNVs_Count': ['97738', '97738', '97738', '97738']}

# Collecting it into a dataframe.
df = pd.DataFrame(data)
print(df)

# Saving the results in csv.
df.to_csv('Strelka_Germline_SNVs_Counts.csv', sep='\t', index = None)
