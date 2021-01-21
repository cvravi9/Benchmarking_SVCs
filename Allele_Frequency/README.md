# Allele Frequency

In this section, Allele Frequency for the vcf files are filtered and then visualized through two tools.

## 1. Inputs

* The four input vcf files namely Miracum_0.4.vcf, Miracum_0.7.vcf, Somatic_0.4.vcf & Somatic_0.7.vcf.

* The files with 0.4.vcf are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

## 2. Procedure

* Group the vcf files based on their Tumor Purity Estimate of either 0.7 and 0.4.

* The folder names are *Tumor_0.4_Purity* & *Tumor_0.7_Purity*.

* Then these vcf files are compared using the command

```
vcftoolz compare first-vcf-file second-vcf-file > Output.txt
```

* Getting allele frequency command

```
vcftools --vcf input.vcf --freq --out output
```

## 3. Outputs

* After the *vcftoolz* comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
