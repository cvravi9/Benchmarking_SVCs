# Original Somatic Data Comparision

In this comparision, the somatic vcf files created from the original vcf files are used. Given below is the detailed information.

## 1. Inputs

* The two input vcf files are the Original_Data_Comparision VCF files.

* The first original vcf file with Tumor Sample Purity of 0.7 is named *First-Original.vcf*

* The second original vcf file with the Tumor Sample Purity of 0.4 is named *Second-Original.vcf*

## 2. Procedure

* From the input vcf files, the Somatic VCF files are obtained using the command

```
bcftools view -i 'SS ~"2"' First-Original.vcf > First-Somatic.vcf
```

* The value for SS is 2 because the Somatic Status value for Somatic is 2.

* By executing this command, two Somatic VCF files from the Original VCF files can be obtained.

* These vcf files are then compared using the command

```
vcftoolz compare First-Somatic.vcf Second-Somatic.vcf > Output.txt
```

## 3. Outputs

* After the vcftoolz comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
