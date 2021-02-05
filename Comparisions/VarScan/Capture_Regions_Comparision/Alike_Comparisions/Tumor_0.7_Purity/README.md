# Capture Regions Alike Comparisions - Tumor Purity - 0.7

In this comparision, vcf files with Tumor Purity Estimate of 0.7 are visualized through vcftoolz.

## 1. Inputs

* The two input vcf files to be compared are named *Miracum_0.7.vcf* & *Somatic_0.7.vcf*.

* Both these files are with Tumor Sample Purity of 0.7.

## 2. Procedure

* The vcf files are compared using the command

```
vcftoolz compare first-vcf-file second-vcf-file > Output.txt
```

## 3. Outputs

* After the *vcftoolz* comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
