# Importing the needed packages.
import numpy as np
import pandas as pd

# Reading the csv input file that is obtained after performing the following operations on the vcf file.
# Step 1 - 'cut -f 1-2,4-5,9-11 Input-VCF-File > Output-VCF-File'
# Step 2 - 'sed '/^#/d' Output-VCF-File > Updated_Output-VCF-File'

# The first step is to selected the needed columns in the vcf file.
# The second step if to eliminate all lines that start with a '#'
dff = pd.read_csv("Selected_Strelka_0.3_SNV.vcf", sep = '\t', index_col= False)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM', 'POS', 'REF', 'ALT', 'FORMAT', 'NORMAL', 'TUMOR']

# Concatinating the "CHROM" and "POS"
dff["CHROM_POS"] = dff['CHROM'].astype(str) + '-' + dff['POS'].astype(str)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['CHROM', 'POS'], axis=1)
cols = dff.columns.tolist()
cols = cols[-1:] + cols[:-1]
dff = dff[cols]

# Adding columns for single read depth value.
dff['REF_U'] = dff["REF"] + "U"
dff['ALT_U'] = dff["ALT"] + "U"

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Normal_DP', 'Normal_FDP', 'Normal_SDP', 'Normal_SUBDP', 'Normal_AU','Normal_CU', 'Normal_GU', 'Normal_TU']] = dff['NORMAL'].str.split(':',expand=True)
dff[['Tumor_DP', 'Tumor_FDP', 'Tumor_SDP', 'Tumor_SUBDP', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU']] = dff['NORMAL'].str.split(':',expand=True)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['FORMAT', 'NORMAL', 'TUMOR', 'Normal_DP', 'Normal_FDP', 'Normal_SDP', 'Normal_SUBDP', 'Tumor_DP', 'Tumor_FDP', 'Tumor_SDP', 'Tumor_SUBDP'], axis=1)

for i in dff['CHROM_POS']:
    dff.loc[dff['REF_U'] == 'AU', 'Normal'] = dff.Normal_AU
    dff.loc[dff['REF_U'] == 'CU', 'Normal'] = dff.Normal_CU
    dff.loc[dff['REF_U'] == 'GU', 'Normal'] = dff.Normal_GU
    dff.loc[dff['REF_U'] == 'TU', 'Normal'] = dff.Normal_TU
    dff.loc[dff['ALT_U'] == 'AU', 'Tumor'] = dff.Tumor_AU
    dff.loc[dff['ALT_U'] == 'CU', 'Tumor'] = dff.Tumor_CU
    dff.loc[dff['ALT_U'] == 'GU', 'Tumor'] = dff.Tumor_GU
    dff.loc[dff['ALT_U'] == 'TU', 'Tumor'] = dff.Tumor_TU

# Creating new columns by splitting the "NORMAL" and "TUMOR" columns by ':' and renaming the new columns based on the format "DP:FDP:SDP:SUBDP:AU:CU:GU:TU"
dff[['Normal_First', 'Normal_Second']] = dff['Normal'].str.split(',',expand=True)
dff[['Tumor_First', 'Tumor_Second']] = dff['Tumor'].str.split(',',expand=True)

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['REF_U', 'ALT_U', 'Normal_AU', 'Normal_CU', 'Normal_GU', 'Normal_TU', 'Tumor_AU', 'Tumor_CU', 'Tumor_GU', 'Tumor_TU', 'Normal','Tumor', 'Normal_Second', 'Tumor_Second'], axis=1)

# Naming the columns after importing the csv file.
dff.columns = ['CHROM_POS', 'REF', 'ALT', 'NORMAL', 'TUMOR']

# Converting string values columans to int.
dff['NORMAL'] = dff['NORMAL'].astype(int)
dff['TUMOR'] = dff['TUMOR'].astype(int)

# Adding columns for single read depth value.
dff['SUM'] = dff["NORMAL"] + dff["TUMOR"]

# Getting Allele Frequency
dff['Allele_Frequency'] = dff['TUMOR']/dff['SUM']

# Dropping of the unnecessary columns and reorganising the columns.
dff = dff.drop(['NORMAL', 'TUMOR', 'SUM'], axis=1)
print(dff)

# Saving the result into a csv file for plotting.
dff.to_csv('Strelka_0.3_SNV.csv', sep=',', index=False, encoding='utf-8')
dff.to_csv('Strelka_0.3_Plot_SNV.csv', sep='\t', index = None)
