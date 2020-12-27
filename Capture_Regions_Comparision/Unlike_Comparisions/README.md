# Capture Regions Unlike Comparisions
# Capture Regions Alike Comparisions

In this comparision, vcf files with Unlike Tumor Purity Estimate are visualized through vcftoolz.

## 1. Inputs

* The four input vcf files namely Miracum_0.4.vcf, Miracum_0.7.vcf, Somatic_0.4.vcf & Somatic_0.7.vcf.

* The files with 0.4.vcf are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

## 2. Procedure

* Group the vcf files based on their Tumor Purity Estimate of either 0.7 and 0.4.

* The folder names are *0.4_vs_0.7* & *0.7_vs_0.4*.

* When it is *0.4_vs_0.7* the Miracum Capture Regions vcf file is with the Tumor Purity Estimate of 0.4 and the Somatic Truth Capture Regions vcf file is with the Tumor Purity Estimate of 0.7.

* When it is *0.7_vs_0.4* the Miracum Capture Regions vcf file is with the Tumor Purity Estimate of 0.7 and the Somatic Truth Capture Regions vcf file is with the Tumor Purity Estimate of 0.4.

* Then these vcf files are compared using the command

```
vcftoolz compare first-vcf-file second-vcf-file > Output.txt
```

## 3. Outputs

* After the *vcftoolz* comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.

