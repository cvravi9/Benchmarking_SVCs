# Positions, SNPs and INDELs

A single-nucleotide polymorphism is a substitution of a single nucleotide at a specific position in the genome that is present in a sufficiently large fraction of the population. Indel is a molecular biology term for an insertion or deletion of bases in the genome of an organism. In this section, Positions, SNPs and INDELs from different somatic variant callers are compared with the artifical truth data obtained from https://ftp-trace.ncbi.nlm.nih.gov/ 

## 1. Inputs

As input, three vcf files from the Strelka somatic variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered, three vcf files from the VarScan variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered alongside the artificial truth vcf file.

## 2. Procedure

From the vcf files, positions could be obtained by using the command **cut -f 2,4-5 Input.vcf > Output.vcf** and then calculating the length of the **POS** column. The SNPs can be obtained from the vcf files using the command **vcftools --vcf input_file.vcf --remove-indels --recode --recode-INFO-all --out SNPs_only** and then calculate the SNPs as mentioned in the Code_SNPs.py. The INDELs can be obtained from the vcf files using the command **vcftools --vcf input_file.vcf --keep-only-indels --recode --recode-INFO-all --out INDELs_only** and then calculate the INDELs as mentioned in the Code_INDELs.py.

## 3. Outputs

The outcomes for both the cases are csv files that give the number of positions, SNPs, and INDELs in Strelka, VarScan and Truth_Data alongside venn diagrams visualizing the outcome.
