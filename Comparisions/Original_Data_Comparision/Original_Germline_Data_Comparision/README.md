# Original Germline Data Comparision

In this comparision, the Germline VCF files created from the Original VCF files are used. Given below is the detailed information.

## 1. Inputs

* The two input vcf files are the Original_Data_Comparision VCF files.

* The first original vcf file with Tumor Sample Purity of 0.7 is named *First-Original.vcf*

* The second original vcf file with the Tumor Sample Purity of 0.4 is named *Second-Original.vcf*

## 2. Procedure

* From the input vcf files, the Germline VCF files are obtained using the command

```
bcftools view -i 'SS ~"1"' First-Original.vcf > First-Germline.vcf
```

* The value for SS is 1 because the Somatic Status value for Germline is 1.

* By executing this command, two Germline VCF files from the Original VCF files can be obtained.

* These vcf files are then compared using the command

```
vcftoolz compare First-Germline.vcf Second-Germline.vcf > Output.txt
```

* Getting allele frequency command

```
vcftools --vcf input.vcf --freq --out output
```

* Getting sequencing depth information

```
vcftools --vcf input.vcf --depth -c > depth_summary.txt
vcftools --vcf input.vcf --site-depth --max-missing 1.0 --out
```

## 3. Outputs

* After the vcftoolz comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.