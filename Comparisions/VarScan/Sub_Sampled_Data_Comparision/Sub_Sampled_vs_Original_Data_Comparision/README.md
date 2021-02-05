# Sub-Sampled vs Original Data Comparision

In this comparision, the Sub-Sampled VCF files and Original VCF files are compared. Given below is the detailed information.

## 1. Inputs

* The four input vcf files are the Original VCF files and Sub-Sampled VCF files.

* The first vcf files are with the Tumor Sample Purity of 0.7 and they are *Original.vcf* & *Sub-Sampled.vcf*

* The second vcf files are with the Tumor Sample Purity of 0.4 and they are *Original.vcf* & *Sub-Sampled.vcf*

## 2. Procedure

* These vcf files are then compared using the command

```
vcftoolz compare Original.vcf Sub-Sampled.vcf > Output.txt
```

## 3. Outputs

* After the vcftoolz comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.

