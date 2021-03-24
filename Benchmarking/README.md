# Benchmarking

Benchmarking is defined as a standard or point of reference against which things may be compared. In this section, ALT variants from the different somatic variant callers are compared with the artifical truth data obtained from https://ftp-trace.ncbi.nlm.nih.gov/

## 1. Inputs

As input, three vcf files from the Strelka somatic variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered, three vcf files from the VarScan variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered alongside the artificial truth vcf file.

## 2. Procedure

For each somatic variant caller, ALT comparison are performed to obtain True Positives, True Negatives, False Positives & False Negatives.

## 3. Outputs

The outcomes for both the cases are csv files that are used for comparisons and plottings.
