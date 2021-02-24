# Importing the needed packages.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Mentioning the column names and inputing the csv file.
column_names = ["CHROM_POS", "VarScan_Chr", "VarScan_Value", "Strelka_Chr", "Strelka_Value", "Difference", "Chr_Equal"]
df = pd.read_csv("Ultimate_Miracum_AF_Values.csv", sep= "\t", names=column_names)

plt.scatter(df[:,'CHROM_POS'], df[:,'VarScan_Value'])
