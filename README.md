# Variant Analysis
Performing variant analysis and reporting the differences.

## 1. Comparing and Plotting two VCF files
Given below are the steps involved in obtaining, comparing and plotting two VCF files on Sample Data.

### 1.1. Getting a Workflow to get VCF files
To obtain vcf files from a workflow, "Galaxy_Workflow_MIRACUM_main.ga" of MIRACUM-Pipe-Galaxy is considered. By constructing a yaml as "Galaxy_Workflow_MIRACUM_main.yml" and giving inputs such as is Normal sample name, Normal purity estimate, Tumor sample name, Tumor purity estimate, NORMAL forward reads, NORMAL reverse reads, TUMOR forward reads, TUMOR reverse reads, & Capture regions a vcf file can be obtained. 

Using this yaml file, the process of generating a vcf file can be automated using planemo in the terminal. The command used to generate a vcf file is **"planemo run workflow_name yaml_name --galaxy_url https://usegalaxy.eu/ --galaxy_user_key key_number --engine external_galaxy --no_shed_install"**


### 1.2. Obtaining two VCF files
In order to compare, two varied vcf files are needed. These varied files could be obtained by modifying the yaml file input parameters. For example by changing the "Tumor Purity Estimate" from its considered value of "0.7" to "0.5", two varied vcf files could be obtained. For convenience, two yaml files have been taken instead of modifying one file.

### 1.3. VCF file Formats
To start comparing, the obtained vcf files are neither indexed nor with the proper extension for a comparision. So after executing the "Galaxy_Workflow_MIRACUM_main.ga" workflow of MIRACUM-Pipe-Galaxy and downloading the vcf files from the https://usegalaxy.eu/, use the "tabix" command i.e. **"tabix -p vcf vcf_filename"** and the vcf files are indexed. The output of the tabix command is in vcf extension and to compare two files, the format should be of vcf.gz. 

Therefore, to change this extension, bgzip command is used i.e. **"bgzip -c file.vcf > file.vcf.gz"** and this changes the extensions of the vcf file from "vcf" to "vcf.gz" and this outcome could be used for the comparision. 

### 1.4. Comparing VCF files
With the vcf files indexed and in vcf.gz extension, there are two ways to compare them. The first of the two ways is using bcftools and the second tool that could be used is the vcftoolz. The difference is that in bcftools another command is needed for visulization while for vcftoolz completes the comparision and visualization by venn diagrams.

#### 1.4.1. Comparision by bcftools
Through bcftools compairison, the outcome of two vcf files is added into a text file and the command is **"bcftools stats vcf_file1 vcf_file2 > output.txt"**. However the outcome obtained only explans the differences in statistical data.

With the textual output, the next goal would be to plot the data and for this "plot-vcfstats" is helpful. The command is **"plot-vcfstats -p venn output.txt"**. However, plotting would need installation of "matplotlib" using **"pip3 install matplotlib"** and "pdflatex" to create the final pdf outcome.

#### 1.4.2. Comparision by vcftoolz
Another tool to compare two vcf files is the "VCF Toolz" and the command is **"vcftoolz compare first-vcf second-vcf"**. With this tool, along with the textual outcome, there are venn diagrams comparing the snps and positions in both the vcf files.

### 1.5. Sub VCF File
Post comparisions of the entire file, the vcf file could be divided in five sub files based on the somatic status. Out of the five of them, three divisions are taken as a seperate sub-vcf files namely Germline, Somatic and LOH. For these divisions, the somatic status also referred to as SS is 1, 2 & 3 respectively. In order to obtain the sub-files, the command used is **"bcftools view -i 'SS ~"2"' vcf-file"**.

#### 1.5.1. Chr Comparisions
When comparing two vcf files, a point to be noted is that ##contig=<ID=chr9, length=23,assembly=b73> and ##contig=<ID=9, length=23,assembly=b73> cannot be compared. So a small command would ensure that chr is added in the second vcf file.

```
awk 
      '{if($0 !~ /^#/) 
      print "chr"$0; 
      else if(match($0,/(##contig=<ID=)(.*)/,m)) 
      print m[1]"chr"m[2]; 
      else print $0}' 
      basic.vcf > modified.vcf
```

# Meeting Notes

## 17th November 2020

* Subset Data
  * Filter BAM file using BED target capture regions, extract the IDs, and filter the FASTQ for pairs.

* Future Ideas:
  * Plot False-Positive Rate against False-Negative Rate, see if there is an optimal crossover point, given changing workflow parameters
