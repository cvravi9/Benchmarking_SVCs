# Allele Frequency

Allele frequency, or gene frequency is defined as the relative frequency of an allele at a particular locus in a population, expressed as a fraction or percentage. In this section, allele frequencies from different somatic variant callers are compared with the artifical truth data obtained from https://ftp-trace.ncbi.nlm.nih.gov/

## 1. Inputs

* There are three variant callers

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

* The first set of output allele frequency files are Miracum_0.4.frq, Miracum_0.7.frq, Somatic_0.4.frq, & Somatic_0.7.frq.

* The second set of output allele frequency files are Miracum_0.4.log, Miracum_0.7.log, Somatic_0.4.log, & Somatic_0.7.log.

* The third outcome is 'Allele_Frequency_Values.csv' which comprises all of the 'ALLELE:FREQ' values.
