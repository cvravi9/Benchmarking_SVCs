# Original Data Comparision
In this comparision, the original vcf files created with an original data are compared. Given below is the information as to how this task has been accomplished.

## 1. Inputs
* The forward and reverse reads for the Normal and Tumor Sample have been downloaded from 

```
ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/use_cases/mixtures/UMCUTRECHT_NA12878_NA24385_mixture_10052016/
```

* The input for the Capture Regions file name is *capture_targets_chr5_12_17.bed* and it can be downloaded from

```
https://usegalaxy.eu/u/wolfgang-maier/h/miracum-annotation-data
```

* The workflow used to generate the vcf files are *Galaxy_Workflow_MIRACUM_main.ga*.

* The yaml file used to generate the vcf files are *Galaxy_Workflow_MIRACUM_main.yml*

## 2. Procedure
* To generate the vcf files from the terminal, use this command while ensuring the inputs are in the same folder

```
planemo run workflow_name yaml_name --galaxy_url https://usegalaxy.eu/ --galaxy_user_key key_number --engine external_galaxy --no_shed_install
```

* Ensure there are two yaml files with different tumor sample purity.

* After the workflows are completed, the vcf files are downloaded from *https://usegalaxy.eu/* using *wget*.

* The vcf files are compared using the command

```
vcftoolz compare first-vcf-file second-vcf-file
```

## 3. Alternate Workflow
*
## 4. Constrains

## 5. Outputs

The first vcf file is obtained with the tumor sample purity of 0.7.
The second vcf file is obtained with the tumor sample purity of 0.4.
