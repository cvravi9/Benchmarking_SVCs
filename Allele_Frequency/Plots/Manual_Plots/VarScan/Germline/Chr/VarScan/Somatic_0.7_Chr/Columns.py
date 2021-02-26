# Importing packages.
import numpy as np
import pandas as pd

# Importing vcf files and assigning columns.
dff = pd.read_csv("Somatic_0.7_Chr17.vcf", sep = '\t', index_col= False)
dff.columns = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'NORMAL', 'TUMOR']

# Saving the outcome to csv file.
dff.to_csv('Somatic_0.7_Chr17.vcf', sep='\t', index = None)