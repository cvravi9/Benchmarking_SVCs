# Sub-Sampled Normal vs Sub-Sampled Tumor Data Comparisions

In this comparision, the Sub-Sampled VCF files created from the original data and *Sub_Sampled_Data_Workflow.ga* are used. Given below is the detailed information.

## 1. Inputs

* The two input vcf files are the Sub-Sampled VCF files.

* The first sub-sampled vcf file with Tumor Sample Purity of 0.7 is named *Sub-Sampled.vcf*

* The second sub-sampled vcf file with the Tumor Sample Purity of 0.4 is named *Sub-Sampled.vcf*

## 2. Procedure

* These vcf files are then compared using the command

```
vcftoolz compare First-Sub-Sampled.vcf Second-Sub-Sampled.vcf > Output.txt
```

## 3. Outputs

* After the vcftoolz comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
