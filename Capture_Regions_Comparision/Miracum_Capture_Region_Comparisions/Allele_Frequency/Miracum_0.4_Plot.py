import matplotlib.pyplot as plt
import pandas as pd
import csv

# x = []
# y = []

# with open('Miracum_0.4_AF_Plot.csv','r') as csvfile:
#        plots = csv.reader(csvfile, delimiter='\t')
#        for row in plots:
#                x.append(int())
#                y.append(int())

column_names = ["POS", "ALLELE"]
df = pd.read_csv("Miracum_0.4_AF_Plot.csv", sep= "\t", names=column_names)
POS_List = df.POS.to_list()
FREQ_List = df.ALLELE.to_list()
print(POS_List)
print(FREQ_List)

plt.plot(POS_List, FREQ_List, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
plt.show()
