# Allele Frequency - vcfstats
In this section, Allele Frequency for the vcf files are visualized using vcfstats tool.

## 1. Inputs

* The four input vcf files namely Miracum_0.4.vcf, Miracum_0.7.vcf, Somatic_0.4.vcf & Somatic_0.7.vcf.

* The files with 0.4.vcf are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

## 2. Procedure

* The overall allele frequency distribution through the vcfstats is obtained from the input files using the command

```
vcfstats --vcf exmaple.vcf --formula 'AAF ~ 1' --outdir Directory_Name --title 'Overall allele frequency distribution'
```

* The number of variants on each chromosome through the vcfstats is obtained from the input files using the command

```
vcfstats --vcf example.vcf --formula 'COUNT(1) ~ CONTIG' --outdir Directory_Name --title 'Number of Variants on Each Chromosome'
```

* Counting type of mutant genotypes for sample on each chromosome is obtained from the input files using the command

```
vcfstats --vcf example.vcf --formula 'COUNT(1, group=GTTYPEs[HET,HOM_ALT]{0}) ~ CHROM' --outdir Directory_Name --title 'Counting Type of Mutant Genotypes (HET, HOM_ALT) for Sample 1 on each Chromosome'
```

## 3. Outputs

* For each input vcf file there are 'Overall allele frequency distribution', 'Number of Variants on Each Chromosome', & 'Counting Type of Mutant Genotypes for each Chromosome' in a new directory namely 'Miracum_0.4', 'Miracum_0.7', 'Somatic_0.4' & 'Somatic_0.7'.

