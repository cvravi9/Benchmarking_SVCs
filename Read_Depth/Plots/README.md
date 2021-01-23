# Read Depth - Plots

In this section, Read Depth for the vcf files is filtered and then visualized using mathplotlib.

## 1. Inputs

* The four input vcf files namely Miracum_0.4.vcf, Miracum_0.7.vcf, Somatic_0.4.vcf & Somatic_0.7.vcf.

* The files with 0.4.vcf are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

## 2. Procedure

* In the first step, a few columns are filtered using the command: 

```
cut -f 1-2, 9-11 Input-VCF-File > Updated-VCF-File
```

* In the second step, lines starting with '#' are removed: 

```
sed '/^#/d' Updated-VCF-File > Final-VCF-File
```

* In the third step, 'CHROM', 'POS' are concatenated into 'CHROM-POS'.

* In the fourth step, the format column is split based on ':' at 'GT:GQ:DP:AD:ADF:ADR' and the columns are named 'Normal-GT', 'Normal-GQ', 'Normal_DP', 'Normal-AD', 'Normal-ADF', 'Normal-ADR', 'Tumor-GT', 'Tumor-GQ', 'Tumor_DP', 'Tumor-AD', 'Tumor-ADF' & 'Tumor-ADR'.

* In the fifth step, 'Normal-GT', 'Normal-GQ', 'Normal-AD', 'Normal-ADF', 'Normal-ADR', 'Tumor-GT', 'Tumor-GQ', 'Tumor-AD', 'Tumor-ADF' & 'Tumor-ADR' are dropped.

## 3. Outputs

* After splitting the format column, the output files are Updated_Miracum_0.4.csv, Updated_Miracum_0.7.csv, Updated_Somatic_0.4.csv & Updated_Somatic_0.7.csv.

* After dropping the unneeded columns, the output files are Final_Miracum_0.4.csv, Final_Miracum_0.7.csv, Final_Somatic_0.4.csv & Final_Somatic_0.7.csv
