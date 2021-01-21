# Allele Frequency

In this section, Allele Frequency for the vcf files are filtered and then visualized through three tools.

## 1. Inputs

* The four input vcf files namely Miracum_0.4.vcf, Miracum_0.7.vcf, Somatic_0.4.vcf & Somatic_0.7.vcf.

* The files with 0.4.vcf are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

## 2. Procedure

* The allele frequency for each of the input files are obtained using the command

```
vcftools --vcf input.vcf --freq --out output
```

* The outcome files for allele frequency have five columns namely 'CHROM', 'POS', 'N_ALLELES', 'N_CHR', 'ALLELE:FREQ'.

* Using the code at 'Allele_Frequency.py', 'CHROM', 'POS' are concatenated into 'CHROM-POS'.

* Using the code at 'Allele_Frequency.py', two columns namely 'N_ALLELES', 'N_CHR' are dropped.

* Using the code at 'Allele_Frequency.py', all 'ALLELE:FREQ' are combined into one file along with 'CHROM-POS'.

## 3. Outputs

* After the *vcftoolz* comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
