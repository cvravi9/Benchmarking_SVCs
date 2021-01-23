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

## 3. Outputs

* In the plots, the output files are csv files with the selected columns and the pdfs with mathplotlib plots.

* In the vcftools. the output files are four ldepth files and four log files.
