# variant-analysis
Performing variant analysis and reporting the differences.

## Getting a Workflow to get VCF files
To obtain vcf files from a workflow, "Galaxy_Workflow_MIRACUM_main.ga" of MIRACUM-Pipe-Galaxy is considered. By constructing a yml as "Galaxy_Workflow_MIRACUM_main.yml" and giving inputs such as is Normal sample name, Normal purity estimate, Tumor sample name, Tumor purity estimate, NORMAL forward reads, NORMAL reverse reads, TUMOR forward reads, TUMOR reverse reads, & Capture regions. 

With the yml files created, the process of generating a vcf file can be automated using planemo. The command used is "**planemo run workflow_name yml_name --galaxy_url https://usegalaxy.eu/ --galaxy_user_key key_number --engine external_galaxy --no_shed_install**"
