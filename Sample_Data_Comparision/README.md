# Sample Data Comparision

In this comparision, the vcf files created with the sample data are used. Given below is the detailed information.

## 1. Inputs

* The forward and reverse reads for the Normal and Tumor Sample have been downloaded from 

```
https://zenodo.org/record/2582555/files/SLGFSK-N_231335_r1_chr5_12_17.fastq.gz
```

* The input for the Capture Regions file name is *capture_targets_chr5_12_17.bed* and it can be downloaded from

```
https://zenodo.org/record/2582555/files/SLGFSK-N_231335_r2_chr5_12_17.fastq.gz
```

* The workflow used to generate the vcf files are *Galaxy_Workflow_MIRACUM_main.ga* and the workflow has been downloaded from

```
Yet to be updated.
```

* The yaml file used to generate the vcf files are *Galaxy_Workflow_MIRACUM_main.yml*

## 2. Procedure

* To generate the vcf files from the terminal, use this command while ensuring the inputs are in the same folder

```
planemo run workflow_name yaml_name --galaxy_url https://usegalaxy.eu/ --galaxy_user_key key_number --engine external_galaxy --no_shed_install
```

* Ensure that there are two yaml files with different Tumor Sample Purity i.e. 0.7 and 0.5.

* After the workflows are completed, the vcf files are downloaded from *https://usegalaxy.eu/* using *wget*.

* Then these vcf files are compared using the command

```
vcftoolz compare first-vcf-file second-vcf-file > Output.txt
```

### 2.1. Purity Sample Values

* The first vcf file is created with the Normal Sample Purity of 1.0 and Tumor Sample Purity of 0.7.

* The second vcf file is created with the Normal Sample Purity of 1.0 and Tumor Sample Purity of 0.5.

## 3. Outputs

* After the *vcftoolz* comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
