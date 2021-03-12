import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

# set width of bar
width = 0.25

# Columns from the file
a1 = [469, 561, 2, 0]
a2 = [1032, 0, 0, 0]
a3 = [0, 0, 1032, 0]
a4 = [0, 1032, 0, 0]

# Set position of bar on X axis
r1 = np.arange(len(a1))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]
r4 = [x + width for x in r3]

# Make the plot
plt.bar(r1, a1, color='#FFD700', width=width, edgecolor='white', label='Strelka_Normal')
plt.bar(r2, a2, color='#FFA500', width=width, edgecolor='white', label='Strelka_Tumor')
plt.bar(r3, a3, color='#FF1493', width=width, edgecolor='white', label='VarScan')
plt.bar(r4, a4, color='#FF0000', width=width, edgecolor='white', label='Truth_Data')

# Add xticks on the middle of the group bars
plt.xlabel('Tumor_0.3_Allele_Frequencies')
plt.xticks([r + width for r in range(len(a1))], ['<= 0.25', '<= 0.50', '<= 0.75', '<= 1.00'])

# Create legend & Show graphic
plt.legend()
plt.show()
plt.savefig('Tumor_0.3_AF_Plot.pdf')
