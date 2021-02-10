# Truth Data Comparision - First VCF Comparision

In this comparision, the Truth Somatic VCF file is compared to the First Original Data. Given below are the details.

## 1. Inputs

* The first original vcf file with Tumor Sample Purity of 0.7 is named *First-Somatic.vcf*

* The second vcf file is the *Updated-Truth-Somatic.vcf*

## 2. Procedure

* The vcf files are compared using the command

```
vcftoolz compare Updated-Truth-Somatic First-Somatic.vcf > Output.txt
```

## 3. Outputs

* After the vcftoolz comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
