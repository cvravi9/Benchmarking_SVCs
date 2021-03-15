# Variants

A variant is an alteration in the most common DNA sequence. In this section, variants from different somatic variant callers are compared with the artifical truth data obtained from https://ftp-trace.ncbi.nlm.nih.gov/

## 1. Inputs

As input, three vcf files from the Strelka somatic variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered, three vcf files from the VarScan variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered alongside the artificial truth vcf file.

## 2. Procedure

The occurance of each variant is calculated from the vcf outcomes using Code.py and then they are normalised with the number of SNPs from each vcf file before checking for bias towards a specific set of variants in different variant callers.

## 3. Outputs

The outcomes for both the cases are csv files that are used for comparisons and plottings.
