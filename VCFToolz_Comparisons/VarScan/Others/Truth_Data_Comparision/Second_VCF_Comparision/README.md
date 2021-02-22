# Truth Data Comparision - Second VCF Comparision

In this comparision, the Truth Somatic VCF file is compared to the Second Original Data. Given below are the details.

## 1. Inputs

* The first original vcf file with Tumor Sample Purity of 0.4 is named *Second-Somatic.vcf*

* The second vcf file is the *Updated-Truth-Somatic.vcf*

## 2. Procedure

* The vcf files are compared using the command

```
vcftoolz compare Updated-Truth-Somatic Second-Somatic.vcf > Output.txt
```

## 3. Outputs

* After the vcftoolz comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
