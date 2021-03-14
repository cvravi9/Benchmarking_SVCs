# Allele Frequency

Allele frequency, or gene frequency is defined as the relative frequency of an allele at a particular locus in a population, expressed as a fraction or percentage. In this section, allele frequencies from different somatic variant callers are compared with the artifical truth data obtained from https://ftp-trace.ncbi.nlm.nih.gov/

## 1. Inputs

As input, three vcf files from the Strelka somatic variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered, three vcf files from the VarScan variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered alongside the artificial truth data vcf file.

## 2. Procedure

For the Strelka somatic variant caller vcf outcomes, allele frequencies are obtained for tumor and normal values using the formulas provided at https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/README.md#somatic while for VarScan variant caller, allele frequencies are obtained using the command **vcftools --vcf input.vcf --freq --out output**

## 3. Outputs

The outcomes for both the cases are csv files that are used for comparisons and plottings.
