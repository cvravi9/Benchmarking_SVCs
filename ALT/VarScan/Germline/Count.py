# Importing the needed packages.
import numpy as np
import pandas as pd

# Importing the csv file.
dff = pd.read_csv("Somatic_0.7.csv", sep = '\t', index_col= False)

# Mentioning the column names and inputing the csv file.
dff.columns = ['CHROM_POS', 'REF', 'ALT']

# Printing the list.
dff1 = dff[(dff['REF'] == 'A') & (dff['ALT'] == 'A')]
print('The number of REF as A and ALT as A is')
print(len(dff1.index))

dff2 = dff[(dff['REF'] == 'A') & (dff['ALT'] == 'T')]
print('The number of REF as A and ALT as T is')
print(len(dff2.index))

dff3 = dff[(dff['REF'] == 'A') & (dff['ALT'] == 'G')]
print('The number of REF as A and ALT as G is')
print(len(dff3.index))

dff4 = dff[(dff['REF'] == 'A') & (dff['ALT'] == 'C')]
print('The number of REF as A and ALT as C is')
print(len(dff4.index))

dff5 = dff[(dff['REF'] == 'T') & (dff['ALT'] == 'T')]
print('The number of REF as T and ALT as T is')
print(len(dff5.index))

dff6 = dff[(dff['REF'] == 'T') & (dff['ALT'] == 'A')]
print('The number of REF as T and ALT as A is')
print(len(dff6.index))

dff7 = dff[(dff['REF'] == 'T') & (dff['ALT'] == 'G')]
print('The number of REF as T and ALT as G is')
print(len(dff7.index))

dff8 = dff[(dff['REF'] == 'T') & (dff['ALT'] == 'C')]
print('The number of REF as T and ALT as C is')
print(len(dff8.index))

dff9 = dff[(dff['REF'] == 'G') & (dff['ALT'] == 'G')]
print('The number of REF as G and ALT as G is')
print(len(dff9.index))

dff10 = dff[(dff['REF'] == 'G') & (dff['ALT'] == 'A')]
print('The number of REF as G and ALT as A is')
print(len(dff10.index))

dff11 = dff[(dff['REF'] == 'G') & (dff['ALT'] == 'T')]
print('The number of REF as G and ALT as T is')
print(len(dff11.index))

dff12 = dff[(dff['REF'] == 'G') & (dff['ALT'] == 'C')]
print('The number of REF as G and ALT as C is')
print(len(dff12.index))

dff13 = dff[(dff['REF'] == 'C') & (dff['ALT'] == 'C')]
print('The number of REF as C and ALT as C is')
print(len(dff13.index))

dff14 = dff[(dff['REF'] == 'C') & (dff['ALT'] == 'A')]
print('The number of REF as C and ALT as A is')
print(len(dff14.index))

dff15 = dff[(dff['REF'] == 'C') & (dff['ALT'] == 'T')]
print('The number of REF as C and ALT as T is')
print(len(dff15.index))

dff16 = dff[(dff['REF'] == 'C') & (dff['ALT'] == 'G')]
print('The number of REF as C and ALT as G is')
print(len(dff16.index))
