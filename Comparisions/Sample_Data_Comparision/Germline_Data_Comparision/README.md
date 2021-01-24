# Sample Germline Data Comparision

In this comparision, the Germline VCF files created from the Sample VCF files are used. Given below is the detailed information.

## 1. Inputs

* The two input vcf files are the Sample_Data_Comparision VCF files.

* The first sample vcf file with Tumor Sample Purity of 0.7 is named *First-Sample.vcf*

* The second sample vcf file with the Tumor Sample Purity of 0.5 is named *Second-Sample.vcf*

## 2. Procedure

* From the input vcf files, the Germline VCF files are obtained using the command

```
bcftools view -i 'SS ~"1"' First-Sample.vcf > First-Germline.vcf
```

* The value for SS is 1 because the Somatic Status value for Germline is 1.

* By executing this command, two Sample VCF files from the Sample VCF files can be obtained.

* These vcf files are then compared using the command

```
vcftoolz compare First-Germline.vcf Second-Germline.vcf > Output.txt
```

## 3. Outputs

* After the vcftoolz comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
