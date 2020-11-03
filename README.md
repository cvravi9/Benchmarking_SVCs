# Variant Analysis
Performing variant analysis and reporting the differences.

## 1. Comparing and Plotting two VCF files
Given below are the steps involved in obtaining, comparing and plotting two VCF files on Sample Data.

### 1.1. Getting a Workflow to get VCF files
To obtain vcf files from a workflow, "Galaxy_Workflow_MIRACUM_main.ga" of MIRACUM-Pipe-Galaxy is considered. By constructing a yaml as "Galaxy_Workflow_MIRACUM_main.yml" and giving inputs such as is Normal sample name, Normal purity estimate, Tumor sample name, Tumor purity estimate, NORMAL forward reads, NORMAL reverse reads, TUMOR forward reads, TUMOR reverse reads, & Capture regions a vcf file can be obtained. 

Using this yaml file, the process of generating a vcf file can be automated using planemo in the terminal. The command used to generate a vcf file is **"planemo run workflow_name yaml_name --galaxy_url https://usegalaxy.eu/ --galaxy_user_key key_number --engine external_galaxy --no_shed_install"**


### 1.2. Obtaining two VCF files
In order to compare, two varied vcf files are needed. These varied files could be obtained by modifying the yaml file input parameters. For example by changing the "Tumor Purity Estimate" from its considered value of "0.7" to "0.5", two varied vcf files could be obtained. For convenience, two yaml files have been taken instead of modifying one file.

### 1.3. Comparing two VCF files
The to be compared vcf files obtained in the workflow are downloaded from https://usegalaxy.eu/. However, the vcf files aren't indexed and comparision wouldn't be possible. So using "tabix" they are indexed. The command used is **"tabix -p vcf vcf_file"**. The output of the tabix is in vcf extension and to compare two files, the format should be of vcf.gz. 

Therefore using bgzip, the format is changed from "vcf" to "vcf.gz". The command used is **"bgzip -c file.vcf > file.vcf.gz"** and the outcome is then used with bcftools for the comparision. The command for the bcftools is **"bcftools stats file1 file2 > output.txt"** and the outcome is a text file explaning the differences betweeen two vcf files in statistical data.

#### Example Comparison Table

Extracting just the first 5 columns of a VCF file: Chrom, POS, ID, REF, ALT

If all the elements in a row are exactly the same (i.e, all files being compared share the same Chrom,Pos,ID,REF,and ALT), then hide that row in the summary table.


| Chrom-Position | First.vcf | Second.vcf | Third.vcf | .... |
|----------------|-----------|------------|-----------|------|
| chr3:123456    |                | . REF=A, ALT=T | rs123 REF=A ALT=T  | ---- |
| chr3:555555    | . REF=T, ALT=G | . REF=A ALT=G  | rs421 REF=T, ALT=G | ---- |


##### OR Using vcftoolz

VCFToolZ already groups files in nice headers, and produces Venn diagrams (up to 6 files). It would be cool to see these headers in a HTML document, and with the Venn diagrams included.

### 1.4. Plotting Comparision of VCF files
With the textual output, the next goal would be to plot the data and for this "plot-vcfstats" is helpful. The command is **"plot-vcfstats -p venn output.txt"**. However, plotting would need installation of "matplotlib" using **"pip3 install matplotlib"** and "pdflatex".

### 1.5. Filtering VCF File based on Somantic Status of Variant
With respect to the comparision of the vcf files division of the base vcf file is divided into three categories based on Germline, Somatic and LOH. The command is **"bcftools view -i 'SS ~ "2"' vcf-file"**.

