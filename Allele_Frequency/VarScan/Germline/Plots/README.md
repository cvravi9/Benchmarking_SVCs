# Allele Frequency - Plots

In this section, Allele Frequency Plots are visualized using the mathplotlib package.

## 1. Inputs

* For the plotting, the four input vcf files namely Miracum_0.4_AF_Plot.csv, Miracum_0.7_AF_Plot.csv, Somatic_0.4_AF_Plot.csv & Somatic_0.7_AF_Plot.csv.

* The files with 0.4.csv are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

* Each of these csv files have two columns namely 'POS' & 'ALLELE:FREQ'.

## 2. Procedure

* The csv input files are obtained by using the 'Plot_AF.py'

* Through 'Plot_AF.py' only the selected columns are choosen and are then saved as csv files.

* Using the Miracum_0.4_AF_Plot.py, Miracum_0.7_AF_Plot.py, Somatic_0.4_AF_Plot.py & Somatic_0.7_AF_Plot.py plotting is accomplished with 'POS' on the x-axis and 'ALLELE:FREQ' on the y-axis.


## 3. Outputs

* The four plots for each input file are namely Miracum_0.4_Plot.pdf, Miracum_0.7_Plot.pdf, Somatic_0.4_Plot.pdf & Somatic_0.7_Plot.pdf.
