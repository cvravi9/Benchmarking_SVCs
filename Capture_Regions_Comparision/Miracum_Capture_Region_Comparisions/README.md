# Miracum Capture Regions Comparisions

In this comparision, vcf files generated using Miracum Capture Regions are visualized through vcftoolz.

## 1. Inputs

* The two input vcf files namely Miracum_0.4.vcf & Miracum_0.7.vcf.

* The file with Miracum_0.4.vcf is with Tumor Sample Purity of 0.4 

* The file with Miracum_0.7.vcf is with Tumor Sample Purity of 0.7.

## 2. Procedure

* Comparing the vcf files using the command

```
vcftoolz compare first-vcf-file second-vcf-file > Output.txt
```

## 3. Outputs

* After the *vcftoolz* comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.

