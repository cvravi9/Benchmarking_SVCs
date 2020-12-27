# Capture Regions Comparision

In this comparision, the capture regions for the MIRACUM Main Workflow are changed to notice the differences in the vcf outcomes.

## 1. Inputs

* The first capture regions are from MIRACUM Annotated Data with the file name as *capture_targets_chr5_12_17.bed* and it could be downloaded from 

```
https://usegalaxy.eu/u/wolfgang-maier/h/miracum-annotation-data
```

* The second capture regions are from SOMATIC Truth Data and they are downloaded from

```
ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/use_cases/mixtures/UMCUTRECHT_NA12878_NA24385_mixture_10052016/
```

* The workflow used to generate the vcf files are *Galaxy_Workflow_MIRACUM_main.ga* and the workflow has been downloaded from

```
https://github.com/AG-Boerries/MIRACUM-Pipe-Galaxy
```

* The workflow used to generate mapped normal and tumor samples is *Workflow_Filter_FASTQ_on_BAM_File_Capture_Regions.ga*.

* The forward and reverse reads for the Original Normal and Tumor Sample have been downloaded from 

```
ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/use_cases/mixtures/UMCUTRECHT_NA12878_NA24385_mixture_10052016/
```

## 2. Procedure

* Generate the Sub-Original and Sub-Tumor samples by providing the Mapped-Original and Mapped-Tumor samples to *Workflow_Filter_FASTQ_on_BAM_File_Capture_Regions.ga* workflow along with *capture_targets_chr5_12_17.bed* capture regions.

* While selecting the capture regions, only use the MIRACUM Capture Regions with the name *capture_targets_chr5_12_17.bed* and not the Somatic Truth Capture Regions. This is because the Somatic Truth Capture Regions wouldn't deliver a sub-sampled Original-Normal and Original-Tumor Data.

* After generating the mapped Original and Tumor Data, use *Workflow_Cut_of_MIRACUM_Main.ga* to get vcf file outcomes with the tumor purity estimate value of 0.7 and 0.4.

* Use both the capture regions when generating the vcf files with different tumor purity estimates.

## 3. Outputs

* The first vcf is with the tumor purity estimate of 0.4 with MIRACUM Capture Regions named *Miracum_0.4.vcf*.

* The second vcf is with the tumor purity estimate of 0.7 with MIRACUM Capture Regions named *Miracum_0.7.vcf*.

* The first vcf is with the tumor purity estimate of 0.4 with Somatic Truth Capture Regions named *Somatic_0.4.vcf*.

* The first vcf is with the tumor purity estimate of 0.7 with Somatic Truth Capture Regions named *Somatic_0.7.vcf*.

