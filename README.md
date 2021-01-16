# Goals

* Setting up yaml file for MIRACUM Workflow.
* Executing MIRACUM Workflow for Tumor and Normal Sample.
* Two VCF Files with 0.7 and 0.5 Tumor Purity Sample.
* Comparision of VCF Files.
* Visual Image of VCF Differences.
* Real Data with new Capture Regions.
* Modified Workflow of MIRACUM
* Creating a Sub-Normal Workflow.
* Adding chr to the VCF Files.
* Obtaining Allele Frequency from VCF Files.
* Obtaning Sequencing Depth Information from VCF Files.
* Plotting Allele Frequency & Sequencing Depth Information.

# Meeting Notes

## 13th January 2021

* Extracting the DP from the VCF File for Normal and Tumor Samples.
* Plotting DP values against their positions.
* Removing the comparision between the AF Values.


## 5th January 2021

* Allele frequencies for each VCF file was shown. We just need a comparison.
  * Extract the CHROM and POS lines from each frequency file and merge them into a unique ID (e.g. "chr4:123456"), and extract just the reference allele, which from testing a few alleles we saw it was the first allele mentioned in the allele frequencies.
  * For each chrom:pos ID across your VCF allele frequency files, check that they all have the same REF allele, and print a message if they don't.
  * Extra: take this further, and compare the REF frequencies to see if it is the same across all files.
  * The pandas python library might be very helpful here.


## 9th December 2020

* Compare variant types found in one workflow comapred to another
  * Compare the same for variants only for WF 1, only for WF2, and finally between both
  * E,g, low frequency, or low covereage, depth,
  * Generate plots to represent these
   * Boxplots and violin plots

* Compare varscan somatic against Stryker -- use Ravi's test to quantify those
  * Why the subsampling doesnt work for the Tumor data, why it doesn't work for this dataset
  * It runs fine

* Galaxy wrapper
  * Take BAM and VCF as input in a workflow, run our tool, get the nice plots

## 17th November 2020

* Subset Data
  * Filter BAM file using BED target capture regions, extract the IDs, and filter the FASTQ for pairs.

* Future Ideas:
  * Plot False-Positive Rate against False-Negative Rate, see if there is an optimal crossover point, given changing workflow parameters
