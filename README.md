# variant-analysis
Performing variant analysis and reporting the differences.

## Getting a Workflow to get VCF files
To obtain vcf files from a workflow, "Galaxy_Workflow_MIRACUM_main.ga" of MIRACUM-Pipe-Galaxy is considered. By constructing a yml as "Galaxy_Workflow_MIRACUM_main.yml" and giving inputs such as is Normal sample name, Normal purity estimate, Tumor sample name, Tumor purity estimate, NORMAL forward reads, NORMAL reverse reads, TUMOR forward reads, TUMOR reverse reads, & Capture regions a vcf file can be obtained. 

Using this yml file, the process of generating a vcf file can be automated using planemo in the terminal. The command used to generate a vcf file is **"planemo run workflow_name yml_name --galaxy_url https://usegalaxy.eu/ --galaxy_user_key key_number --engine external_galaxy --no_shed_install"**

In order to compare two vcf files, the "Tumor Purity Estimate" is considered "0.7" for the first time and "0.5" for the second time.
