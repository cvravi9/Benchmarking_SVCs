# Read Depth

Read Depth describes the number of times that a given nucleotide in the genome has been read in an experiment.In this section, read depths from different somatic variant callers are compared with the artifical truth data obtained from https://ftp-trace.ncbi.nlm.nih.gov/

## 1. Inputs

As input, three vcf files from the Strelka somatic variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered, three vcf files from the VarScan variant caller with the tumor purity of 0.3, 0.5 and 0.7 respectively are considered alongside the artificial truth vcf file.

## 2. Procedure

For the Strelka somatic variant caller, read depth value is taken from **DP** in FORMAT with **DP : FDP : SDP : SUBDP : AU : CU : GU : TU** and it has Normal and Tumor Read Depth. For the VarScan somatic variant caller, read depth value is taken from DP in FORMAT with **GT : GQ : DP : AD : ADF : ADR** and it has Normal and Tumor Read Depth. For Somatic Truth Data, read depth value is taken from DP in FORMAT with **GT : PS : DP : GQ** and it is the only read depth.

## 3. Outputs

The outcomes for both the cases are csv files that are used for comparisons and plottings.
