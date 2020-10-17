# variant-analysis
Performing variant analysis and reporting the differences.

## Getting a Workflow to get VCF files
To obtain vcf files from a workflow, "Galaxy_Workflow_MIRACUM_main.ga" of MIRACUM-Pipe-Galaxy is considered. By constructing a yaml as "Galaxy_Workflow_MIRACUM_main.yml" and giving inputs such as is Normal sample name, Normal purity estimate, Tumor sample name, Tumor purity estimate, NORMAL forward reads, NORMAL reverse reads, TUMOR forward reads, TUMOR reverse reads, & Capture regions a vcf file can be obtained. 

Using this yaml file, the process of generating a vcf file can be automated using planemo in the terminal. The command used to generate a vcf file is **"planemo run workflow_name yaml_name --galaxy_url https://usegalaxy.eu/ --galaxy_user_key key_number --engine external_galaxy --no_shed_install"**


## Obtaining two VCF files
In order to compare, two varied vcf files are needed. These varied files could be obtained by modifying the yaml file input parameters. For example by changing the "Tumor Purity Estimate" from its considered value of "0.7" to "0.5", two varied vcf files could be obtained. For convenience, two yaml files have been taken instead of modifying one file.

## Comparing two VCF files
The vcf files obtained in the workflow are downloaded to be compared. However, the format in which they are wouldn't help in comparision. So "tabix" 
