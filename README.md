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
The to be compared vcf files obtained in after executing the "Galaxy_Workflow_MIRACUM_main.ga" workflow of MIRACUM-Pipe-Galaxy and could be downloaded from the https://usegalaxy.eu/ into the required file using wget. However, the vcf files aren't indexed and a comparision wouldn't be possible. So using the "tabix" command i.e. **"tabix -p vcf vcf_filename"**, the vcf files could be indexed. The output of the tabix command is in vcf extension and to compare two files, the format should be of vcf.gz. 

Therefore, to change this extension, bgzip command is used i.e. **"bgzip -c file.vcf > file.vcf.gz"** and this changes the extensions of the vcf file from "vcf" to "vcf.gz" and this outcome could be used for the comparision. 

##### 1.3.1. Using bcftools
One way to compare two vcf files is by using bcftools and taking the comparision output into a text file. The command for the bcftools is **"bcftools stats vcf_file1 vcf_file2 > output.txt"** and this obtains an outcome text file explaning the differences betweeen two vcf files in statistical data.

##### 1.3.1 Using vcftoolz

VCFToolZ already groups files in nice headers, and produces Venn diagrams (up to 6 files). It would be cool to see these headers in a HTML document, and with the Venn diagrams included. The command is **"vcftoolz compare first-vcf second-vcf"**

### 1.4. Plotting Comparision of VCF files
With the textual output, the next goal would be to plot the data and for this "plot-vcfstats" is helpful. The command is **"plot-vcfstats -p venn output.txt"**. However, plotting would need installation of "matplotlib" using **"pip3 install matplotlib"** and "pdflatex".

### 1.5. Filtering VCF File based on Somantic Status of Variant
With respect to the comparision of the vcf files division of the base vcf file is divided into three categories based on Germline, Somatic and LOH. The command is **"bcftools view -i 'SS ~"2"' vcf-file"**.


##### Meeting - 17-11-20

* Subset Data
  * Filter BAM file using BED target capture regions, extract the IDs, and filter the FASTQ for pairs.

* Future Ideas:
  * Plot False-Positive Rate against False-Negative Rate, see if there is an optimal crossover point, given changing workflow parameters
